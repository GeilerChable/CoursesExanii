from tkinter import CASCADE
import datetime

from django.db import models
from django.utils import timezone

class Course(models.Model):
    course_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField("date published")

    def __str__(self):
        return self.course_text

    def was_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Student(models.Model):
    student= models.CharField(max_length=150)
    school= models.CharField(max_length=200)
    course= models.ForeignKey(Course, models.CASCADE, related_name="students")