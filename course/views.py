from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject, Course, Comment, Student, Quiz
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse


def index(request):
    subjects = Subject.objects.all()

    for subject in subjects:
        courses = Course.objects.filter(subject=subject)
        all_comments = Comment.objects.filter(course__in=courses)

        if all_comments.exists():
            total_rating = sum(comment.rating for comment in all_comments)
            average_rating = round(total_rating / all_comments.count(), 1)
        else:
            average_rating = 0

        subject.avg_rating = average_rating

    return render(request, 'index.html', {'subjects': subjects})

def subject_courses(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    courses = Course.objects.filter(subject=subject)
    return render(request, 'subject_courses.html', {
        'subject': subject,
        'courses': courses,
    })

def purchase_page(request):
    return render(request, 'purchase.html')

def about(request):
    return render(request, 'about.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')  # yoki asosiy sahifa
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)

            # YANGI QO‘SHILDI: student profile ham yaratyapmiz
            Student.objects.create(user=user)

            login(request, user)
            return redirect('index')
    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def add_comment(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # Student mavjudligini tekshirish
    student, created = Student.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        text = request.POST.get('text')
        rating = request.POST.get('rating')

        if text and rating:
            comment = Comment.objects.create(
                course=course,
                student=student,
                text=text,
                rating=rating,
                created_at=timezone.now()
            )

            all_comments = course.comments.all()
            total_rating = sum(c.rating for c in all_comments)
            course.review_count = all_comments.count()
            course.rating = round(total_rating / course.review_count, 1)
            course.save()

    return redirect('subject_courses', slug=course.subject.slug)


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    comments = course.comments.all().order_by('-created_at')
    return render(request, 'course_detail.html', {'course': course, 'comments': comments})


def quiz_page(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = Quiz.objects.filter(course=course)

    return render(request, 'quiz_page.html', {
        'course': course,
        'quizzes': quizzes
    })


def submit_quiz(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    score = 0
    for quiz in Quiz.objects.filter(course=course):
        user_answer = request.POST.get(f'question_{quiz.id}')
        if user_answer == quiz.correct_option:
            score += 1

    return HttpResponse(f'Your score: {score} out of {len(Quiz.objects.filter(course=course))}')
