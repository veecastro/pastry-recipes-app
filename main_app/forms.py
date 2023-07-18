from django.forms import ModelForm
from .models import Pastryrecipe, Category
from django import forms

CATEGORY = (
   ('CC', 'Cakes and Cupcakes'),
   ('PT', 'Pies and Tarts'),
   ('CB', 'Cookies and Bisquits'),
   ('PP', 'Pastries and Puff Pastry'),
   ('FD', 'Frozen Desserts'),
   ('PC', 'Puddings and Custards'),
   ('FR', 'Fruit-based Desserts'),
   ('ID', 'International Desserts'),
   ('OT', 'Other Desserts'),
)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Pastryrecipe
        fields = ('title','category', 'preptime', 'cookingtime', 'totaltime', 'yields', 'ingredients', 'instructions', 'categories')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=CATEGORY, attrs={'class': 'form-control'}),
            'preptime': forms.NumberInput(attrs={'class': 'form-control'}),
            'cookingtime': forms.NumberInput(attrs={'class': 'form-control'}),
            'totaltime': forms.NumberInput(attrs={'class': 'form-control'}),
            'yields': forms.NumberInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),
        }