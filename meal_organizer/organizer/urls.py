from django.urls import path
from . import views

urlpatterns = [
    path('product', views.ProductViewSet.as_view()),
    path('ingredient', views.IngredientViewSet.as_view()),
    path('meal', views.MealViewSet.as_view()),
]
