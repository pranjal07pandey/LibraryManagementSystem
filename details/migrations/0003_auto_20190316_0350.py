# Generated by Django 2.1.7 on 2019-03-16 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_bookdetail_b_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='bookdetail',
            name='b_id',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
