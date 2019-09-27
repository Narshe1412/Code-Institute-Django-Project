from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from post.models import Post

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    content = models.TextField(verbose_name="Your comment")
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return "{0} {1}-{2} - {3}".format(self.created, self.id, self.post.title, self.author)
    
