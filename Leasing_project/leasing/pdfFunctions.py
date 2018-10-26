from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from PyPDF2 import PdfFileMerger

def iterarPDFflujo(year, month, day, tables, x, prestamo, mess, path):

    c = canvas.Canvas(path + "LAP-Sol-" + str(prestamo.id) + mess + " " + str(prestamo.empresa_solicitante.razon_social) + "-Periodo-" +  str(x) + " " +
    str(year) + "-" + str(month) + "-" + str(day) + ".pdf", pagesize=landscape(letter))
    c.setFont('Helvetica', 30, leading=None)
    c.drawCentredString(415, 500, str(prestamo.empresa_solicitante.razon_social) + " Flujo de caja")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(100, 450, "Periodo: " + str(tables[x-1]["n"]))
    c.drawString(100, 425, "Saldo inicial: " + str(tables[x-1]["saldo_inicial"]))
    c.drawString(100, 400, "Interés: " + str(tables[x-1]["interes"]))
    c.drawString(100, 375, "Cuota: " + str(tables[x-1]["Cuota"]))
    c.drawString(100, 350, "Amortización: " + str(tables[x-1]["amortizacion"]))
    c.drawString(100, 325, "Seguro riesgo: " + str(tables[x-1]["seguro_riesgo"]))
    c.drawString(100, 300, "Comisión: " + str(tables[x-1]["comision"]))
    c.drawString(100, 275, "Recompra: " + str(tables[x-1]["recompra"])) 
    c.drawString(100, 250, "Saldo final: " + str(tables[x-1]["saldo_final"]))
    c.drawString(100, 225, "Depreciación: " + str(tables[x-1]["depreciacion"]))
    c.drawString(100, 200, "Ahorro tributario: " + str(tables[x-1]["ahorro_t"]))
    c.drawString(100, 175, "IGV: " + str(tables[x-1]["igv"]))
    c.drawString(100, 150, "Flujo bruto: " + str(tables[x-1]["flujo_b"]))
    c.drawString(100, 125, "Flujo igv: " + str(tables[x-1]["flujo_igv"]))
    c.drawString(100, 100, "Flujo neto: " + str(tables[x-1]["flujo_neto"]))
    c.save()

def PDFDE(year, month, day, prestamo, path, frecuencia_pago, dias_del_ano, IGV, impuesto_renta):

    c = canvas.Canvas(path + "LAP-Sol-" + str(prestamo.id) + " " + str(prestamo.empresa_solicitante.razon_social) + "-DE- " +
    str(year) + "-" + str(month) + "-" + str(day) + ".pdf", pagesize=landscape(letter))
    c.setFont('Helvetica', 30, leading=None)
    c.drawCentredString(415, 550, str(prestamo.empresa_solicitante.razon_social) + " datos iniciales")

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(100, 500, "Datos de entrada")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(100, 465, "Empresa ofertante: " + str(prestamo.empresa_ofertante))
    c.drawString(100, 440, "Empresa solicitante: " + str(prestamo.empresa_solicitante))
    c.drawString(100, 415, "Vehículo: " + str(prestamo.vehiculo))
    c.drawString(100, 390, "Modelo: " + str(prestamo.modelo))
    c.drawString(100, 365, "Tipo de pago: " + str(prestamo.tipo_de_pago))
    c.drawString(100, 340, "Tipo de tasa Interés: " + str(prestamo.tipo_tasa_interes))
    c.drawString(100, 315, "Plazo de gracia: " + str(prestamo.plazo_de_gracia) + ' días')
    c.drawString(100, 290, "Periodo inicial de plazo de gracia: " + str(prestamo.periodo_inicial_pg))
    c.drawString(100, 265, "Fecha de inicio: " + str(day) + '/' + str(month) + '/' + str(year)) 

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(450, 500, "Del préstamo")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(450, 465, "Precio de venta del activo: " + 'S/ ' +str(prestamo.precio_venta_del_activo))
    c.drawString(450, 440, "Número de años: " + str(prestamo.numero_de_años))
    c.drawString(450, 415, "Frecuencia de pago: " + frecuencia_pago)
    c.drawString(450, 390, "Nª días del año: " + str(dias_del_ano))
    c.drawString(450, 365, "TEA: " + str(prestamo.tasa_de_interes) + ' %')
    c.drawString(450, 340, "IGV: " + str(IGV) + ' %')
    c.drawString(450, 315, "IR: " + str(impuesto_renta) + ' %')
    c.drawString(450, 290, "Recompra: " + str(prestamo.recompra) + ' %')

    c.line(100, 240, 700, 240)

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(100, 200, "Costos iniciales")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(100, 165, "Costes notariales: " + 'S/ ' + str(prestamo.costos_notariales))
    c.drawString(100, 140, "Costes registrales: " + 'S/ ' + str(prestamo.costos_registrales))
    c.drawString(100, 115, "Tasación: " + 'S/ ' + str(prestamo.tasacion))
    c.drawString(100, 90, "Comisión de estudio: " + 'S/ ' + str(prestamo.comision_de_estudio))
    c.drawString(100, 65, "Comisión de activación: " + 'S/ ' + str(prestamo.comision_de_activacion))

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(450, 200, "Costos periódicos")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(450, 165, "Comisión periódica: " + 'S/ ' + str(prestamo.comision_periodica))
    c.drawString(450, 140, "Seguro de riesgo: " + str(prestamo.seguro_riesgo) + ' %')

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(450, 100, "Costo de oportunidad")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(450, 65, "Tasa de descuento Ks: " + str(prestamo.tasa_descuento_Ks) + ' %')
    c.drawString(450, 40, "Tasa de descuento WACC: " + str(prestamo.tasa_descuento_WACC) + ' %')

    c.save()

