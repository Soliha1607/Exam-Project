from django.shortcuts import render, get_object_or_404
from .models import Subject, Course

def index(request):
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'subjects': subjects})

def subject_courses(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    courses = Course.objects.filter(subject=subject)
    return render(request, 'subject_courses.html', {
        'subject': subject,
        'courses': courses,
    })
