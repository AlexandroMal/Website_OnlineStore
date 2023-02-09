from django.db import models

class telephones_Base(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=0)
    img_full = models.ImageField(upload_to="telephones/")
   
    
class notebook_Base(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=0)
    img_full = models.ImageField(upload_to="notebook/")
  
    
class desktop_Base(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=0)
    img_full = models.ImageField(upload_to="desktop/")

    
class console_Base(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=0)
    img_full = models.ImageField(upload_to="console/")
    
