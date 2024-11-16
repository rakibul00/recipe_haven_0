# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeSearchForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login,logout


def base(request):
    return render(request,'home.html')




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username =name,password=userpass)
            if user is not None:
                login(request,user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'from':form})





def user_singup(request):
    if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           print(form.changed_data)
           return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'singup.html', {'from':form})



def user_logout(request):
    logout(request)
    return redirect('login')




def user_profile(request):
   

    return render(request, 'user_profile.html')



def pp(request):
      recipes = Recipe.objects.all()
      return render(request, 'pp.html', {'recipes': recipes})
  
  

def submit_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('menu')  # or the name of your recipes list page
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})



def menu(request):
    form = RecipeSearchForm(request.GET or None)
    recipes = Recipe.objects.all()

    if form.is_valid():
        category = form.cleaned_data.get('category')
        ingredient = form.cleaned_data.get('ingredient')
        search_query = form.cleaned_data.get('search_query')

        if category:
            recipes = recipes.filter(category=category)
        if ingredient:
            recipes = recipes.filter(ingredients=ingredient)
        if search_query:
            recipes = recipes.filter(title__icontains=search_query)

    return render(request, 'menu.html', {'recipes': recipes, 'form': form})
    

def details(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
   
    return render(request, 'recipe_datelis.html', {'recipe':recipe})




def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)  # Ensure the user owns the recipe
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form})
