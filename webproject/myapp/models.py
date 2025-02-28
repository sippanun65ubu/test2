from django.db import models

# Create your models here.
class Course(models.Model):
    Course_id = models.CharField(max_length=100)
    Course_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
