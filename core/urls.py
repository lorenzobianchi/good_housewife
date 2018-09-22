from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('spesa/<int:pk>/', views.SpesaDetailView.as_view(), name='spesa_detail'),
    path('spesa/add/', views.SpesaAddView.as_view(), name='spesa_add'),
    path('spesa/<int:pk>/delete', views.SpesaDeleteView.as_view(), name='spesa_delete'),
]
