from rest_framework import serializers
from .models import User, Step, Ingredient, Recipe

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

class ListRecipeSerializer(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()
    ingredient = serializers.SerializerMethodField()

    def get_step(self, obj):
        step = obj.Recipe_Step
        serializer = StepSerializer(step, many=True).data
        return serializer

    def get_ingredient(self, obj):
        ingredient = obj.Recipe_Ingredient
        serializer = IngredientSerializer(ingredient, many=True).data
        return serializer

    class Meta:
        model = Recipe
        fields = "__all__"
