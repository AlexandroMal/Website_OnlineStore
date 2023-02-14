from django.db import models
from django.urls import reverse

class product_data(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=0)
    img_full = models.ImageField(upload_to="telephones/")
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ('post', kwargs={'slug_post': self.slug})
    
    class Meta:
        verbose_name = 'All product'
        ordering = ['title', 'id']
        

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('category', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id', 'name']
