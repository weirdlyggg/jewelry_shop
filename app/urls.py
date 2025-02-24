from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    # Другие маршруты...
]