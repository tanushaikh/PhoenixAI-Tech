from django.db import models
from django.contrib.auth.models import User

class TechBlog(models.Model):
    title = models.CharField(max_length=255)
    
    short_description = models.TextField(max_length=500)
    content = models.TextField()

    featured_image = models.ImageField(upload_to='blogs/', blank=True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    tags = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated tags"
    )

    views_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
