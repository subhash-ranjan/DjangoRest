from django.db import models

class Employee(models.Model):
    empId = models.IntegerField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)