from django.db import models


# Create your models here.
class results(models.Model):
    project_name=models.CharField(max_length=255,default='new project')
    test_name=models.CharField(max_length=255)
    duration=models.FloatField()
    test_outcome=models.CharField(max_length=255)
    longrep=models.CharField(max_length=10000)
    created_at=models.DateTimeField()
    employee_id=models.CharField(max_length=255)
    employee_name=models.CharField(max_length=255)
    plat_form=models.CharField(max_length=1000)
    python=models.CharField(max_length=255)

    
    
