from django.db import models

class Question(models.Model):
    query = models.CharField(max_length=300)
    branch_id = models.IntegerField()
    query_date = models.DateField('date asked')

class Departments(models.Model):
    