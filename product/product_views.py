from django.db import models
from django.views import View
from product.models import Product

class ProductCRUDView(View):
    def get_product_value_from_request(self, request):
        context = dict()
        data = request.POST
        context['product_name'] = data.get('product_name')
        context['product_code'] = data.get('product_code')
        context['product_purchase_price'] = data.get('product_purchase_price')
        context['product_selling_price'] = data.get('product_selling_price')

        print(context, '----------context data---------')

        return context


    def save_product(self, product_obj, product_name, product_code, product_purchase_price, product_selling_price):
        product_obj.product_name = product_name
        product_obj.product_code = product_code
        product_obj.product_purchase_price = product_purchase_price
        product_obj.product_selling_price = product_selling_price

        product_obj.save()


    def create_product(self, request):
        data_dict = self.get_product_value_from_request(request)
        product_obj = Product()
        data_dict['product_obj'] = product_obj
        self.save_product(**data_dict)
