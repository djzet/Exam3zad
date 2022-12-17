from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'name'
