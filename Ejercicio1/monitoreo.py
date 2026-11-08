from normalizacion import registros_raw, limpiar_registro_sensor

"""
Toma una colección de registros sanitizados previamente con la función del Punto A y
un valor límite. Debe retornar una tupla (lista_sensores_alerta, promedio_temperatura) 
conteniendo los IDs de los dispositivos que superan el umbral estipulado y el promedio
térmico global de la planta.
"""
def generar_resumen_sensores(lista_sensores_normalizados, umbral_temperatura):
    lista_sensores_alerta = []
    suma_temperaturas = 0.0
    total_sensores = len(lista_sensores_normalizados)
    
    if total_sensores == 0:
        return [], 0.0
    for sensor in lista_sensores_normalizados:
        temp_actual = sensor["Temperatura en °C"]
        suma_temperaturas += temp_actual
        if temp_actual > umbral_temperatura:                         # Verificar si supera el umbral estipulado
            lista_sensores_alerta.append(sensor["Sensor_id"])        # Guardamos el ID (string) como pide la consigna
            
    promedio_temperatura = suma_temperaturas / total_sensores        # Calcular el promedio térmico global
    return lista_sensores_alerta, promedio_temperatura
    
print("╔════════════════════════════════════════════════════════════╗")
print("│       BLOQUE DE EJECUCUÍON Y VISUALIZACIÓN DE FLUJO        │")
print("╚════════════════════════════════════════════════════════════╝")   
    
if __name__ == "__main__":
    print("Iniciando procesamiento de Estandarización\n")                      # Muestra proceso de ESTANDARIZACION 
    sensores_limpios = [limpiar_registro_sensor(reg) for reg in registros_raw] # Procesamos diccionario de la lista registros_raw 
    print("\n¡Proceso de Estandarización finalizado con éxito!")
    print("-" * 90)
    
    for sensor in sensores_limpios:                        # Muestra la lista final completa de diccionarios estandarizados
        print(sensor)
    print("-" * 90)
    UMBRAL_LIMITE = 28.0                                   # Definimos el umbral
    sensores_en_alerta, promedio_global = generar_resumen_sensores(sensores_limpios, UMBRAL_LIMITE)  # Resumen estadístico
    
    """
    MOSTRAMOS REPORTES FINALES
    """
    print("\n" + "=" * 70)
    print("            REPORTE DE SENSORES EN ALERTA   ")
    print("=" * 70)
    print(f" Umbral límite configurado : {UMBRAL_LIMITE:.1f} °C")
    print(f" Promedio térmico global   : {promedio_global:.1f} °C")
    
    if sensores_en_alerta:
        print(f" Sensores en Alerta :{', '.join(sensores_en_alerta)}")
    else:
        print(" Sensores en Alerta  :Ninguno")
    print("=" * 70)
    print()
    print("#" * 70)
    
    # DETALLE DE DISPOSITIVOS EN ALERTA (Ubicación y Temperatura)
    if sensores_en_alerta:
        print(" DETALLE DE UBICACIÓN Y TEMPERATURA EN ALERTA:")
                
        for sensor in sensores_limpios:                                 # Buscamos los sensores en alerta
            if sensor["Sensor_id"] in sensores_en_alerta:
                print(f" • Sensor ID : {sensor['Sensor_id']}")
                print(f"   Ubicación : {sensor['Ubicacion']}")
                print(f"   Temperatura: {sensor['Temperatura en °C']} °C")
                print(" " + "-" * 40)
    else:
        print(" ✅ Ningún sensor supera el umbral estipulado.")
    print("#" * 70)