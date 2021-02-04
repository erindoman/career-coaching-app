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
    path('clients/<int:client_id>/add_application/', views.add_application, name='add_application'),
    path('skills/', views.SkillList.as_view(), name='skills_index'),
    path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skills_detail'),
    path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
    path('skills/<int:pk>/update', views.SkillUpdate.as_view(), name='skills_update'),
    path('skills/<int:pk>/delete', views.SkillDelete.as_view(), name='skills_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]