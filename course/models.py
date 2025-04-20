from django.db import models
from urllib.parse import urlparse, parse_qs
from django.utils.text import slugify
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='subjects/')
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    youtube_url = models.URLField()
    duration = models.CharField(max_length=20)
    students_count = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    review_count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    @property
    def video_id(self):
        try:
            query = urlparse(self.youtube_url)
            video_id = parse_qs(query.query).get('v')
            if video_id:
                return video_id[0]
        except:
            return None


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.DurationField()
    order = models.PositiveIntegerField(default=1)  # dars tartib raqami

    class Meta:
        ordering = ['order']  # avtomatik tartiblash

    def __str__(self):
        return f"{self.course.name} - {self.order}. {self.title}"


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name}"


class Quiz(models.Model):
    course = models.ForeignKey('Course', related_name='quiz', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.question