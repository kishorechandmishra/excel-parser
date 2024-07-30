import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from .models import Product, ProductVariation
from django.http import JsonResponse

# View to handle file upload and parsing
def upload_file(request):
    if request.method == 'POST': # Check if the request method is POST
        form = UploadFileForm(request.POST, request.FILES) # Bind form with POST data and files
        print('reached here')
        if form.is_valid(): # Validate the form
            print('reached here 1')
            file = request.FILES['file'] # Get the uploaded file
            if file.content_type in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
                if file.size <= 2 * 1024 * 1024: # Validate file size (must not exceed 2 MB)
                    try:
                        print('reached here 2')
                        df = pd.read_excel(file) # Parse the Excel file
                        for _, row in df.iterrows(): # Iterate over each row in the Excel file
                            product_name = row['Product Name'] # Get product name from the row
                            variation_text = row['Variation']  # Get variation text from the row
                            stock = row['Stock'] # Get stock value from the row
                            lowest_price=row['Lowest Price'] # Get lowest price from the row
                            print('reached here 30')
                            # Get or create the product, setting the lowest price if the product is created
                            product, created = Product.objects.get_or_create(name=product_name,defaults={'lowest_price': lowest_price})
                            print('reached here 3')
                            if created:
                                product.save() # Save the product if it was newly created
                            if stock is None: # Set stock to 0 if it's None
                                stock = 0 
                            # Get or create the product variation, setting the stock if the variation is created
                            variation, created = ProductVariation.objects.get_or_create(product=product, variation_text=variation_text,defaults={'stock': stock})
                            if not created:
                                variation.stock += stock # Update the stock if variation already exists
                            else:
                                variation.stock = stock # Set the stock if variation is newly created
                            variation.save() # Save the variation
                        messages.success(request, "File uploaded and data updated successfully!") # Add success message
                    except Exception as e:
                        messages.error(request, f"Error processing file: {e}") # Add error message if exception occurs
                else:
                    messages.error(request, "File size exceeds 2 MB") # Add error message if file size exceeds limit
            else:
                messages.error(request, "Invalid file type") # Add error message if file type is invalid
        else:
            messages.error(request, "Invalid form submission") # Add error message if form is invalid
        return redirect('upload_file') # Redirect to the file upload page
    else:
        form = UploadFileForm() # Initialize an empty form
    return render(request, 'upload.html', {'form': form}) 



def product_list(request):
    return render(request, 'product_list.html') # Render the product list template

# View to provide product list data in JSON format
def product_list_data(request):
    products = Product.objects.all() # Retrieve all products
    data = []
    for product in products:
        variations = product.variations.all() # Retrieve all variations for the product
        variations_list = []
        for variation in variations:
            variations_list.append(f"{variation.variation_text} - {variation.stock}") # Create a string representation of the variation
        data.append({
            "id": product.id, # Add product ID
            "name": product.name, # Add product name
            "lowest_price": product.lowest_price, # Add product lowest price
            "variations": ", ".join(variations_list), # Add variations as a comma-separated string
            "last_updated": product.last_updated.strftime("%d %B %Y %I:%M %p") # Add last updated timestamp
        })
    return JsonResponse({"data": data}) # Return the data as JSON

