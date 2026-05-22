from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.ProductSearchView.as_view(), name='search'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product')
]