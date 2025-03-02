import pytest
from cine import Pelicula

# Prueba: Compra de entradas con asientos suficientes
def test_compra_exitosa():
    pelicula = Pelicula("Test Movie", 10, 5)
    resultado = pelicula.vender_entradas(3)
    assert resultado == "Has comprado 3 entradas para Test Movie. Total: $15"
    assert pelicula.asientos_disponibles == 7  # Verificar que se han descontado los asientos

# Prueba: Compra de más entradas de las disponibles
def test_compra_insuficiente():
    pelicula = Pelicula("Test Movie", 5, 5)
    resultado = pelicula.vender_entradas(6)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 5 asientos."
    assert pelicula.asientos_disponibles == 5  # No debería cambiar

# Prueba: Compra de cero entradas
def test_compra_cero():
    pelicula = Pelicula("Test Movie", 10, 5)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Test Movie. Total: $0"
    assert pelicula.asientos_disponibles == 10  # No debería cambiar
