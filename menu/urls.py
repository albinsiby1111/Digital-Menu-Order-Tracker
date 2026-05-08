from django.urls import path
from .views import MenuListView, OrderCreateView

urlpatterns = [
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
]