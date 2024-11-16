from django.urls import path
from . import views

urlpatterns = [
    path('',views.base, name='base'),
    path('singup/',views.user_singup,name='singup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
  
  
    path('submit-recipe/', views.submit_recipe, name='submit_recipe'),


    path('pp/',views.pp,name='profile'),
    path('menu/',views.menu,name='menu'),
    path('profile/',views.user_profile,name='user_profile'),
    path('menu/<int:recipe_id>',views.details, name='details'),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),


    
   
    
]
