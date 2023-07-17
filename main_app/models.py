from django.db import models
from django.urls import reverse

# Create your models here.

CATEGORY = (
   ('CC', 'Cakes and Cupcakes'),
   ('PT', 'Pies and Tarts'),
   ('CB', 'Cookies and Bisquits'),
   ('PP', 'Pastries and Puff Pastry'),
   ('FD', 'Frozen Desserts'),
   ('PC', 'Puddings and Custards'),
   ('FR', 'Fruit-based Desserts'),
   ('ID', 'International Desserts'),
   ('OT', 'Other Desserts'),
)

class Pastryrecipe(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=4,
      choices=CATEGORY,
      default=CATEGORY[0][0])
    preptime = models.IntegerField()
    cookingtime = models.IntegerField()
    totaltime = models.IntegerField()
    yields = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    img = models.ImageField(upload_to='recipes/', blank=True)
    
    def __str__(self):
      return f'{self.title} ({self.id})'

    def get_absolute_url(self):
      return reverse('detail', kwargs={'recipe_id': self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    recipe = models.ForeignKey(Pastryrecipe, on_delete=models.CASCADE)

    def __str__(self):
      return f"Photo for recipe_id: {self.recipe_id} @ {self.url}"


class Category(models.Model):
    name = models.CharField(
      max_length=4,
      choices=CATEGORY,
      default=CATEGORY[0][0]
    )


    def __str__(self):
      return f'{self.get_category_display()}'
