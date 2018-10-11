from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Course(models.Model):
    """
    owner    : The instructor that related this course
    subject  : The subject that this course belongs to. 
               A Foreign Key that points to the subject model
    title    : The title of the course
    slug     : The slug of the course. This will be used in URL's later
    overview : This is a TextField column to include an overview about this 
               course
    created  : The date and time when the course was created 

    """
    owner = models.ForeignKey(
        User, related_name='course_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(
        Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
