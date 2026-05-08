from django.contrib import admin
from .models import Category, MenuItem, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'available']
    list_filter = ['available', 'category']
    search_fields = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'item', 'quantity', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['customer_name']