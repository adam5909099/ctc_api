# Generated by Django 3.0.5 on 2020-04-11 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_resume_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='description_html',
        ),
    ]