

def calcular_emisiones_carbono(Consumo_Kwh: float,factor_emision: float = 0.4):
    """
    Calcula las emisiones de carbono en kwh con un factor de emision
    de 0.4.
    Eleva ValueError si el consumo es negativo
    """
    if Consumo_Kwh < 0:                      # Parametro para resultado negativo
        raise ValueError ("El valor no puede ser negativo")
    return Consumo_Kwh * factor_emision


def calcular_emisiones_carbono(consumo_kwh):
    """
    Convierte el consumo en Kwh a emisiones de CO2e.
    Permite valores negativos para reflejar devoluciones o correcciones.
    """
    factor_emision = 0.4  # Factor de conversión
    return consumo_kwh * factor_emision  # Si es negativo, el resultado será negativo de forma lógica




def Obtener_metricas_consumo (registros: float):
    """
    Se calcula las metricas, procesando un historial de consumos por planta industrial 
    para determinar  el total global de emisiones y la planta de mayor consumo 
    """
    
    total_global_de_emisiones = 0           # inicializo en "0"
    emisiones_por_planta = {}                   # Creo una lista vacia
    """
    Obtiene los valores totales
    """
    for registro in registros:
        planta = registro.get ("Planta","Planta Desconocida")
        consumo = registro.get ("Consumo Kwh", 0.0) ######
        
        emisiones= calcular_emisiones_carbono (consumo) # Algoritmo de los difeentes calculos
        total_global_de_emisiones  += emisiones
        
        if planta not in emisiones_por_planta:
            emisiones_por_planta[planta] = 0.0
        emisiones_por_planta[planta] += emisiones
    
    """
    Obtiene la Planta de Mayor consumo de todo el listado de registro
    """
    planta_de_mayor_consumo = "Ninguna"
    mayor_emisión = 0.0
    
    for planta, emisiones in emisiones_por_planta.items():
        if emisiones > mayor_emisión:
           mayor_emisión = emisiones
           planta_de_mayor_consumo = planta
    
    return {
        "total_global_de_emisiones": total_global_de_emisiones,   
        "planta_de_mayor_consumo": planta_de_mayor_consumo,
        "emisiones_por_planta": emisiones_por_planta ,
    }       