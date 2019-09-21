from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post,PostType
from .forms import PostForm

def get_news(request):
    return get_all_posts(request, PostType.NEWS)
    
def get_blogs(request):
    return get_all_posts(request, PostType.BLOG)

def get_all_posts(request, show_only=None):
    """
    Creates a view that will return all the posts that are published and by 
    ordering them by importance first, then date
    """
    if(show_only == None):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-is_important', '-published_date')
    else:
        posts = Post.objects.filter(post_type__exact=show_only.name).filter(published_date__lte=timezone.now()).order_by('-is_important', '-published_date')
    return render(request, "posts.html", {"posts": posts})
    
    
def post_detail(request, pk):
    """
    Return and render a single post with all its details.
    Will return an error if post is not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "details.html", {"post": post})
    
def show_post_form(request, pk=None):
    """
    Displays a view that will allow form input. If pk is not NULL then show 
    the post to edit. Otherwise it will be an empty form to create anew
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    
    else:
        form = PostForm(instance=post)
    return render(request, "postform.html", {"post":post})