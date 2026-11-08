import json

class StockInvalidoError(ValueError):
    """Excepción personalizada para valores de stock negativos."""
    def __init__(self, mensaje="El Stock no puede ser un valor negativo."):
        super().__init__(mensaje)


class DispositivoEcológico:
    def __init__(self, codigo: str, marca: str, precio: float, cant_celdas: int, stock: int):
        self.codigo = codigo
        self.marca = marca
        self.precio = precio
        self.cant_celdas = cant_celdas
        self.__stock = 0                 
        self.stock = stock               # Llama al setter para aplicar la validación
    
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise StockInvalidoError(f"Error de stock: '{nuevo_stock}' no es válido. \n      El Stock no puede tener valor negativo.")
        self.__stock = nuevo_stock
    
    """Método base para la ficha técnica (Polimorfismo)."""

    def generar_ficha_tecnica(self) -> str:
        return (
            f"PRODUCTO:\n"
            f"Codigo: {self.codigo}\n"
            f"Marca: {self.marca}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Cantidad de celdas: {self.cant_celdas}\n"
            f"Stock: {self.__stock} unidades"
        )


class PanelSolar(DispositivoEcológico):
    def __init__(self, codigo: str, marca: str, precio: float, cant_celdas: int, stock: int, potencia_w: int, capacidad: float):
        super().__init__(codigo, marca, precio, cant_celdas, stock)
        self.potencia_w = potencia_w
        self.capacidad = capacidad

    def mostrar_ficha_tecnica(self) -> str:
        ficha_base = super().generar_ficha_tecnica()
        return (
            f"{ficha_base}\n"
            f"Potencia: {self.potencia_w} Watts \n"
            f"Capacidad: {self.capacidad} %"
        )


class GestorInventario:
    def guardar_catalogo_ecotech_json(self, lista_dispositivo, ruta_archivo):
        catalogo = []
        for dispositivo in lista_dispositivo:
            producto = {
                
                "Codigo": dispositivo.codigo,
                "Marca": dispositivo.marca,
                "Precio": dispositivo.precio,
                "Cantidad de celdas": dispositivo.cant_celdas,
                "Stock": dispositivo.stock                      
            }
            if isinstance(dispositivo, PanelSolar):                # Verificamos si es un PanelSolar usando isinstance
                producto["potencia_w"] = dispositivo.potencia_w
                producto["capacidad"] = dispositivo.capacidad
            
            catalogo.append(producto)
        
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            json.dump(catalogo, file, indent=4, ensure_ascii=False)
            print("#" * ancho)
            print("✅  Catálogo guardado exitosamente")
            print("#" * ancho)

if __name__ == "__main__":
    
    ancho = 60
    
    print("╔════════════════════════════════════════════════════════════╗")
    print("│                     BLOQUE DE PRUEBA                       │")
    print("╚════════════════════════════════════════════════════════════╝")   
    
    # Creamos algunos dispositivos de prueba 
    
    Panel_1 = PanelSolar("PS001", "EcoSun", 150000, 24, 40, 300, 21.5)
    Panel_2 = PanelSolar("PS002", "Dream", 135000, 36, 25, 400, 22)
    Equipo_Solar_1 = DispositivoEcológico("ES003", "System_sol", 800000, 24, 5)
    Equipo_Solar_2 = DispositivoEcológico("ES004", "System_sol", 700000, 24, 10)
    
    # Probar la captura de excepción por stock negativo
    try:
        Panel_3 = PanelSolar("PS004", "Gateway", 1350000, 36, -100, 400, 22) # (Nota: Panel_3 fallaría por valor negativo de stock
    except StockInvalidoError as error:
        print("*" * 60)
        print(f" ⚠️    ERROR CONTROLADO: {error}")
        print("*" * 60)
    productos = [Panel_1, Panel_2, Equipo_Solar_1, Equipo_Solar_2]  # Lista de productos válidos para exportar
    
    for producto in productos:
        print("=" * ancho)
        if hasattr(producto, 'mostrar_ficha_tecnica'):
            print(producto.mostrar_ficha_tecnica())
        else:
            print(producto.generar_ficha_tecnica())
        print("=" * ancho)    
        
    print("ADMINISTRADOR DE CATALOGOS".center(ancho))
    print("=" * 60)
    
    gestor = GestorInventario()
    gestor.guardar_catalogo_ecotech_json(productos, "catalogo_ecotech.json")
    