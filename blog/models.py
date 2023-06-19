from django.db import models


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Main blog post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


# class Contact(models.Model):
#     name = models.CharField(max_length=158)
#     email = models.EmailField()
#     message = models.TextField()

#     def __str__(self):
#         return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email