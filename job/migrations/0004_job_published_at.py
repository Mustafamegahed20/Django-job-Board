# Generated by Django 4.0.3 on 2022-03-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
