from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=250)
    ingredients = models.TextField()
    link = models.URLField(max_length=600)

    def __str__(self):
        return self.name

