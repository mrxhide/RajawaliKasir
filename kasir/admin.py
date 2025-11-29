from django.contrib import admin
from .models import Category, Product, Sale, SaleItem, StockMovement


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'unit', 'sell_price', 'stock', 'min_stock', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'barcode', 'sku')


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 0


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'date_time', 'cashier', 'total', 'payment_method')
    list_filter = ('date_time', 'payment_method', 'cashier')
    search_fields = ('invoice_no', 'customer_name')
    inlines = [SaleItemInline]


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity', 'created_at', 'user')
    list_filter = ('movement_type', 'created_at')
    search_fields = ('product__name',)
