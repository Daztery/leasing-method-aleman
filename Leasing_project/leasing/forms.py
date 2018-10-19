from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['empresa_ofertante', 'empresa_solicitante', 'precio_venta_del_activo', 'numero_de_años',
    'frecuencia_de_pago', 'tipo_de_pago', 'tipo_tasa_interes', 'TEA', 'recompra', 'costos_notariales', 'costos_registrales', 'tasacion', 'comision_de_estudio', 'comision_de_activacion', 'comision_periodica', 
    'seguro_riesgo', 'intereses', 'fecha_inicio', 'plazo_de_gracia', 'modelo', 'vehiculo']

class PrestamoForm1(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['costos_registrales', 'tasacion', 'comision_de_estudio', 'comision_de_activacion', 'comision_periodica', 
    'seguro_riesgo', 'intereses', 'fecha_inicio', 'plazo_de_gracia', 'modelo', 'vehiculo']

class PrestamoForm2(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['empresa_ofertante', 'empresa_solicitante', 'precio_venta_del_activo', 'numero_de_años',
    'frecuencia_de_pago', 'tipo_de_pago', 'tipo_tasa_interes', 'TEA', 'recompra', 'costos_notariales']
