# urls.py
from django.urls import path
from .views import CustomerListView, CustomerUpdateView, ProductListView, OrderListView, OrderUpdateView

urlpatterns = [
    path('api/customers/', CustomerListView.as_view(), name='customer-list-create'),
    path('api/customers/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('api/products/', ProductListView.as_view(), name='product-list-create'),
    path('api/orders/', OrderListView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderUpdateView.as_view(), name='order-retrieve-update'),
]
