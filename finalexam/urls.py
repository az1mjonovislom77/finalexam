from django.urls import path
from .views import (
    CategoryCreateView, CategoryDeleteView,
    ProductCreateView, ProductDeleteView,
    LikeToggleView,
    CommentCreateView,
    CartItemAddView,
    OrderCreateView,
)

urlpatterns = [
    # Category
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    # Product
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # Like
    path('products/<int:pk>/like-toggle/', LikeToggleView.as_view(), name='like_toggle'),

    # Comment
    path('products/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment_create'),

    # Cart
    path('cart/items/add/', CartItemAddView.as_view(), name='cartitem_add'),

    # Order
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
]
