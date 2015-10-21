from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    slug = models.SlugField(blank=True)
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey('Category')
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.id:
            #Newly Created Object
            self.slug = slugify(self.title)

        super(Product, self).save(*args,**kwargs)

    def __str__(self):
        return "%s (%s) - %s" % (self.title,self.brand.name, self.category)

class Category(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey("self", related_name="children", blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    pass

class CarItem(models.Model):
    pass