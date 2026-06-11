from django.contrib import admin
from .models import ContactMessage, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'rating', 'in_stock')
    list_filter = ('category', 'in_stock')
    search_fields = ('name', 'short_description')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'topic', 'created_at')
    search_fields = ('name', 'email', 'topic')
    readonly_fields = ('created_at',)
