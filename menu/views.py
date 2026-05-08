from rest_framework import generics
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer


class MenuListView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(available=True)
    serializer_class = MenuItemSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer