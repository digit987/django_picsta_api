from djongo import models
from django import forms
from datetime import date
# Create your models here.

class Reply(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=70, blank=False, default='')
    timestamp = models.DateTimeField(default=date.today)
    likes = models.IntegerField()
    def __str__(self):
        return self.text

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=70, blank=False, default='')
    timestamp = models.DateTimeField(default=date.today)
    likes = models.IntegerField()
    replies = models.ArrayField(
        model_container=Reply
    )

    def __str__(self):
        return self.text

class Password(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=70, blank=False)
    timestamp = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.password

class LogInHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=70, blank=False)
    device = models.CharField(max_length=70, blank=False)
    timestamp = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.location

class Followers(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return self.username

class Following(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return self.username

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField(max_length=70, blank=False, default='')
    passwords = models.ArrayField(
        model_container=Password
    )
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70, blank=False, default='')
    date_of_birth = models.DateTimeField(blank=False)
    created_on = models.DateTimeField(default=date.today)
    log_in_history = models.ArrayField(
        model_container=LogInHistory
    )
    bio = models.CharField(max_length=100, blank=False, default='')
    followers = models.ArrayField(
        model_container=Followers
    )
    following = models.ArrayField(
        model_container=Following
    )
    comments = models.ArrayField(
        model_container=Comment
    )

    def __str__(self):
        return self.username

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return self.username

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    #Created By
    username = models.CharField(max_length=70, blank=False, default='')
    #Created On
    timestamp = models.DateTimeField(default=date.today)
    #Created At Location
    location = models.CharField(max_length=70, blank=False)
    #Photo Id
    photo_id = models.IntegerField()
    #Tags
    tags = models.ArrayField(
        model_container=Tag
    )
    #Comments
    comments = models.ArrayField(
        model_container=Comment
    )
    def __str__(self):
        return "Post by " + self.username

class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    #Created By
    username = models.CharField(max_length=70, blank=False, default='')
