from django.shortcuts import get_object_or_404, redirect
from .models import Product
from .services import add_to_cart

def add_to_cart_view(request, product_id):
    """
    View для добавления товара в корзину.
    """
    product = get_object_or_404(Product, id=product_id)
    user = request.user  # Предполагается, что пользователь авторизован
    quantity = int(request.POST.get('quantity', 1))  # Получаем количество из POST-запроса

    # Добавляем товар в корзину через сервисный слой
    add_to_cart(user=user, product=product, quantity=quantity)

    return redirect('cart_view')  # Перенаправляем на страницу корзины