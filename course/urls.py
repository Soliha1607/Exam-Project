from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/<slug:slug>/', views.subject_courses, name='subject_courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/quiz/', views.quiz_page, name='quiz_page'),
    path('course/<int:course_id>/quiz/submit/', views.submit_quiz, name='submit_quiz'),
    path('purchase/', views.purchase_page, name='purchase'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('courses/<int:course_id>/comment/', views.add_comment, name='add_comment'),
]
