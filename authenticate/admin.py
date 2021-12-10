from django.contrib import admin
from django.apps import apps

# Register your models here.
depot_app_config = apps.get_app_config('authenticate')
for model in depot_app_config.get_models():
    admin.site.register(model)
