from django.urls import path
from .views import upload_file, product_list, product_list_data

# URL patterns for the products app
urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('products/', product_list, name='product_list'),
    path('products/data/', product_list_data, name='product_list_data'),
]
