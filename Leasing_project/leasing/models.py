from django.db import models
from datetime import datetime   
from django.contrib.auth.models import User
from django.urls import reverse

class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    ruc = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre_empresa

    def get_absolute_url(self):
        return reverse('empresa-home')

tipo_pago = (
    ('Efectivo','Efectivo'),
    ('Crédito', 'Crédito')
)

tipo_TI = (
    ('TEA', 'TEA'),
    ('TNA', 'TNA')
)

class Prestamo(models.Model):
    precio_venta = models.DecimalField(max_digits=11, decimal_places=4)
    cuota_inicial = models.DecimalField(max_digits=11, decimal_places=4)
    empresa_ofertante = models.CharField(max_length=100)
    empresa_solicitante = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo_de_pago = models.CharField(max_length=20, choices=tipo_pago, default='Efectivo')
    plazos_de_pago = models.IntegerField()
    tipo_tasa_interes = models.CharField(max_length=20, choices=tipo_TI, default='TEA')
    TEA = models.DecimalField(max_digits=7, decimal_places=4)
    TCEA = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    cuotas = models.IntegerField(null=True)
    intereses = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    VAN = models.DecimalField(max_digits=11, decimal_places=4, null=True)
    comision_rt = models.DecimalField(max_digits=9, decimal_places=4)
    fotocopias = models.DecimalField(max_digits=9, decimal_places=4)
    gastos_admin = models.DecimalField(max_digits=9, decimal_places=4)
    fecha_inicio = models.DateTimeField(default=datetime.now, blank=True)
    seguro_riesgo = models.DecimalField(max_digits=7, decimal_places=4)
    seguro_desgravamen = models.DecimalField(max_digits=7, decimal_places=4)
    plazo_de_gracia = models.IntegerField()
    date_posted = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100, null=True)
    vehiculo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.empresa_solicitante

    def get_absolute_url(self):
        return reverse('prestamo-tabla')




