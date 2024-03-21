from django.db import models
class register(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)


# Create your models here.
