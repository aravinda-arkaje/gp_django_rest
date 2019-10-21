from django.shortcuts import render

from .models import Recipe, Step, Ingredient
from .serializers import RecipeSerializer,ListRecipeSerializer
from rest_framework.generics import ListAPIView ,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# To get all the recipes.
class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = ListRecipeSerializer

# To get recipes by particular user.
class RecipeView(ListAPIView):
    def get_queryset(self):
        queryset = Recipe.objects.filter(user=self.request.user)
        return queryset
    serializer_class = RecipeSerializer

# To create a new recipe.
class RecipeCreateView(CreateAPIView):
     queryset = ""
     serializer_class = RecipeSerializer

     def create(self, request, *args, **kwargs):
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save(user=request.user)
         return Response(serializer.data, status=status.HTTP_201_CREATED)

# To update a recipe and delete a particular recipe.
class RecipeRetrieveUpdatdDestroy(RetrieveUpdateDestroyAPIView):
     queryset = Recipe.objects.all()
     serializer_class = RecipeSerializer
