# Generated by Django 5.2 on 2025-04-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_module_student_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='youtube_url',
            field=models.TextField(help_text='Separate URLs with commas if multiple videos'),
        ),
    ]
