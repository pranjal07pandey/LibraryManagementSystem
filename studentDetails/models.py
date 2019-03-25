from django.db import models
from details.models import BookDetail
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
        return self.s_id


class BookIssue(models.Model):
    s_id = models.ForeignKey(StudentsDetail, on_delete=models.CASCADE)
    b_id = models.ForeignKey(BookDetail, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)

    #
    # def __str__(self):
    #     return self.b_id




# class BookReturn(models.Model):
