from django.shortcuts import render
from .models import SiteProfile, Skill, Experience, Education, Language


def cv_view(request):
    """Display the dynamic CV page"""
    profile = SiteProfile.objects.first()
    skills = Skill.objects.filter(is_active=True).select_related('category')
    experiences = Experience.objects.filter(is_active=True).order_by('-start_date')
    educations = Education.objects.filter(is_active=True).order_by('-start_date')
    languages = Language.objects.filter(is_active=True)
    
    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'languages': languages,
    }
    
    return render(request, 'cv/cv.html', context)
