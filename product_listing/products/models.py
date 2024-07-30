from django.db import models

# Product model to store basic product details
class Product(models.Model):
    name = models.CharField(max_length=255) # Product name
    lowest_price = models.DecimalField(max_digits=10, decimal_places=2) # Lowest price of the product
    last_updated = models.DateTimeField(auto_now=True) # Timestamp for last update

    def __str__(self):
        return self.name

# ProductVariation model to store variations of a product
class ProductVariation(models.Model): 
    product = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE) # Foreign key to Product
    variation_text = models.CharField(max_length=255) # Description of the variation
    stock = models.IntegerField() # Stock quantity
    last_updated = models.DateTimeField(auto_now=True) # Timestamp for last update

    def __str__(self):
        return f'{self.variation_text} ({self.product.name})'
