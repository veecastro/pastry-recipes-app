from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Pastryrecipe

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
  pastryrecipes = Pastryrecipe.objects.all()
  return render(request, 'recipes/index.html', {
    'pastryrecipes': pastryrecipes
  })

class RecipeCreate(CreateView):
  model = Pastryrecipe
  fields = '__all__'
  template_name = 'main_app/recipe_form.html'
  success_url = '/recipes' 

