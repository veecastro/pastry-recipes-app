import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pastryrecipe, Photo



def home(request):
  # return render(request, 'home.html')
  pastryrecipes = Pastryrecipe.objects.all()
  return render(request, 'recipes/index.html', {
    'pastryrecipes': pastryrecipes
  })

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
  pastryrecipes = Pastryrecipe.objects.all()
  return render(request, 'recipes/index.html', {
    'pastryrecipes': pastryrecipes
  })

def recipes_detail(request, recipe_id):
  recipe = Pastryrecipe.objects.get(id=recipe_id)
  photos = recipe.photo_set.all()
  # photos = Photo.objects.filter(recipe_id=recipe_id)
  return render(request, 'recipes/detail.html', {
    'recipe': recipe,
    'photos': photos,
   })

def add_photo(request, pastryrecipe_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, recipe_id=pastryrecipe_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', recipe_id=pastryrecipe_id)

def delete_photo(request, photo_id):
  photo = Photo.objects.get(id=photo_id)
  recipe_id = photo.recipe_id
  photo.delete()
  return redirect('detail', recipe_id=recipe_id)


class RecipeCreate(CreateView):
  model = Pastryrecipe
  fields = '__all__'
  template_name = 'main_app/recipe_form.html'
  success_url = '/recipes/'

def form_valid(self, form):
  form.instance.photo = self.request.FILES.get('photo')
  return super(RecipeCreate, self).form_valid(form)


class RecipeUpdate(UpdateView):
  model = Pastryrecipe
  template_name = 'main_app/recipe_form.html'
  fields = '__all__'

class RecipeDelete(DeleteView):
  model = Pastryrecipe
  success_url = '/recipes/'
  template_name = 'main_app/recipe_confirm_delete.html'

def search_recipe(request):
  if request.method == 'POST':
    searched = request.POST['searched']
    recipes = Pastryrecipe.objects.filter(title__contains=searched)
    return render(request, 'search_recipe.html', {'searched': searched, 'recipes': recipes})
  else:
    return render(request, 'search_recipe.html', {})
  


