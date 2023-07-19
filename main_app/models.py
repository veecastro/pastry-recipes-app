from django.db import models
from django.urls import reverse

# Create your models here.

CATEGORY_CHOICES = (
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
    title = models.CharField(max_length=100, verbose_name="Title")
    preptime = models.IntegerField(verbose_name="Prep Time")
    cookingtime = models.IntegerField(verbose_name="Cooking Time")
    totaltime = models.IntegerField(verbose_name="Total Time")
    yields = models.IntegerField(verbose_name="Yields")
    ingredients = models.TextField(verbose_name="Ingredients")
    instructions = models.TextField(verbose_name="Instructions")
    # categorytype = models.CharField('Category', max_length=2, choices=CATEGORY_CHOICES)

        
    def __str__(self):
      return f'{self.title} ({self.id})'

    def get_absolute_url(self):
      return reverse('detail', kwargs={'recipe_id': self.id})
    
class Photo(models.Model):
    url = models.ImageField(upload_to='recipes/', default="No Image")
    recipe = models.ForeignKey(Pastryrecipe, on_delete=models.CASCADE)

    def __str__(self):
      return f"Photo for recipe_id: {self.recipe_id} @ {self.url}"
    
class Category(models.Model):
    recipes = models.ForeignKey(Pastryrecipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=4)

    def __str__(self):
      return f"{self.get_name_display()}"
    
    def get_absolute_url(self):
      return reverse('categories_detail', kwargs={'pk': self.id})