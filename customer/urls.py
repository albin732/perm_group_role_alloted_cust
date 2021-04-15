from django.urls import path
from customer.view.customer import Customer_CreateView, Customer_DeleteView, Customer_DetailView, Customer_ListView, Customer_UpdateView

urlpatterns = [
    path('customer_add/', Customer_CreateView.as_view(),
         name='customer_add'),
    path('customer_list/', Customer_ListView.as_view(),
         name='customer_list'),
    path('customer_detail/<int:pk>/', Customer_DetailView.as_view(),
         name='customer_detail'),
    path('customer_edit/<int:pk>/', Customer_UpdateView.as_view(),
         name='customer_edit'),
    path('customer_delete/<int:pk>/', Customer_DeleteView.as_view(),
         name='customer_delete'),
]
