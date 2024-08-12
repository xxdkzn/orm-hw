from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Phone


class CatalogView(View):
    def get(self, request):
        sort_option = request.GET.get('sort', 'name')
        if sort_option == 'min_price':
            phones = Phone.objects.all().order_by('price')
        elif sort_option == 'max_price':
            phones = Phone.objects.all().order_by('-price')
        else:
            phones = Phone.objects.all().order_by('name')
        return render(request, 'catalog.html', {'phones': phones})

class PhoneDetailView(View):
    def get(self, request, slug):
        phone = get_object_or_404(Phone, slug=slug)
        return render(request, 'phone_detail.html', {'phone': phone})