from django import forms

# Form for uploading Excel file
class UploadFileForm(forms.Form):
    file = forms.FileField() # File field for the Excel file
