from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .product_views import ProductCRUDView
from .category_views import CategoryCRUDViewMixin
from .country_views import CountryCRUDViewMixin
from . models import Category

# Create your views here.
class CategoryCRUDView(CategoryCRUDViewMixin ,View):    
    def get(self, request):        
        if request.resolver_match.url_name == 'create_category_url':            
            return render(request, 'create_category.html')        
    
    def post(self, request):
        if request.resolver_match.url_name == 'create_category_url':                        
            self.create_category(request=request)
            return redirect('product:category_list_url')


class CategoryListView(View):

    def get(self, request):        
        if request.resolver_match.url_name == 'category_list_url':                            
            categories = Category.objects.all()
            context = {                
                'categories': categories
            }            
            return render(request, 'category_list.html', context)


class CountryCRUDView(CountryCRUDViewMixin, View):

    def get(self, request):        
        if request.resolver_match.url_name == 'create_country_url':
            return render(request, 'country/create_country.html')

    def post(self, request):        
        if request.resolver_match.url_name == 'create_country_url':
            self.create_country(request=request)            
            return redirect('product:country_list_url')

class CreateProductView(ProductCRUDView ,View):
    def get(self, request):
        if request.resolver_match.url_name == 'create_product_url':
            return render(request, 'create_product.html')

        if request.resolver_match.url_name == 'product_list_url':
            return render(request, 'product_list.html')

    def post(self, request):
        if request.resolver_match.url_name == 'create_product_url':
            self.create_product(request=request)            
            return redirect('product:product_list_url')


