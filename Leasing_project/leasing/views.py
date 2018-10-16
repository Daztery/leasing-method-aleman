from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Prestamo, Empresa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PrestamoForm

class PrestamoListView(LoginRequiredMixin, ListView):
    model = Prestamo
    template_name = 'leasing/home.html'
    context_object_name= 'prestamos'

# EN ESTA FUNCIÓN VA LA LÓGICA DEL LEASING
def prestamo_tabla(request):
    
    tables = [] #Arreglo de diccionarios sobre el cual vamos a iterar

    #Al crear un nuevo leasing nos traerá automáticamente a esta función

    #Ejemplo de como tomar los atributos de los valores de entrada del leasing

    n = 12 #numero de meses por ejemplo de los plazos

    """
        Podemos utilizar los datos de entrada de el último objeto creado de Prestamo "Prestamo.objects.last().precio_venta", por ejemplo
        con esto calculamos los valores de salida que salen en la tabla de método alemán
    """

    for x in range(1, n + 1):
        campo = {}
        campo["n"] = x
        campo["PG"] = Prestamo.objects.last().precio_venta
        campo["saldo_inicial"] = Prestamo.objects.last().cuota_inicial
        campo["interes"] = Prestamo.objects.last().empresa_ofertante
        campo["Cuota"] = Prestamo.objects.last().empresa_solicitante
        campo["amortizacion"] = Prestamo.objects.last().tipo_de_pago
        campo["seguroR"] = Prestamo.objects.last().plazos_de_pago
        campo["comision"] = Prestamo.objects.last().tipo_tasa_interes
        campo["recompra"] = Prestamo.objects.last().TEA
        campo["saldo_final"] = Prestamo.objects.last().comision_rt
        campo["depreciacion"] = Prestamo.objects.last().fotocopias
        campo["ahorroTr"] = Prestamo.objects.last().gastos_admin
        campo["IGV"] = Prestamo.objects.last().fecha_inicio
        campo["flujo_bruto"] = Prestamo.objects.last().seguro_riesgo
        campo["flujo_con_igv"] = Prestamo.objects.last().seguro_desgravamen
        campo["flujo_neto"] = Prestamo.objects.last().plazo_de_gracia

        tables.append(campo)

    context = {
        'tables': tables
    }

    return render(request, 'leasing/prestamo_tabla.html', context)

    #Puede ser bueno crear una tabla para guardar estos resultados, puesto que solo se generan al momento de crear un nuevo leasing y no son persistentes.

class PrestamoDetailView(LoginRequiredMixin, DetailView):
    model = Prestamo

class PrestamoCreateView(LoginRequiredMixin, CreateView):
    model = Prestamo
    form_class = PrestamoForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.TCEA = form.instance.plazos_de_pago*12

        return super().form_valid(form)

class PrestamoUpdateView(LoginRequiredMixin, UpdateView):
    model = Prestamo
    form_class = PrestamoForm

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