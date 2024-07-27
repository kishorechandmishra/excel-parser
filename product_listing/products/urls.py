from django.urls import path
from .views import upload_file, product_list, product_list_data

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('products/', product_list, name='product_list'),
    path('products/data/', product_list_data, name='product_list_data'),
]
