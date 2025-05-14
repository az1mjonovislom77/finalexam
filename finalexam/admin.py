from django.contrib import admin
from .models import User, Category, Product, ProductImage, Like, Comment, Cart, CartItem, Order, OrderItem

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'created_at', 'updated_at', 'slug')  # slug va updated_at qo'shildi
    prepopulated_fields = {'slug': ('name',)}  # Slugni avtomatik to'ldirish
    inlines = [ProductImageInline]  # ProductImage Inline qo'shildi

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'pros', 'cons', 'review', 'created_at')  # created_at qo'shildi
    list_filter = ('product', 'user', 'created_at')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Like, LikeAdmin)
