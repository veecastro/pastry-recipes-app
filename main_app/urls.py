from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes_index, name='index'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('about/', views.about, name='about'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),
]
