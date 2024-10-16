from django.urls import path
from . import views
from  .views import  logout_view

urlpatterns = [
    path('', views.index, name='inicio'),
    path('donaciones/', views.donate, name='donaciones'),
    path('donation-success/', views.donation_success, name='donation_success'),
    path('login/', views.login_view, name='login'),  # Usa solo esta línea
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload_project/', views.upload_project, name='upload_project'),
    path('logout/', logout_view, name='logout'),
    path('manage_projects/', views.manage_projects, name='manage_projects'),
]
