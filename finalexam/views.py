from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Product, Like, Comment, Cart, CartItem, Order, OrderItem
from .serializers import (
    CategorySerializer, ProductSerializer, CommentSerializer,
    CartSerializer, CartItemSerializer, OrderSerializer
)


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LikeToggleView(APIView):


    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, product=product)
        if not created:
            like.delete()
            return Response({'liked': False})
        return Response({'liked': True})


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs['pk']
        product = get_object_or_404(Product, pk=product_id)
        serializer.save(user=self.request.user, product=product)

class CartItemAddView(APIView):

    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        item.quantity = quantity
        item.save()
        return Response({'status': 'added'})

class OrderCreateView(APIView):

    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        order = Order.objects.create(user=request.user)
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.items.all().delete()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
