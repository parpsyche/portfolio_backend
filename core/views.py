from django.shortcuts import render
from rest_framework import viewsets
from .models import Testimonial, NowItem, Resume
from .serializers import TestimonialSerializer, NowItemSerializer, ResumeSerializer

# Create your views here.

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('-date')
    serializer_class = TestimonialSerializer

class NowItemViewSet(viewsets.ModelViewSet):
    queryset = NowItem.objects.all().order_by('-start_date')
    serializer_class = NowItemSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all().order_by('-created_at')
    serializer_class = ResumeSerializer
