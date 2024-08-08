from django.db import models

class man(models.Model):
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    class Meta:
        db_table="man"

class Admin(models.Model):
  name=models.CharField(max_length=50);
  price=models.FloatField()
  quantity= models.IntegerField()
  image=models.CharField(max_length=2083)
  class Meta:
    db_table="Admin"
    