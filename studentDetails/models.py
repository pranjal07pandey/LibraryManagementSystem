from django.db import models

# Create your models here.


class StudentsDetail(models.Model):
    s_id = models.CharField(max_length=100, primary_key=True, blank=False, default='')
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, default='')
    contactNo = models.CharField(max_length=100, blank=False)
    dateOfBirth = models.DateField()
    rollNumber = models.IntegerField(blank=False)
    guardianName = models.CharField(max_length=100, blank=False)
    batch = models.CharField(max_length=100, blank=False)
    grade = models.IntegerField(blank=False)
    section = models.CharField(max_length=10, blank=True, default='')
    gender = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField()

    def __str__(self):
        return self.name

