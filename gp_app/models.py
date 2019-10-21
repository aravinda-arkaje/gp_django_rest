from django.db import models
# Inbulit user model inporting
from django.contrib.auth.models import User

# Create your models here.

# 1. Design the User Model with username(unique field), email(unique field), first_name,
# last_name,m password. (You can use the django inbuilt user model)
# 2. Design A Step Model with step_text(string field, not null), Many to One relationship with
# Recipe
# 3. Design An Ingredient Model with text(not null, string), Many to One relationship with
# Recipe
# 4. Design A Recipe Model with name(string, not null), Foreign Key to User table(one to one
# relationship), One to Many relationship with Step and Ingredient Model

# one to one relationship with User.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Recipe')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# Many to One relationship with Recipe.
class Step(models.Model):
    step_text = models.TextField(null=False)
    recipe_step = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='Recipe_Step')

# Many to One relationship with Recipe.
class Ingredient(models.Model):
    text = models.TextField()
    recipe_ingredient = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='Recipe_Ingredient')
