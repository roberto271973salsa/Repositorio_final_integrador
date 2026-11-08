
# 🌿 Panel de Sustentabilidad - Ecotech Solutions

Sistema de monitoreo y gestión de emisiones de carbono y consumo energético para plantas operativas, desarrollado con **Django** y **Chart.js**.

## 🚀 Características Principales
- **Indicadores Globales:** Visualización en tiempo real del total de emisiones de CO₂e y la planta con mayor consumo.
- **Desglose Detallado:** Tablas organizadas por planta operativa.
- **Gráficos Interactivos:** Comparativas visuales (barras, líneas y distribución porcentual) implementadas con Chart.js y `chartjs-plugin-datalabels`.

## 🛠️ Tecnologías Utilizadas
- **Backend:** Python / Django
- **Frontend:** HTML5, CSS3 (Variables CSS, Grid / Flexbox)
- **Librerías de Gráficos:** Chart.js

## 📁 Estructura del Proyecto

REPOSITORIO_FINAL_INTEGRADOR/
│
├── Ejercicio1/       
│   ├── monitoreo.py/                     # Lógica y procesamiento de métricas 
│   └── normalización.py /                # Estanderiza la información obtenida   
│ 
├── Ejercicio2/             
│   ├── catalogo.py/                       # Dominio del Catálogo y Reglas de Inventario
│   └── views.py                           # Archivo de exportación .json
│   
|── Ejercicio3/             
│   └── Ecotech_solutions                  # Carpeta principal
│      └── Ecotech_solutions               # Carpeta datos por defecto        
│           └── sustentabilidad            # app del proyecto
|                └── manage.py             # Administrador del proyecto
|                └── service.py            # Lógica y procesamiento de métricas 
|                └── views.py              # visualizacion de los registros de las diferentes plantas
|                └── test.py               # Unitest ( test - casos de prueba)
|                └── urls.py               # contiene  path('panel/', vista_panel_sustentabilidad,name = "Panel Sustentable")
|                └── templates/
|                    └── sustentabilidad/
|                         └── panel.html   # Plantillas HTML (panel.html)
|
├── requirements.py                        # Lista de librerias entre ellas ( Django==6.1.3; numpy==2.5.4;pandas==3.1.0 )
└── README.md

Contacto : Roberto Ulloa ( Provincia de Mendoza - cel 2616957)
