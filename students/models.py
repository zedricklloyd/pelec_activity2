
from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    birthdate = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField()

    previous_school = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    guardian = models.CharField(max_length=200)

    course = models.CharField(max_length=100)
    year_level = models.CharField(max_length=50)
    section = models.CharField(max_length=50)

    school_year = models.CharField(max_length=20)
    semester = models.CharField(max_length=50)
    enrollment_status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
