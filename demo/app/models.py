from django.db import models
class prdct(models.Model):
    p_id = models.CharField(max_length=90,primary_key="True")
    p_name = models.CharField(max_length=30)
    p_price = models.CharField(max_length=90)
    p_pic = models.CharField(max_length=90)
    
    
    class Meta:
        db_table = "prdct"

# Create your models here.
class odr(models.Model):
    o_id= models.CharField(max_length=90,primary_key="True")
    p_id=models.ForeignKey(prdct,on_delete=models.CASCADE)
    o_date=models.CharField(max_length=30)
    o_qnty=models.CharField(max_length=30)
    o_sts=models.CharField(max_length=30)
    class Meta:
        db_table = "odr"

class idgen(models.Model):
    p_id=models.IntegerField()
    o_id=models.IntegerField()
    class Meta:
        db_table = "idgen"
