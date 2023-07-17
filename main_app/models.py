from django.db import models
from django.urls import reverse

# Create your models here.
class Pastryrecipe(models.Model):
    title = models.CharField(max_length=100)
    preptime = models.IntegerField()
    cookingtime = models.IntegerField()
    totaltime = models.IntegerField()
    yields = models.IntegerField()
    instructions = models.TextField()
    ingredients = models.TextField()
    img = models.ImageField(upload_to='photos/', blank=True)
    
    def __str__(self):
      return f'{self.title} ({self.id})'

    def get_absolute_url(self):
      return reverse('detail', kwargs={'recipe_id': self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    recipe = models.ForeignKey(Pastryrecipe, on_delete=models.CASCADE)

    def __str__(self):
      return f"Photo for {self.recipe_id} @ {self.url}"