from django.db import models


class Task(models.Model):
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    title = models.CharField('название',max_length=50)
    availability = models.BooleanField(default=True, verbose_name='azyrky uchurda barbi')
    image = models.ImageField(upload_to='p/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Book(models.Model):
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    name = models.CharField('название',max_length=50)
    availability = models.BooleanField(default=True, verbose_name='azyrky uchurda barbi')
    image = models.ImageField(upload_to='p/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.book