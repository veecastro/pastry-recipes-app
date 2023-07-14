from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),

   path('recipes/', views.recipes_index, name='index'),
   path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),

 ]