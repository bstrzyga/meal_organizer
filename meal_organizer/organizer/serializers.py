from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ('product', 'amount')


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meal
        fields = ('name', 'ingredients', 'added_by')
