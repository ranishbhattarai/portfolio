from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    bio=models.TextField()
    image=models.ImageField(upload_to='profile/')
    email=models.EmailField(blank=True, null=True)
    github_url=models.URLField(blank=True, null=True)
    linkedin_url=models.URLField(blank=True, null=True)
    cv_file=models.FileField(upload_to='cv/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Skill(models.Model):
    SKILL_CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools & Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=SKILL_CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80, help_text="Proficiency level 0-100")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.name
