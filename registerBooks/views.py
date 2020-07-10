from django.shortcuts import render, redirect
from .models import register_book
from .forms import book_form
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home_view(request):
    Item_id_lis = register_book.objects.values_list('id', flat=True)
    all_data = []
    for i in Item_id_lis:
        all_prod = register_book.objects.get(id=i)
        data = {
            'obj': all_prod
        }
        if data is not None:
            all_data.append(data)
    return render(request, "homepage.html", {"data": all_data})


def new_book_view(request):
    if request.method == 'POST':
        form = book_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("./")
    else:
        form = book_form()
    return render(request, "new_book.html", {"form": form})
