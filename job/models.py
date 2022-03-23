from django.db import models
JOB_Type=(
    ('part time','part time'),
    ('full time','full time'),
)
# Create your models here.
class job(models.Model):
    title = models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=JOB_Type) 
    Description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary =models.IntegerField(default=1)
    experience=models.IntegerField(default=0)
    

    def __str__(self):
        return self.title