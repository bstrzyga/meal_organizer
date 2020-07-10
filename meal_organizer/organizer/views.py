from rest_framework import generics
from . import models
from . import serializers


class ProductViewSet(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class IngredientViewSet(generics.ListCreateAPIView):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class MealViewSet(generics.ListCreateAPIView):
    queryset = models.Meal.objects.all()
    serializer_class = serializers.MealSerializer
