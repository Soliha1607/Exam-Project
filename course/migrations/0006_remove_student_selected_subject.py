# Generated by Django 5.2 on 2025-04-20 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_youtube_url_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='selected_subject',
        ),
    ]
