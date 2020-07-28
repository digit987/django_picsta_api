from rest_framework import serializers
from picsta_api.models import Reply, Comment, Password, LogInHistory, Followers, Following, User, Tag, Photo, Post

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id',
                  'text',
                  'timestamp',
                  'likes')

class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True)
    class Meta:
        model = Comment
        fields = ('id',
                  'text',
                  'timestamp',
                  'likes',
                  'replies')

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ('id',
                  'password',
                  'timestamp')

class LogInHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogInHistory
        fields = ('id',
                  'location',
                  'device',
                  'timestamp')

class FollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Followers
        fields = ('id',
                  'username')

class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Following
        fields = ('id',
                  'username')

class UserSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    passwords = PasswordSerializer(many=True)
    log_in_history = LogInHistorySerializer(many=True)
    followers = FollowersSerializer(many=True)
    following = FollowingSerializer(many=True)
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'passwords',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'created_on',
                  'log_in_history'
                  'bio',
                  'followers',
                  'following',
                  'comments')

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id',
                  'username')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id',
                  'username')

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id',
                  'username',
                  'timestamp',
                  'location',
                  'photo_id',
                  'tags',
                  'comments')
