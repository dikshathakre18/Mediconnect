from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donor/dashboard/', views.donor_dashboard, name='donor_dashboard'),
    path('requester/dashboard/', views.requester_dashboard, name='requester_dashboard'),
    path('select-request/', views.select_request, name='select_request'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('create-request/', views.create_request, name='create_request'),
    path('update-request/<int:id>/<str:status>/', views.update_request, name='update_request'),
    path('about/', views.about, name='about'),
]


