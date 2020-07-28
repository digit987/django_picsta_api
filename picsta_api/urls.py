from django.urls import path
from picsta_api import views


urlpatterns = [
    path('users', views.UserView.as_view(), name="users"),
    path('users/<int:pk>', views.UserView.as_view(), name="users"),
    path('photos', views.PhotoView.as_view(), name="photos"),
    path('photos/<int:pk>', views.PhotoView.as_view(), name="photos"),
    path('posts', views.PostView.as_view(), name="post"),
    path('posts/<int:pk>', views.PostView.as_view(), name="posts"),
]
