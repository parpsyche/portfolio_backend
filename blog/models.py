from django.db import models
from projects.models import Tag, Category

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    content = models.TextField()
    summary = models.CharField(max_length=300, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    published_at = models.DateTimeField()
    author = models.CharField(max_length=100)
    reactions = models.JSONField(default=dict, blank=True)  # e.g., {"like": 0, "love": 0}
    comments_enabled = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reactions = models.JSONField(default=dict, blank=True)
    def __str__(self):
        return f"Comment by {self.author_name} on {self.blogpost.title}"
