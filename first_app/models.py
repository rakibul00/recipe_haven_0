# models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes", default=1)  # Set the default category ID
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to='recipe_images/')

    def __str__(self):
        return self.title



