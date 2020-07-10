from django.db import models
from django.utils.text import slugify
from . import current_user


class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Meal(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient, related_name='Ingredients')
    added_by = models.ForeignKey('auth.User', default=current_user.get_current_user, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=80)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name} by {self.added_by.name}')
        super(Meal, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} by {self.added_by.name}'

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    """
    #  maybe I should put exporting all ingredients in the meal here?
    def export_ingredients_to_txt(self):
        with open(f'/{self.name}.txt', 'w') as file:
            for ingredient in self.ingredients:
                file.write(f'{ingredient.product} - {ingredient.amount}\\n')
    """

#  TODO right now I can create alot of ingredients, and just only update products...sth weird
