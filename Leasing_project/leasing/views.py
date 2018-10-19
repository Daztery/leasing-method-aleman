from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Prestamo, Empresa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PrestamoForm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from django.contrib import messages

class PrestamoListView(LoginRequiredMixin, ListView):
    model = Prestamo
    template_name = 'leasing/home.html'
    context_object_name= 'prestamos'

# EN ESTA FUNCIÓN VA LA LÓGICA DEL LEASING

def prestamo_tabla(request, pk):
    
    tables = [] #Arreglo de diccionarios sobre el cual vamos a iterar

    #Al crear un nuevo leasing nos traerá automáticamente a esta función

    #Variables

    IGV = 0.18

    impuesto_renta = 0.30

    IGV_del_activo = (Prestamo.objects.filter(id=pk).first().precio_venta_del_activo/(1+IGV))*IGV

    valor_de_venta_a = Prestamo.objects.filter(id=pk).first().precio_venta_del_activo - IGV_del_activo

    monto_del_leasing = (valor_de_venta_a +
    Prestamo.objects.filter(id=pk).first().costos_notariales + Prestamo.objects.filter(id=pk).first().costos_registrales +
    Prestamo.objects.filter(id=pk).first().tasacion + Prestamo.objects.filter(id=pk).first().comision_de_estudio +
    Prestamo.objects.filter(id=pk).first().comision_de_activacion)

    TEP = (1 + Prestamo.objects.filter(id=pk).first().TEA/100)**(Prestamo.objects.filter(id=pk).first().frecuencia_de_pago/360) - 1

    numero_cuotas_por_ano = 360/Prestamo.objects.filter(id=pk).first().frecuencia_de_pago

    nCuotas = numero_cuotas_por_ano*Prestamo.objects.filter(id=pk).first().numero_de_años

    """
        Podemos utilizar los datos de entrada de el último objeto creado de Prestamo "Prestamo.objects.filter(id=pk).first().precio_venta", por ejemplo
        con esto calculamos los valores de salida que salen en la tabla de método alemán
    """

    # Llenamos la tabla con las variables calculadas

    for x in range(1, int(nCuotas) + 1):
        campo = {}
        campo["n"] = x
        if x == 1:
            campo["saldo_inicial"] = monto_del_leasing
        else:
            campo["saldo_inicial"] = tables[x-2]["saldo_final"]
        campo["interes"] = (campo["saldo_inicial"]*-1)*TEP
        campo["amortizacion"] = (campo["saldo_inicial"]*-1)/(nCuotas-x+1)
        campo["Cuota"] = campo["interes"] + campo["amortizacion"]
        campo["saldo_final"] = campo["saldo_inicial"] + campo["amortizacion"]

        tables.append(campo)

    #Guardar periodo elegido en formato pdf

    year = Prestamo.objects.filter(id=pk).first().fecha_inicio.year
    month = Prestamo.objects.filter(id=pk).first().fecha_inicio.month
    day = Prestamo.objects.filter(id=pk).first().fecha_inicio.day

    query = request.POST.get("nPeriodo")
    periodoI = request.POST.get("periodoI")
    periodoF = request.POST.get("periodoF")

    numPeriodos = ""
    valor = ""

    if 'buscar' in request.POST or 'filtrar' in request.POST and periodoI != "" and periodoF != "":
        valor = "s"
        iType = "submit"  
    else:
        iType = "hidden"    

    if 'filtrar' in request.POST and periodoI != "" and periodoF != "": #Filtramos entre periodos
        numPeriodos = range(int(periodoI), int(periodoF)+1)
        
    if 'PDF' in request.POST:
        nPeriodoPDF = request.POST.get("nPeriodoPDF")
        periodoIPDF = request.POST.get("periodoIPDF")
        periodoFPDF = request.POST.get("periodoFPDF")

        for x in range(1, int(nCuotas) + 1):
            if nPeriodoPDF is None: continue
            else:
                if tables[x-1]["n"] == int(nPeriodoPDF):
                    iterarPDF(year, month, day, tables, pk, x)
        messages.success(request, f'¡Se ha guardado PDF exitósamente!')

        if periodoIPDF is None and periodoFPDF is None: return
        for x in range(1, int(nCuotas) + 1):  

                if tables[x-1]["n"] >= int(periodoIPDF) and tables[x-1]["n"] <= int(periodoFPDF):
                    iterarPDF(year, month, day, tables, pk, x)

        messages.success(request, f'¡Se ha guardado PDF exitósamente!')

    context = {
        'tables': tables,
        'pk': pk,
        'query': query,
        'valor': valor,
        'iType': iType,
        'numPeriodos': numPeriodos,
        'periodoI': periodoI,
        'periodoF': periodoF
    }

    return render(request, 'leasing/prestamo_tabla.html', context)

    #Puede ser beno crear una tabla para guardar estos resultados, puesto que solo se generan al momento de crear un nuevo leasing y no son persistentes.

def iterarPDF(year, month, day, tables, pk, x):
    c = canvas.Canvas("LAP-Sol-" + str(Prestamo.objects.filter(id=pk).first().id) + " " + str(Prestamo.objects.filter(id=pk).first().empresa_solicitante.razon_social) + "-Periodo-" +  str(x) + "-" +
    str(year) + "-" + str(month) + "-" + str(day) + ".pdf", pagesize=landscape(letter))
    c.setFont('Helvetica', 48, leading=None)
    c.drawCentredString(415, 500, "Empresa: " + str(Prestamo.objects.filter(id=pk).first().empresa_solicitante.razon_social))
    c.setFont('Helvetica', 20, leading=None)
    c.drawString(100, 400, "Periodo: " + str(tables[x-1]["n"]))
    c.drawString(100, 350, "Saldo inicial: " + str(tables[x-1]["saldo_inicial"]))
    c.drawString(100, 300, "Interés: " + str(tables[x-1]["interes"]))
    c.drawString(100, 250, "Amortización: " + str(tables[x-1]["amortizacion"]))
    c.drawString(100, 200, "Cuota: " + str(tables[x-1]["Cuota"]))
    c.drawString(100, 150, "Saldo final: " + str(tables[x-1]["saldo_final"]))
    c.save()

class PrestamoDetailView(LoginRequiredMixin, DetailView):
    model = Prestamo

class PrestamoCreateView(LoginRequiredMixin, CreateView):
    model = Prestamo
    form_class = PrestamoForm

    def form_valid(self, form):
        form.instance.author = self.request.user
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