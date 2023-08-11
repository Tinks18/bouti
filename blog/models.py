
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


STATUS = ((0, "Draft"), (1, "Published"))


class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
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
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="response")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Response {self.body} by {self.name}"


class Review(models.Model):
    """ Product review model """
    user = models.ForeignKey(
        User, related_name="review_user", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250, null=False, blank=False)
    product_name = models.CharField(max_length=150, null=False, blank=False)
    content = models.TextField(max_length=10000, null=False, blank=False)
    review_date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    class Meta:
        ordering = ["-review_date"]

    def __str__(self):
        return str(self.title)
