from django.contrib import admin
from .models import Subject, Course, Student, Module, Comment, Quiz
from django.contrib.admin.sites import site


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'duration', 'students_count', 'rating', 'price')
    list_filter = ('subject',)
    search_fields = ('name', 'subject__name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_subject')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'duration')
    list_filter = ('course',)
    search_fields = ('title', 'course__name')
    ordering = ('order',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'rating', 'created_at')
    list_filter = ('course', 'rating')
    search_fields = ('student__user__username', 'course__name')


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'course', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option')
    search_fields = ('question', 'course__name')
    list_filter = ('course',)
