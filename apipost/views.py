from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
# Create your views here.
# PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer