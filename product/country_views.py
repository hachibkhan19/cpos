from django.db import models
from django.views import View
from .models import Country

class CountryCRUDViewMixin(View):
    def get_country_value_from_request(self, request):
        context = dict()
        data = request.POST
        context['country_name'] = data.get('country_name')
        return context

    def save_country(self, country_obj, country_name):
        country_obj.country_name = country_name
        country_obj.save()   
    
    def create_country(self, request):
        data_dict = self.get_country_value_from_request(request)
        country_obj = Country()
        data_dict['country_obj'] = country_obj
        self.save_country(**data_dict)
        