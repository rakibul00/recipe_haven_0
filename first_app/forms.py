# forms.py

from django import forms
from .models import Category, Ingredient

class RecipeSearchForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(), required=False)
    search_query = forms.CharField(max_length=100, required=False, label="Search Recipe by Name")

# forms.py

from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'instructions', 'category', 'ingredients', 'image']


# users/forms.py


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
       
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional customizations, if needed
        


