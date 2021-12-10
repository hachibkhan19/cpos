from django.views import View
from product.models import Category

class CategoryCRUDViewMixin(View):
    def get_category_value_from_request(self, request):
        context = dict()
        data = request.POST
        context['category_name'] = data.get('category_name')
        return context

    def save_category(self, category_obj, category_name):
        category_obj.category_name = category_name
        category_obj.save()

    def create_category(self, request):
        data_dict = self.get_category_value_from_request(request)    
        category_obj = Category()
        data_dict['category_obj'] = category_obj
        self.save_category(**data_dict)    

