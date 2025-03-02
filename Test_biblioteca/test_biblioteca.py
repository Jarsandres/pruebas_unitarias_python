import pytest
from biblioteca import Libro, Biblioteca

# 2.1. PRUEBAS PARA LA CLASE LIBRO

def test_libro_atributos():
    libro = Libro("Clean Code", "Robert C. Martin", 2008)
    assert libro.titulo == "Clean Code"
    assert libro.autor == "Robert C. Martin"
    assert libro.anio == 2008
    assert libro.prestado == False

def test_libro_estado():
    libro = Libro("Clean Code", "Robert C. Martin", 2008)
    assert str(libro) == "Clean Code de Robert C. Martin (2008) - disponible"
    libro.prestado = True
    assert str(libro) == "Clean Code de Robert C. Martin (2008) - prestado"


# 2.2. PRUEBAS PARA LA CLASE BIBLIOTECA

@pytest.fixture
def biblioteca():
    return Biblioteca()

@pytest.fixture
def libro():
    return Libro("The Pragmatic Programmer", "Andrew Hunt & David Thomas", 1999)


# Agregar libros
def test_agregar_libro(biblioteca, libro):
    biblioteca.agregar_libro(libro)
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0] == libro


# Eliminar libros
def test_eliminar_libro_existente(biblioteca, libro):
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("The Pragmatic Programmer")
    assert len(biblioteca.libros) == 0

def test_eliminar_libro_inexistente(biblioteca):
    biblioteca.eliminar_libro("Refactoring")
    assert len(biblioteca.libros) == 0  # No debe afectar la lista


# Buscar libros
def test_buscar_libro_existente(biblioteca, libro):
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.buscar_libro("The Pragmatic Programmer")
    assert resultado == libro

def test_buscar_libro_inexistente(biblioteca):
    resultado = biblioteca.buscar_libro("You Don't Know JS")
    assert resultado is None


# Listar libros
def test_listar_libros(biblioteca, libro):
    biblioteca.agregar_libro(libro)
    assert biblioteca.listar_libros() == ["The Pragmatic Programmer de Andrew Hunt & David Thomas (1999) - disponible"]


# Prestar libros
def test_prestar_libro_disponible(biblioteca, libro):
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.prestar_libro("The Pragmatic Programmer")
    assert resultado == "Has pedido prestado el libro 'The Pragmatic Programmer'."
    assert libro.prestado == True

def test_prestar_libro_ya_prestado(biblioteca, libro):
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("The Pragmatic Programmer")
    resultado = biblioteca.prestar_libro("The Pragmatic Programmer")
    assert resultado == "El libro 'The Pragmatic Programmer' ya está prestado."

def test_prestar_libro_inexistente(biblioteca):
    resultado = biblioteca.prestar_libro("Design Patterns")
    assert resultado == "El libro 'Design Patterns' no se encuentra en la biblioteca."


# Devolver libros
def test_devolver_libro_prestado(biblioteca, libro):
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("The Pragmatic Programmer")
    resultado = biblioteca.devolver_libro("The Pragmatic Programmer")
    assert resultado == "Has devuelto el libro 'The Pragmatic Programmer'."
    assert libro.prestado == False

def test_devolver_libro_no_prestado(biblioteca, libro):
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.devolver_libro("The Pragmatic Programmer")
    assert resultado == "El libro 'The Pragmatic Programmer' no estaba prestado."

def test_devolver_libro_inexistente(biblioteca):
    resultado = biblioteca.devolver_libro("Java Concurrency in Practice")
    assert resultado == "El libro 'Java Concurrency in Practice' no se encuentra en la biblioteca."
