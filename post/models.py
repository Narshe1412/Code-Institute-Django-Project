from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from enum import Enum

# Create your models here.

        
class PostType(Enum):
    """
    Stores an enumeration to distinguish between types of post
    """
    NEWS = "News Post"
    BLOG = "Blog Post"


class Post(models.Model):
    """
    Stores the information for a news or blog post for the site
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, 
        default=timezone.now)
    views = models.IntegerField(default=0)
    tag=models.CharField(max_length = 30, blank=True, null=True)
    image=models.ImageField(upload_to="img", blank=True, null=True)
    author = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    post_type = models.CharField(
      max_length=5,
      choices=[(tag, tag.value) for tag in PostType],
      default=PostType.BLOG
    )
    is_important = models.BooleanField(default=False)
    
    
    def __unicode__(self):
        return self.title
