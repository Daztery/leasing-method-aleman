from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = ['empresa_ofertante', 'empresa_solicitante', 'precio_venta_del_activo', 'numero_de_años',
    'frecuencia_de_pago', 'tipo_de_pago', 'tipo_tasa_interes', 'tasa_de_interes', 'recompra', 'costos_notariales', 'costos_registrales', 'tasacion', 'comision_de_estudio', 'comision_de_activacion', 'comision_periodica', 
    'seguro_riesgo', 'fecha_inicio', 'plazo_de_gracia', 'periodo_inicial_pg', 'tasa_descuento_Ks', 'tasa_descuento_WACC', 'modelo', 'vehiculo']


    def clean(self):
        cleaned_data = super(PrestamoForm, self).clean()
        
        numero_de_años = cleaned_data.get('numero_de_años')
        frecuencia_de_pago = cleaned_data.get('frecuencia_de_pago')
        plazo_de_gracia = cleaned_data.get('plazo_de_gracia')
        periodo_inicial_pg = cleaned_data.get('periodo_inicial_pg')

        numero_cuotas_por_ano = 360/frecuencia_de_pago
        nCuotas = numero_cuotas_por_ano*numero_de_años

        meses_antes_de_nCuotas = plazo_de_gracia/30

        if periodo_inicial_pg + 1 + meses_antes_de_nCuotas + 1 > nCuotas or periodo_inicial_pg < 1:
            self.add_error(None, forms.ValidationError('El periodo de gracia no puede exceder un número de ' + str(int(nCuotas)) + ' cuotas ni ser menor a 1.'))
    

