from django.db import models
class stud(models.Model):
    stud_id = models.CharField(max_length=90)
    name = models.CharField(max_length=30)
    Age = models.CharField(max_length=90)
    
    
    class Meta:
        db_table = "stud"
class dept(models.Model):
    dept_id = models.CharField(max_length=90)
    name = models.CharField(max_length=30)
    
    
    class Meta:
        db_table = "dept"
# Create your models here.
