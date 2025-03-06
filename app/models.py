from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.first_name}"


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return f"Image for review {self.review.id}"


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    address = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email




class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total_price(self):
        return sum(item.price_at_time_of_purchase * item.quantity for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} by {self.user.first_name}"




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_time_of_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.price_at_time_of_purchase:
            self.price_at_time_of_purchase = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"




class CartItem(models.Model):
    user = models.ForeignKey(User, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} favorited by {self.user.first_name}"


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, related_name='materials', on_delete=models.CASCADE)
    material = models.ForeignKey('Material', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} made of {self.material.name}"


class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductGemstone(models.Model):
    product = models.ForeignKey(Product, related_name='gemstones', on_delete=models.CASCADE)
    gemstone = models.ForeignKey('Gemstone', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} with {self.gemstone.name}"


class Gemstone(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')  # Поле для загрузки изображений
    alt_text = models.CharField(max_length=255, blank=True, null=True)  # Опциональное описание

    def __str__(self):
        return f"Image for {self.product.name}"
