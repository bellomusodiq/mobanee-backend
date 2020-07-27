from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=225)
    aka = models.CharField(max_length=225)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']


class Contact(models.Model):
    email = models.EmailField(max_length=225)
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-pk']


class Comment(models.Model):
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    comment = models.CharField(max_length=400)
    image = models.ImageField(upload_to='comments')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
