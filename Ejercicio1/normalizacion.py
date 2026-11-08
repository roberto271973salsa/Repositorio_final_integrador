
registros_raw= [
    {
        "sensor_id": " SENSOR-001 ", 
        "temperatura": "0 C", 
        "ubicacion": "Planta Norte"
    },
    {
        "sensor_id": "   SenSor-002 ", 
        "temperatura": "30c", 
        "ubicacion": ""  
    },
    {
        "sensor_id": "SENSOR-003", 
        "temperatura": "35 °c", 
        "ubicacion": "Planta Sur "
    },
    {
            "sensor_id": "SENSOR-009", 
            "temperatura": "19.833 °C", 
            "ubicacion": "   Planta SUR"
    },
    {
            "sensor_id": "sensor-010", 
            "temperatura": "29.8 C", 
            "ubicacion": " Planta Centro"
    },
    {
                "sensor_id": "sensor-006", 
                "temperatura": "45.8 C", 
                "ubicacion": "" 
    },
]

""" 
Procesa y transformar la información para retornar un nuevo diccionario estandarizado, 
garantizando que el identificador quede sin espacios sobrantes, la temperatura sea un 
valor numérico de tipo float sin sufijos de unidad, y la ubicación posea un valor por
defecto seguro en caso de no haberse registrado
"""

def limpiar_registro_sensor(registro_raw):
    sensor_id_limpio = registro_raw.get("sensor_id", "").strip().upper() # eliminar espacios sobrantes al inicio y final
    
    temperatura_raw = str(registro_raw.get("temperatura","0")) # Temperatura (valor float)
    temperatura_procesada = (temperatura_raw.replace("C", "")  # Temperatura sin sufijo
                                               .replace("c", "")
                                               .replace("°C", "")
                                               .replace("°c", "")
                                               .replace("°", "")
                                               .strip()
                            )    
    if temperatura_procesada :
       temperatura_float =round(float(temperatura_procesada), 1)
    else:
       temperatura_float = 0.0
    
    ubicacion_sector= registro_raw.get("ubicacion")            #Asignar ubicación con un valor por defecto
    if not ubicacion_sector or not ubicacion_sector.strip():
        ubicacion_sector ="PLANTA DESCONOCIDA"                 # Valor por defecto 
    else:
        ubicacion_sector = ubicacion_sector.strip().upper()
    
    registro_estandarizado = {                                  # Nuevo diccionario estandarizado                      
        "Sensor_id":sensor_id_limpio,
        "Temperatura en °C":temperatura_float,
        "Ubicacion":ubicacion_sector
    }
    return registro_estandarizado