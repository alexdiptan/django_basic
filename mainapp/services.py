import random

from basketapp.models import Basket
from mainapp.models import Product


def get_basket(user):
    basket_list = []
    if user.is_authenticated:
        # basket_list = sum(list(Basket.objects.filter(user=user).values_list('quantity', flat=True)))
        basket_list = Basket.objects.filter(user=user)

    return basket_list


def get_hot_product():
    # Это вариант будет работать быстрее, так как при получении products_list не происходит получение всех
    # записей из БД. Записи из БД будут подтягиваться в момент вызова return random.sample(list(products_list), 1)[0]
    # Т.е. записи из БД не будут подтягиваться при загрузке приложения.
    # products_list = Product.objects.all()
    # return random.sample(list(products_list), 1)[0]
    return Product.objects.all().order_by('?').first()


def get_same_products(product):
    return Product.objects.filter(category=product.category).exclude(pk=product.pk)[:3]
