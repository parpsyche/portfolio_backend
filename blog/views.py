from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer, CommentSerializer
from rest_framework.response import Response

# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-published_at')
    serializer_class = BlogPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        blogpost_id = self.request.query_params.get('blogpost')
        if blogpost_id:
            queryset = queryset.filter(blogpost=blogpost_id)
        return queryset
