from django.db import models

class employees(models.Model):
    employee_name=models.CharField(max_length=255)
    employee_id=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
