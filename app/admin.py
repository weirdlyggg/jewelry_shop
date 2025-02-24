from django.contrib import admin
from .models import Category, Product, Review, ReviewImage, User, Order, OrderItem, CartItem, Favorite, ProductMaterial, Material, ProductGemstone, Gemstone, ProductImage


class ProductInLine(admin.TabularInline):
    model = Product
    extra = 1

class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 1

class ProductMaterialInLine(admin.TabularInline):
    model = ProductMaterial
    extra = 1

class ProductGemstoneInLine(admin.TabularInline):
    model = ProductGemstone
    extra = 1

class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    inlines = [ProductMaterialInLine, ProductGemstoneInLine, ProductImageInLine]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    search_fields = ('product__name', 'user__first_name')

@admin.register(ReviewImage)
class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ('review', 'image_url')
    search_fields = ('review__product__name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'total_price', 'status', 'created_at')
#     list_filter = ('user',)
#     search_fields = ('user__email',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_total_price', 'status', 'created_at')
    list_filter = ('user', 'status')
    search_fields = ('user__email',)

    @admin.display(description='Total Price')
    def get_total_price(self, obj):
        return obj.calculate_total_price()

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product', 'quantity', 'price_at_time_of_purchase')
#     search_fields = ('order__id', 'product__name')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price_at_time_of_purchase')
    list_filter = ('order', 'product')
    search_fields = ('order__id', 'product__name')

# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity')
#     search_fields = ('user__email', 'product__name')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('user', 'product')
    search_fields = ('user__email', 'product__name')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user__email', 'product__name')

@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product', 'material')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ProductGemstone)
class ProductGemstoneAdmin(admin.ModelAdmin):
    list_display = ('product', 'gemstone')

@admin.register(Gemstone)
class GemstoneAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_url')  
    search_fields = ('product__name',)