from django.urls import path
from . import views

app_name = 'products'  # las direciones pertenecen a esta app

urlpatterns = [
    path('search/', views.ProductSearchView.as_view(), name='search'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product')
]