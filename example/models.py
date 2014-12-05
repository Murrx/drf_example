from django.db import models


class Example(models.Model):
    foo = models.CharField(max_length=200)
    bar = models.CharField(max_length=200)
