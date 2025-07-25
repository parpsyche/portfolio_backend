from rest_framework import serializers
from .models import Testimonial, NowItem, Resume

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class NowItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowItem
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__' 