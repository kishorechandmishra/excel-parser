# excel-parser
# Product Listing Application

## Introduction
This project is a Django application for managing product listings. It includes features such as:
- Uploading product data via an Excel file
- Displaying a list of products with variations, stock, and last updated information
- Adding products through an admin interface with search, sorting, and pagination functionalities

## Features
- **Excel File Upload**: Upload product data using `.xls` or `.xlsx` files.
- **Product List**: View a list of products with their variations and stock details.
- **Admin Interface**: Manage products and variations through an intuitive admin panel.
- **DataTable**: Display products in a searchable, sortable, and paginated table.

## Technologies Used
- Python 3.x
- Django
- Pandas
- HTML/CSS
- JavaScript (for DataTables)

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/product-listing-app.git
    cd product-listing-app
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (for admin access):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

### Usage

1. **Access the admin panel:**
    - Open your browser and go to `http://127.0.0.1:8000/admin/`
    - Log in with the superuser credentials you created earlier

2. **Upload products via Excel file:**
    - Go to the upload page (e.g., `http://127.0.0.1:8000/upload/`)
    - Upload a valid `.xls` or `.xlsx` file

3. **View the product list:**
    - Go to the product list page (e.g., `http://127.0.0.1:8000/products/`)
    - Search, sort, and paginate through the products

### Directory Structure
```plaintext
product-listing-app/
│
├── products/
│   ├── migrations/
│   ├── templates/
│   │   ├── upload.html
│   │   ├── product_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│
├── product_listing/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md

Models

Product

ID: Primary key
Name: Name of the product
Lowest Price: Lowest price of the product
Last Updated: Timestamp of the last update

ProductVariation

ID: Primary key
Product: Foreign key to the Product model
Variation Text: Description of the variation (e.g., color, size)
Stock: Number of items in stock
Last Updated: Timestamp of the last update

Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

