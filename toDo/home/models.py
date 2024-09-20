from django.db import models

# Create your models here

class todoList(models.Model):
    item=models.CharField(max_length=200)
    status=models.CharField(max_length=100, default="In progress")