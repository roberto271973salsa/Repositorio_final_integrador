from django.test import TestCase
import unittest
from .service import calcular_emisiones_carbono

"""
    Clase  de prueba TestCalculoEmisiones(unittest.TestCase).
    Diferentes casos de prueba necesarios para validar tanto la exactitud
    numérica del cálculo ante valores nominales como la correcta elevación de
    la excepción ante consumos fuera de rango (valores negativos).
"""
    
    
class TestCalcularEmisiones(unittest.TestCase):
    """
    El valor obtenido debe ser 80 ( multiplicar el valor de 200 * 0.4
    ( que es el valor por default declarado )
    """
    def test_calculo_nominal_default (self):
     resultado = calcular_emisiones_carbono(200)
     self.assertEqual(resultado,80.0)

    def test_calculo_factor_personalizado (self):
        """
        El valor obtenido debe ser 400 ( multiplicar el valor de 500 * 0.8
        ( que es un valor personalizado )
        """
        resultado = calcular_emisiones_carbono(500,factor_emision=0.8)
        self.assertEqual(resultado,400.0)    

    def test_total_consumo_cero (self):
        """
        El valor obtenido debe ser 0 , cuando el consumo de la planta es cero
        """
        resultado = calcular_emisiones_carbono(0) 
        self.assertEqual(resultado, 0.0)

    def test_total_consumo_negativo (self):             
            """
            Me permite visualizar si hay un valor negativo,lanza un "ValueError"
            """
            self.assertRaises(ValueError,calcular_emisiones_carbono,-200)  


