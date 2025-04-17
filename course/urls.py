from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/<slug:slug>/', views.subject_courses, name='subject_courses'),
]
