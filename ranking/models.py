from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Swordfighter(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    appears_on = models.CharField(max_length=100)
    description = models.TextField()
    profile_img = CloudinaryField('image', default='placeholder')
    upvotes = models.ManyToManyField(User, related_name="swordfighter_upvotes", blank=True)

    class meta:
        ordering = ['upvotes']

    def __str__(self):
        return self.name
    
    def number_of_upvotes(self):
        return self.upvotes.count()



