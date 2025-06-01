from django.db import models

from common.models import BaseModel, MediaFile


class Brand(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    logo = models.ImageField(upload_to='brands', null=True, blank=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='categories', null=True, blank=True)

    def __str__(self):
        return self.name


class Size(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Color(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    default_images = models.ManyToManyField('common.MediaFile', blank=True)
    stock = models.IntegerField(default=0, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductVariant(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    images = models.ManyToManyField('common.MediaFile', blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField(default=0, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

