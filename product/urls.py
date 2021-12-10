from django.urls import path
from . import views

app_name='product'
urlpatterns = [

    path('create_category/', views.CategoryCRUDView.as_view(), name='create_category_url'),

    path('category_list/', views.CategoryListView.as_view(), name='category_list_url'),

    path('create-country/', views.CountryCRUDView.as_view(), name='create_country_url'),
    
    path('country-list/', views.CountryCRUDView.as_view(), name='country_list_url'),
    


    path('create_product/', views.CreateProductView.as_view(), name='create_product_url'),
    path('product_list/', views.CreateProductView.as_view(), name='product_list_url')    
]
