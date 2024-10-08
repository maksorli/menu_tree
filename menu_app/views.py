 
from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def home(request):
    return render(request, 'menu_app/home.html')
def punkt1_view(request):
    return render(request, 'menu_app/punkt1.html')
def punkt2_view(request):
    return render(request, 'menu_app/punkt2.html')
def menu_item_view(request, slug):
    menu_item = get_object_or_404(MenuItem, slug=slug)
    context = {
        'menu_item': menu_item,
    }
    return render(request, 'menu_app/menu_item_page.html', context)
