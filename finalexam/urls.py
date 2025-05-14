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
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),

    # Product
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),

    # Like
    path('products/<int:pk>/like-toggle/', LikeToggleView.as_view(), name='like-toggle'),

    # Comment
    path('products/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment-create'),

    # Cart
    path('cart/items/add/', CartItemAddView.as_view(), name='cartitem-add'),

    # Order
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
]
