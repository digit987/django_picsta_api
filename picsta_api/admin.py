from django.contrib import admin
from .models import Reply, Comment, Password, LogInHistory, Followers, Following, User, Tag, Photo, Post
# Register your models here.
admin.site.register([Reply, Comment, Password, LogInHistory, Followers, Following, User, Tag, Photo, Post])
