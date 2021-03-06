from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumb = models.ImageField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Skill(models.Model):
    text = models.TextField(default='')

class Work(models.Model):
    job_title = models.CharField(max_length=200)
    time_frame = models.CharField(max_length=50)
    text = models.TextField(default='')

class Education(models.Model):
    school = models.CharField(max_length=200)
    qualification = models.CharField(max_length=50)
    text = models.TextField(default='')
