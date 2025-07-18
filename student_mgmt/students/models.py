from django.db import models
from datetime import date

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    reg_date = models.DateField(default=date.today)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='student_pics/', blank=True, null=True)

    def __str__(self):
        return self.name

