from django.db import models
from django.shortcuts import reverse

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

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.png')

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title