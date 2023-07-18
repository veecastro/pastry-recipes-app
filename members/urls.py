from django.urls import path
from .views import UserRView

urlpatterns = [
    path('register/', UserRView.as_view(), name='register'),
    
]