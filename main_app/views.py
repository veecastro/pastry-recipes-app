from django.shortcuts import render
from django.views.generic.edit import CreateView
# from.django.views.generic import ListView
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
 pastryrecipe = Pastryrecipe.objects.get(id=recipe_id)
 return render(request, 'recipes/detail.html', {
   'pastryrecipe': pastryrecipe
 })

# class RecipeList(ListView):
#   model = Pastryrecipe
#   template_name = 'recipes/index.html'
#   # context_object_name = 'pastryrecipes'

class RecipeCreate(CreateView):
  model = Pastryrecipe
  fields = '__all__'
  template_name = 'main_app/recipe_form.html'
  success_url = '/recipes' 

