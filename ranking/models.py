from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Pending Approval'), (1, 'Published'), (2, 'Published with edit'), (3, 'Disapproved'))


class Swordfighter(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    appears_on = models.CharField(max_length=100)
    description = models.TextField()
    profile_img = CloudinaryField('image', default='placeholder')
    upvotes = models.ManyToManyField(User, related_name="swordfighter_upvotes", blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    suggested_by = models.CharField(max_length=100, default='admin')


    class meta:
        ordering = ['upvotes']

    def __str__(self):
        return self.name
    
    def number_of_upvotes(self):
        return self.upvotes.count()


class Comment(models.Model):
    swordfighter = models.ForeignKey(Swordfighter, on_delete=models.CASCADE, related_name="comments")
    submitted_by = models.CharField(max_length=100)
    submitted_on_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    flags = models.ManyToManyField(User, related_name='comment_flag', blank=True)

    class Meta:
        ordering = ["-submitted_on_date"]

    def __str__(self):
        return f"{self.submitted_by} on {self.submitted_on_date} - {self.content}"
        
    def count_flags(self):
        return self.flags.count()

