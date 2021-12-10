from django.urls import path
from . import views

app_name='authenticate'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_url'),
    path('register/', views.RegisterView.as_view(), name='register_url'),    
    path('login/', views.LoginView.as_view(), name='login_url'),    
    path('logout/', views.LogoutView.as_view(), name='logout_url'),    
]
