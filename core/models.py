from django.db import models
from projects.models import Project

# Create your models here.

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    def __str__(self):
        return f"{self.author} ({self.role})"

class NowItem(models.Model):
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.description

class Resume(models.Model):
    pdf_file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Resume {self.id}"
