from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    
    # Block URLs
    path('blocks/', views.block_list, name='block_list'),
    path('blocks/<int:pk>/', views.block_detail, name='block_detail'),
    path('blocks/create/', views.block_create, name='block_create'),
    path('blocks/<int:pk>/update/', views.block_update, name='block_update'),
    path('blocks/<int:pk>/delete/', views.block_delete, name='block_delete'),
    
    # Apartment URLs
    path('apartments/', views.apartment_list, name='apartment_list'),
    path('apartments/<int:pk>/', views.apartment_detail, name='apartment_detail'),
    path('apartments/create/', views.apartment_create, name='apartment_create'),
    path('apartments/<int:pk>/update/', views.apartment_update, name='apartment_update'),
    path('apartments/<int:pk>/delete/', views.apartment_delete, name='apartment_delete'),
    
    # Dues URLs
    path('dues/', views.dues_list, name='dues_list'),
    path('dues/create/', views.dues_create, name='dues_create'),
    path('dues/<int:pk>/update/', views.dues_update, name='dues_update'),
    path('dues/<int:pk>/delete/', views.dues_delete, name='dues_delete'),
    
    # Expense URLs
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/create/', views.expense_create, name='expense_create'),
    path('expenses/<int:pk>/update/', views.expense_update, name='expense_update'),
    path('expenses/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
] 