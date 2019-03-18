from django.db import models

# Create your models here.


class BookDetail(models.Model):
    b_id = models.CharField(max_length=100, primary_key=True, blank=False, default='')
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    published_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

