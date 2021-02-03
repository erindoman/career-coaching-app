from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('clients/', views.clients_index, name='index'),
    path('clients/<int:client_id>/', views.clients_detail, name='detail'),
    path('clients/create/', views.ClientCreate.as_view(), name='client_create'),
    path('clients/<int:pk>/update', views.ClientUpdate.as_view(), name='clients_update'),
    path('clients/<int:pk>/delete/', views.ClientDelete.as_view(), name='clients_delete'),

    path('accounts/signup/', views.signup, name='signup'),
]