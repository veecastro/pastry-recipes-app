from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pastryrecipe, Photo


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
# still tryingto figure out how to add a photo to a recipe using aws  
def add_photo(request, recipe_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, recipe_id=recipe_id)
    except:
      print('An error occurred uploading file to S3')
  return redirect('details', recipe_id=recipe_id)

class RecipeCreate(CreateView):
  model = Pastryrecipe
  fields = '__all__'
  template_name = 'main_app/recipe_form.html'
  success_url = '/recipes/' 

def form_valid(self, form):
   form.instance.photo = self.request.FILES.get('photo')
   return super(RecipeCreate, self).form_valid(form)
# still trying to figure out the code btwn comments

class RecipeUpdate(UpdateView):
  model = Pastryrecipe
  template_name = 'main_app/recipe_form.html'
  fields = '__all__'

class RecipeDelete(DeleteView):
  model = Pastryrecipe
  success_url = '/recipes/'
  template_name = 'main_app/recipe_confirm_delete.html'
