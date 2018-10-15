from django.urls import path
from . views import (PrestamoListView,
PrestamoDetailView,
PrestamoCreateView,
PrestamoUpdateView,
PrestamoDeleteView,
EmpresaListView,
EmpresaCreateView,
EmpresaUpdateView,
EmpresaDeleteView,
)
from . import views

urlpatterns = [
    path('', PrestamoListView.as_view(), name='leasing-home'),
    path('prestamo/<int:pk>/', PrestamoDetailView.as_view(), name='prestamo-detail'),
    path('prestamo/new/', PrestamoCreateView.as_view(), name='prestamo-create'),
    path('prestamo/<int:pk>/update', PrestamoUpdateView.as_view(), name='prestamo-update'),
    path('prestamo/<int:pk>/delete', PrestamoDeleteView.as_view(), name='prestamo-delete'),

    path('empresa', EmpresaListView.as_view(), name='empresa-home'),
    path('empresa/new/', EmpresaCreateView.as_view(), name='empresa-create'),
    path('empresa/<int:pk>/update', EmpresaUpdateView.as_view(), name='empresa-update'),
    path('empresa/<int:pk>/delete', EmpresaDeleteView.as_view(), name='empresa-delete'),
]