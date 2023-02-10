from django.db import models
from django.urls import reverse

class product_data(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=0)
    img_full = models.ImageField(upload_to="telephones/")
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse ('category', kwargs={'cat_id': self.pk})
