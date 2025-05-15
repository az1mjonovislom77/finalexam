from django.urls import path
from .views import (
    RegisterView, ProfileView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    LikeToggleView, CommentCreateView, CommentUpdateView,
    CartItemAddView, CartItemUpdateView,
    OrderCreateView, OrderListView,
)

urlpatterns = [
    # User 
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/profile/', ProfileView.as_view(), name='profile'),

    # Categories
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # Products 
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Likes
    path('products/<int:pk>/like-toggle/', LikeToggleView.as_view(), name='like-toggle'),

    # Comments
    path('products/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),

    # Cart
    path('cart/items/add/', CartItemAddView.as_view(), name='cart-item-add'),
    path('cart/items/<int:pk>/update/', CartItemUpdateView.as_view(), name='cart-item-update'),

    # Orders
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]
