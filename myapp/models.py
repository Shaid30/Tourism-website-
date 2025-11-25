from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/',default='default.jpg')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Destination(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='destinations')
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class About(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)  # left side big image

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='team/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=300, blank=True)
    icon_class = models.CharField(max_length=100, blank=True, help_text="(optional) icon class if using fontawesome or similar")

    def __str__(self):
        return self.name


class GalleryCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="gallery/")
    uploaded_to = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else "Image"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog/')
    short_description = models.CharField(max_length=100)
    content = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

        def __str__(self):
            return self.title
        

