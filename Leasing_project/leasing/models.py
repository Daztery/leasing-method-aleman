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

frec_pago = (
    (30, 'Mensual'),
    (60, 'Bimestral'),
    (90, 'Trimestral'),
    (120, 'Cuatrimestral'),
    (180, 'Semestral'),
)

plazo_g = (
    (0, 'sin plazo de gracia'),
    (30, '1 mes'),
    (60, '2 meses'),
    (90, '3 meses'),
    (120, '4 meses'),
    (150, '5 meses'),
    (180, '6 meses'),
)

class Prestamo(models.Model):
    empresa_ofertante = models.CharField(max_length=100)
    empresa_solicitante = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    precio_venta_del_activo = models.FloatField(null=True)
    numero_de_años = models.IntegerField(null=True)
    frecuencia_de_pago = models.IntegerField(choices=frec_pago, default=30)
    tipo_de_pago = models.CharField(max_length=20, choices=tipo_pago, default='Efectivo')
    tipo_tasa_interes = models.CharField(max_length=20, choices=tipo_TI, default='TEA')
    TEA = models.FloatField(null=True)
    recompra = models.FloatField(null=True)
    costos_notariales = models.FloatField(null=True)
    costos_registrales = models.FloatField(null=True)
    tasacion = models.FloatField(null=True)
    comision_de_estudio = models.FloatField(null=True)
    comision_de_activacion = models.FloatField(null=True)
    comision_periodica = models.FloatField(null=True)
    seguro_riesgo = models.FloatField(null=True)
    fecha_inicio = models.DateTimeField(default=datetime.now, blank=True)
    plazo_de_gracia = models.IntegerField(choices=plazo_g, default=30)
    tasa_descuento_Ks = models.FloatField(null=True)
    tasa_descuento_WACC = models.FloatField(null=True)
    date_posted = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100, null=True)
    vehiculo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.empresa_solicitante

    def get_absolute_url(self):
        return reverse('prestamo-tabla', kwargs={'pk': self.pk})




