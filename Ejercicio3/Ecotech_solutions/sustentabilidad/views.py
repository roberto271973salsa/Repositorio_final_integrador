from django.shortcuts import render
from .service import Obtener_metricas_consumo
 
def vista_panel_sustentabilidad (request):
    """ 
    Registro tomados de los sensores de las diferentes plantas ,
    """
    registros = [
        {"Planta": "Planta Norte", "Consumo Kwh": 1450.5},
        {"Planta": "Planta Sur", "Consumo Kwh": 2520.0},
        {"Planta": "Planta Este", "Consumo Kwh": 820.0},
        {"Planta": "Planta Oeste", "Consumo Kwh": 2130.4},
        {"Planta": "Planta Desconocida", "Consumo Kwh": 310.2},
        {"Planta": "Planta Norte", "Consumo Kwh": 940.8},
        {"Planta": "Planta Sur", "Consumo Kwh": 1750.0},
        {"Planta": "Planta Este", "Consumo Kwh": 852.5},
        {"Planta": "Planta Oeste", "Consumo Kwh": 1120.0},
        {"Planta": "Planta Desconocida", "Consumo Kwh": 550.7},
        {"Planta": "Planta Norte", "Consumo Kwh": 3020.1},
        {"Planta": "Planta Sur", "Consumo Kwh": 640.3},
        {"Planta": "Planta Este", "Consumo Kwh": 1290.0},
        {"Planta": "Planta Oeste", "Consumo Kwh": 890.6},
        {"Planta": "Planta Desconocida", "Consumo Kwh": 430.0},
        {"Planta": "Planta Norte", "Consumo Kwh": 1155.2},
        {"Planta": "Planta Sur", "Consumo Kwh": 980.4},
        {"Planta": "Planta Este", "Consumo Kwh": 2400.9},
        {"Planta": "Planta Oeste", "Consumo Kwh": 760.3},
        {"Planta": "Planta Desconocida", "Consumo Kwh": 150.0}
    ]

    metricas = Obtener_metricas_consumo (registros)

    contexto = { 
        "total_emisión": metricas["total_global_de_emisiones"],
        "planta_mayor_consumo": metricas["planta_de_mayor_consumo"],
        "emision_por_planta": metricas["emisiones_por_planta"],
        "registros": registros
    }
    
    return render(request, "sustentabilidad/panel.html", contexto)
