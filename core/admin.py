from django.contrib import admin
from .models import Profile, Project, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'title', 'bio', 'email', 'image')}),
        ('Social Links', {'fields': ('github_url', 'linkedin_url')}),
        ('Files', {'fields': ('cv_file',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Project Details', {'fields': ('title', 'description', 'image')}),
        ('Technical Info', {'fields': ('tech_stack',)}),
        ('Links', {'fields': ('github_link', 'live_demo_link')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('category', 'order')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Skill Info', {'fields': ('name', 'category', 'proficiency', 'order')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )