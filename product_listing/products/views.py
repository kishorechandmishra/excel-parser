import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from .models import Product, ProductVariation
from django.http import JsonResponse
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print('reached here')
        if form.is_valid():
            print('reached here 1')
            file = request.FILES['file']
            if file.content_type in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
                if file.size <= 2 * 1024 * 1024:
                    try:
                        print('reached here 2')
                        df = pd.read_excel(file)
                        for _, row in df.iterrows():
                            product_name = row['Product Name']
                            variation_text = row['Variation']
                            stock = row['Stock']
                            lowest_price=row['Lowest Price']
                            print('reached here 30')
                            product, created = Product.objects.get_or_create(name=product_name,defaults={'lowest_price': lowest_price})
                            print('reached here 3')
                            if created:
                                product.save()
                            if stock is None:
                                stock = 0 
                            variation, created = ProductVariation.objects.get_or_create(product=product, variation_text=variation_text,defaults={'stock': stock})
                            if not created:
                                variation.stock += stock
                            else:
                                variation.stock = stock
                            variation.save()
                        messages.success(request, "File uploaded and data updated successfully!")
                    except Exception as e:
                        messages.error(request, f"Error processing file: {e}")
                else:
                    messages.error(request, "File size exceeds 2 MB")
            else:
                messages.error(request, "Invalid file type")
        else:
            messages.error(request, "Invalid form submission")
        return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})



def product_list(request):
    return render(request, 'product_list.html')

def product_list_data(request):
    products = Product.objects.all()
    data = []
    for product in products:
        variations = product.variations.all()
        variations_list = []
        for variation in variations:
            variations_list.append(f"{variation.variation_text} - {variation.stock}")
        data.append({
            "id": product.id,
            "name": product.name,
            "lowest_price": product.lowest_price,
            "variations": ", ".join(variations_list),
            "last_updated": product.last_updated.strftime("%d %B %Y %I:%M %p")
        })
    return JsonResponse({"data": data})

