from django.contrib import admin
from .models import Product, ProductVariation

# Register the Product model with the admin interface
@admin.register(Product)
class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1

# Register the ProductVariation model with the admin interface
@admin.register(ProductVariation)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'lowest_price', 'last_updated')
    inlines = [ProductVariationInline]

admin.site.register(Product, ProductAdmin)
