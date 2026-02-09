from django.shortcuts import render
from .models import Profile, Project, Skill

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    # Group skills by category
    frontend_skills = skills.filter(category='frontend')
    backend_skills = skills.filter(category='backend')
    tools_skills = skills.filter(category='tools')
    
    return render(request, 'core/home.html', {
        'profile': profile, 
        'projects': projects,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'tools_skills': tools_skills,
    })