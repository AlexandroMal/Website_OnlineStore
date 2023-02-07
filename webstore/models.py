from django.db import models

class telephonesBase(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    img_full = models.ImageField(upload_to="telephones/full/%Y/%m/%d/")
    img_contraction = models.ImageField(upload_to="telephones/contraction/%Y/%m/%d/")
