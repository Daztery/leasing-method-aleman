from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['precio_venta', 'cuota_inicial', 'empresa_ofertante', 'empresa_solicitante',
    'tipo_de_pago', 'plazos_de_pago', 'tipo_tasa_interes', 'TEA', 'comision_rt', 'fotocopias',
    'gastos_admin', 'fecha_inicio', 'seguro_riesgo', 'seguro_desgravamen', 'plazo_de_gracia', 
    'modelo', 'vehiculo']