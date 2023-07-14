from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Pastryrecipe

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def recipes_index(request):
  pastryrecipes = Pastryrecipe.objects.all()
  return render(request, 'recipes/index.html', {
    'pastryrecipes': pastryrecipes
  })

class RecipeCreate(CreateView):
  model = Pastryrecipe
  fields = '__all__'
  success_url = '/recipes' 

