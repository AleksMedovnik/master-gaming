from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')

    class Meta:
        ordering = ['-date_pub', ]
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})



class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    price = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    image = models.ImageField(upload_to='images/', default='images/default.png')

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    email = models.CharField(max_length=150, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='', blank=True, null=True)

    def __str__(self):
        return self.name