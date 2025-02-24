from .models import CartItem

def add_to_cart(user, product, quantity=1):
    """
    Добавляет товар в корзину пользователя.
    Если товар уже есть в корзине, увеличивает количество.
    """
    cart_item, created = CartItem.objects.get_or_create(
        user=user,
        product=product,
        defaults={'quantity': quantity}  # Создаем новую запись, если товара нет в корзине
    )
    if not created:
        # Если товар уже есть, увеличиваем количество
        cart_item.quantity += quantity
        cart_item.save()