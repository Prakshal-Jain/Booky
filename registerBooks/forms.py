from .models import register_book
from django import forms


class book_form(forms.ModelForm):
    class Meta:
        model = register_book
        widgets = {
            'Book_Name': forms.TextInput(attrs={'placeholder': 'Enter Book Name'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter product description and condition'}),
            "author": forms.TextInput(attrs={'placeholder': 'Enter Author(s) name'}),
            "date": forms.DateTimeInput(attrs={'placeholder': 'Enter Date'}),
            "location": forms.TextInput(attrs={'placeholder': 'Enter your location'}),
            "price": forms.NumberInput(attrs={'placeholder': 'Enter price'}),
        }
        
        fields = [
            "Book_Name",
            "author",
            "book_image",
            "date",
            "location",
            "description",
            "price",
        ]
