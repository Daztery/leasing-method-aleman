from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Prestamo, Empresa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PrestamoListView(LoginRequiredMixin, ListView):
    model = Prestamo
    template_name = 'leasing/home.html'
    context_object_name= 'prestamos'

class PrestamoDetailView(LoginRequiredMixin, DetailView):
    model = Prestamo

class PrestamoCreateView(LoginRequiredMixin, CreateView):
    model = Prestamo
    fields = ['precio_venta', 'cuota_inicial', 'empresa_ofertante', 'empresa_solicitante',
    'tipo_de_pago', 'plazos_de_pago', 'tipo_tasa_interes', 'TEA', 'comision_rt', 'fotocopias',
    'gastos_admin', 'seguro_riesgo', 'seguro_desgravamen', 'plazo_de_gracia', 
    'modelo', 'vehiculo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.TCEA = 21
        form.instance.cuotas = 12
        form.instance.intereses = 21
        form.instance.VAN = 30
        return super().form_valid(form)

class PrestamoUpdateView(LoginRequiredMixin, UpdateView):
    model = Prestamo
    fields = ['precio_venta', 'cuota_inicial', 'empresa_ofertante', 'empresa_solicitante',
    'tipo_de_pago', 'plazos_de_pago', 'tipo_tasa_interes', 'TEA', 'comision_rt', 'fotocopias',
    'gastos_admin', 'seguro_riesgo', 'seguro_desgravamen', 'plazo_de_gracia', 
    'modelo', 'vehiculo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PrestamoDeleteView(LoginRequiredMixin, DeleteView):
    model = Prestamo
    success_url = '/'

# Empresas

class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'leasing/empresa_list.html'
    context_object_name= 'empresas'

class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = ['nombre_empresa', 'razon_social', 'ciudad', 'ruc', 'telefono']

class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = ['nombre_empresa', 'razon_social', 'ciudad', 'ruc', 'telefono']

class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    model = Empresa
    success_url = '/empresa'