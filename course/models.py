from django.db import models
from urllib.parse import urlparse, parse_qs
from django.utils.text import slugify

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
