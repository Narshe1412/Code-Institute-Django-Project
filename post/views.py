from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post,PostType
from comments.models import Comment
from .forms import PostForm
from comments.forms import CommentForm

def get_news(request):
    """ Get all the posts that are of type NEWS """
    return get_all_posts(request, PostType.NEWS)
    
def get_blogs(request):
    """ Get all the posts that are of type BLOG """
    return get_all_posts(request, PostType.BLOG)

def get_all_posts(request, show_only=None):
    """
    Creates a view that will return all the posts that are published and by 
    ordering them by importance first, then date
    """
    if(show_only == None):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-is_important', '-published_date')
        title = "All Posts"
    else:
        posts = Post.objects.filter(post_type__exact=show_only.name).filter(published_date__lte=timezone.now()).order_by('-is_important', '-published_date')
        title = show_only.name
    return render(request, "posts.html", {"posts": posts, "title": title})
    
    
def post_detail(request, pk):
    """
    Return and render a single post with all its details.
    Will return an error if post is not found
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all
    post.views += 1
    post.save()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid() and request.user:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
    elif request.user:
        comment_form = CommentForm()
    
    return render(request, "details.html", {"post": post, "comments": comments, "comment_form": comment_form})
    
    
def show_post_form(request, pk=None):
    """
    Displays a view that will allow form input. If pk is not NULL then show 
    the post to edit. Otherwise it will be an empty form to create anew
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    header = "Edit \"{0}\"".format(post.title) if pk else "New Post"
    title = "Edit #{0}".format(pk) if pk else "New Post"
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.instance.author = request.user
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "postform.html", {"form":form, "title": title, "header": header})