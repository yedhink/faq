from django.db import models

class HOD(models.Model):
    name = models.CharField(max_length=30)
    branch_id = models.IntegerField()

class Question(models.Model):
    query = models.CharField(max_length=300)
    branch_id = models.ForeignKey(HOD,on_delete=models.CASCADE)
    query_date = models.DateField('date asked')

