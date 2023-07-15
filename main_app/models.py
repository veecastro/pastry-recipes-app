from django.db import models
from django.urls import reverse

# Create your models here.
class Pastryrecipe(models.Model):
    title = models.CharField(max_length=100)
    preptime = models.IntegerField()
    cookingtime = models.IntegerField()
    totaltime = models.IntegerField()
    yields = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    # photo_url = models.URLField()


    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})