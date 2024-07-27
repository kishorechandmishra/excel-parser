from django.contrib import admin
from .models import Product, ProductVariation

class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'lowest_price', 'last_updated')
    inlines = [ProductVariationInline]

admin.site.register(Product, ProductAdmin)
