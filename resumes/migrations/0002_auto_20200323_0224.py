# Generated by Django 3.0.4 on 2020-03-23 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='position',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]