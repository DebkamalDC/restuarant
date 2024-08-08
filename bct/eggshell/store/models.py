from django.db import models

class man(models.Model):
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    class Meta:
        db_table="man"

    