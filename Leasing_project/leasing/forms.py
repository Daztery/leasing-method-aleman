from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    empresa_ofertante=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'pad-custom'
        }
    ))
    
    class Meta:
        model = Prestamo
        fields = ['empresa_ofertante', 'empresa_solicitante', 'precio_venta_del_activo', 'numero_de_años',
    'frecuencia_de_pago', 'tipo_de_pago', 'tipo_tasa_interes', 'periodo_cap', 'tasa_de_interes', 'recompra', 'costos_notariales', 'costos_registrales', 'tasacion', 'comision_de_estudio', 'comision_de_activacion', 'comision_periodica', 
    'seguro_riesgo', 'fecha_inicio', 'plazo_de_gracia', 'periodo_inicial_pg', 'tasa_descuento_Ks', 'tasa_descuento_WACC', 'modelo', 'vehiculo']


    def clean(self):
        cleaned_data = super(PrestamoForm, self).clean()
        
        numero_de_años = cleaned_data.get('numero_de_años')
        frecuencia_de_pago = cleaned_data.get('frecuencia_de_pago')
        plazo_de_gracia = cleaned_data.get('plazo_de_gracia')
        periodo_inicial_pg = cleaned_data.get('periodo_inicial_pg')
        tipo_tasa_interes = cleaned_data.get('tipo_tasa_interes')
        periodo_cap = cleaned_data.get('periodo_cap')

        numero_cuotas_por_ano = 360/frecuencia_de_pago
        nCuotas = numero_cuotas_por_ano*numero_de_años

        meses_antes_de_nCuotas = plazo_de_gracia/30

        if tipo_tasa_interes == 'TEA' and periodo_cap != 0:
            self.add_error(None, forms.ValidationError('La tasa efectiva no tiene periodo de capitalización, por favor seleccione ninguno.'))

        if (periodo_inicial_pg + 1 + meses_antes_de_nCuotas + 1 > nCuotas or periodo_inicial_pg < 1) and plazo_de_gracia != 0:
            self.add_error(None, forms.ValidationError('El periodo de gracia no puede exceder un número de ' + str(int(nCuotas)) + ' cuotas ni ser menor a 1.'))
    

