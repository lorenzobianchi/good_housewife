from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('spesa/<int:pk>/', views.SpesaDetailView.as_view(), name='spesa_detail'),
    path('spesa/add/', views.SpesaAddView.as_view(), name='spesa_add'),
    path('spesa/<int:pk>/delete', views.SpesaDeleteView.as_view(), name='spesa_delete'),
    path('spesa/<int:pk>/edit', views.SpesaEditView.as_view(), name='spesa_edit'),
    path('spesa-type/', views.TipoSpesaListView.as_view(), name='tipo_spesa_list'),
    path('spesa-type/<int:pk>/', views.TipoSpesaDetailView.as_view(), name='tipo_spesa_detail'),
    path('spesa-type/add/', views.TipoSpesaAddView.as_view(), name='tipo_spesa_add'),
    path('spesa-type/<int:pk>/edit', views.TipoSpesaEditView.as_view(), name='tipo_spesa_edit'),
    path('spesa-type/<int:pk>/delete', views.TipoSpesaDeleteView.as_view(), name='tipo_spesa_delete'),
]
