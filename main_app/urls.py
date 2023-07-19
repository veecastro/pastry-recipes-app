from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes_index, name='index'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('about/', views.about, name='about'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('recipes/<int:pastryrecipe_id>/add_photo/', views.add_photo, name='add_photo'),
    path('photos/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('search_recipe/', views.search_recipe, name='search'),
]


