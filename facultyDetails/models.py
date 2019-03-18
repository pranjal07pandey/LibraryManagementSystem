from django.db import models

# Create your models here.


class FacultyDetails(models.Model):
    f_id = models.CharField(primary_key=True, max_length=100, default='')
    contact = models.CharField(max_length=100, blank=False, default='')
    name = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField()
    designation = models.CharField(max_length=100, blank=False, default='')
    subject = models.CharField(max_length=100, blank=True, default='')

