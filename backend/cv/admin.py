from django.contrib import admin
from .models import SiteProfile, SkillCategory, Skill, Experience, Education, Language


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']
    search_fields = ['full_name', 'email']
    ordering = ['full_name']


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level', 'is_active']
    list_filter = ['category', 'level', 'is_active']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'is_current', 'is_active']
    list_filter = ['is_current', 'is_active', 'start_date']
    search_fields = ['company', 'position', 'description']
    ordering = ['-start_date']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'field_of_study', 'start_date', 'is_active']
    list_filter = ['is_active', 'start_date']
    search_fields = ['institution', 'degree', 'field_of_study']
    ordering = ['-start_date']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'is_active']
    list_filter = ['proficiency', 'is_active']
    search_fields = ['name']
    ordering = ['name']