def PDFRE(year, month, day, prestamo, path, IGV_del_activo, valor_de_venta_a, monto_del_leasing, TEP, numero_cuotas_por_ano, nCuotas,
    s_riesgo, intereses, amortizacion_c, seguro_ctr, comisiones_p, recompra_t, desembolso_t, TCEA_fb, TCEA_fn, VAN_fb, VAN_fn):

    c = canvas.Canvas(path + "LAP-Sol-" + str(prestamo.id) + " " + str(prestamo.empresa_solicitante.razon_social) + "-RE- " +
    str(year) + "-" + str(month) + "-" + str(day) + ".pdf", pagesize=landscape(letter))
    c.setFont('Helvetica', 30, leading=None)
    c.drawCentredString(415, 550, str(prestamo.empresa_solicitante.razon_social) + " resultados")

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(100, 500, "Del arrendamiento")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(100, 465, "IGV del activo: " + 'S/ ' + str(round(IGV_del_activo, 2)))
    c.drawString(100, 440, "Valor venta del activo: " + 'S/ ' + str(round(valor_de_venta_a,2)))
    c.drawString(100, 415, "Monto del leasing: " + 'S/ ' + str(round(monto_del_leasing,2)))
    c.drawString(100, 390, "TEP: " + str(round(TEP,4)) + ' %')
    c.drawString(100, 365, "Nº cuotas por año: " + str(numero_cuotas_por_ano))
    c.drawString(100, 340, "Nº total de cuotas " + str(nCuotas))

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(450, 500, "Gastos periódicos:")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(450, 465, "Seguro riesgo: " + 'S/ ' + str(s_riesgo))

    c.line(100, 315, 700, 315)

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(100, 275, "Totales por")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(100, 240, "Intereses: " + 'S/ ' + str(round(intereses,2)))
    c.drawString(100, 215, "Amoritzación del capital: " + 'S/ ' + str(round(amortizacion_c,2)))
    c.drawString(100, 190, "Seguro contra todo riesgo: " + 'S/ ' + str(seguro_ctr))
    c.drawString(100, 165, "Comisiones periódicas: " + 'S/ ' + str(comisiones_p))
    c.drawString(100, 140, "Recompra: " + 'S/ ' + str(round(recompra_t,2)))
    c.drawString(100, 115, "Desembolso total: " + 'S/ ' + str(round(desembolso_t,2)))

    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawString(450, 275, "Indicadores de rentabilidad:")
    c.setFont('Helvetica', 15, leading=None)
    c.drawString(450, 240, "TCEA flujo bruto: " + str(round(TCEA_fb,4)) + ' %')
    c.drawString(450, 215, "TCEA flujo neto: " + str(round(TCEA_fn,4)) + ' %')
    c.drawString(450, 190, "VAN flujo bruto: " + 'S/ ' + str(round(VAN_fb,2)))
    c.drawString(450, 165, "VAN flujo neto: " + 'S/ ' + str(round(VAN_fn,2)))

    c.save()