from django.contrib import admin
from .models import Subject, Course


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'duration', 'students_count', 'rating', 'price')
    list_filter = ('subject',)
    search_fields = ('name', 'subject__name')
