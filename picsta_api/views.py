from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from picsta_api.models import Reply, Photo, Password, LogInHistory, Followers, Following, User, Tag, Photo, Post
from picsta_api.serializers import ReplySerializer, PhotoSerializer, PasswordSerializer, LogInHistorySerializer, FollowersSerializer, FollowingSerializer, UserSerializer, TagSerializer, PhotoSerializer, PostSerializer
from django.http import HttpResponse
# Create your views here.

class UserView(APIView):
    @parser_classes([JSONParser])
    def post(self, request):
        user_data = request.data
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
            if pk:
                user = get_object_or_404(User.objects.all(), pk=pk)
                user_serializer = UserSerializer(user)
                if user_serializer:
                    return JsonResponse(user_serializer.data, safe=False, status=status.HTTP_200_OK)
                return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = User.objects.all()
                user_serializer = UserSerializer(user, many=True)
                if user_serializer:
                    return JsonResponse(user_serializer.data, safe=False, status=status.HTTP_200_OK)
                return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @parser_classes([JSONParser])
    def put(self, request, pk):
        update_user_data = get_object_or_404(User.objects.all(), pk=pk)
        user_data = request.data
        user_serializer = UserSerializer(instance=update_user_data, data=user_data, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @parser_classes([JSONParser])
    def delete(self, request, pk=None):
        try:
            if pk:
                delete_user_data = get_object_or_404(User.objects.all(), pk=pk)
                delete_user_data.delete()
                return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                delete_user_data = User.objects.all()
                delete_user_data.delete()
                return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoView(APIView):
    @parser_classes([JSONParser])
    def post(self, request):
        photo_data = request.data
        photo_serializer = PhotoSerializer(data=photo_data)
        if photo_serializer.is_valid(raise_exception=True):
            photo_serializer.save()
            return JsonResponse(photo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:
            photo = get_object_or_404(Photo.objects.all(), pk=pk)
            photo_serializer = PhotoSerializer(user)
            if photo_serializer.is_valid(raise_exception=True):
                return JsonResponse(photo_serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            photo = Photo.objects.all()
            photo_serializer = PhotoSerializer(photo, many=True)
            if Photo_serializer.is_valid(raise_exception=True):
                return JsonResponse(photo_serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @parser_classes([JSONParser])
    def put(self, request, pk):
        update_photo_data = get_object_or_404(Photo.objects.all(), pk=pk)
        photo_data = request.data
        photo_serializer = PhotoSerializer(instance=update_photo_data, data=photo_data, partial=True)
        if photo_serializer.is_valid(raise_exception=True):
            photo_serializer.save()
            return JsonResponse(photo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @parser_classes([JSONParser])
    def delete(self, request, pk=None):
        try:
            if pk:
                delete_photo_data = get_object_or_404(Photo.objects.all(), pk=pk)
                delete_photo_data.delete()
                return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                delete_photo_data = Photo.objects.all()
                delete_photo_data.delete()
                return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostView(APIView):
    @parser_classes([JSONParser])
    def post(self, request):
        post_data = request.data
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid(raise_exception=True):
            Post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:
            post = get_object_or_404(Photo.objects.all(), pk=pk)
            photo_serializer = PhotoSerializer(user)
            if Photo_serializer.is_valid(raise_exception=True):
                return JsonResponse(photo_serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            photo = Photo.objects.all()
            photo_serializer = PhotoSerializer(photo, many=True)
            if photo_serializer.is_valid(raise_exception=True):
                return JsonResponse(photo_serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @parser_classes([JSONParser])
    def put(self, request, pk):
        update_photo_data = get_object_or_404(Photo.objects.all(), pk=pk)
        photo_data = request.data
        photo_serializer = PhotoSerializer(instance=update_photo_data, data=photo_data, partial=True)
        if photo_serializer.is_valid(raise_exception=True):
            photo_serializer.save()
            return JsonResponse(photo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @parser_classes([JSONParser])
    def delete(self, request, pk=None):
        try:
            if pk:
                delete_photo_data = get_object_or_404(Photo.objects.all(), pk=pk)
                delete_photo_data.delete()
                return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                delete_photo_data = Photo.objects.all()
                delete_photo_data.delete()
                return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
