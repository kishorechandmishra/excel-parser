from django.apps import AppConfig

# Define the ProductsConfig class for the products app
class ProductsConfig(AppConfig):
    # Set the default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # Specify the name of the app
    name = 'products'
