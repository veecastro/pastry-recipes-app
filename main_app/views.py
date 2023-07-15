from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pastryrecipe


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
  pastryrecipes = Pastryrecipe.objects.all()
  return render(request, 'recipes/index.html', {
    'pastryrecipes': pastryrecipes
  })

def recipes_detail(request, recipe_id):
  recipe = Pastryrecipe.objects.get(id=recipe_id)
  return render(request, 'recipes/detail.html', {
    'recipe': recipe
  })

class RecipeCreate(CreateView):
  model = Pastryrecipe
  fields = '__all__'
  template_name = 'main_app/recipe_form.html'
  success_url = '/recipes/' 

class RecipeUpdate(UpdateView):
  model = Pastryrecipe
  template_name = 'main_app/recipe_form.html'
  fields = '__all__'

class RecipeDelete(DeleteView):
  model = Pastryrecipe
  success_url = '/recipes/'
  template_name = 'main_app/recipe_confirm_delete.html'
