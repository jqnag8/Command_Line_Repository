import sys
import os

# Agrega el directorio src al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from relaciones import comp_relaciones,relacion_inversa, es_reflexiva, es_simetrica, es_antisimetrica
from conjuntos import producto_cartesiano

# Comp de relaciones
def test_composicion_relaciones() -> None:
    # Caso de prueba 1: relaciones vacías
    assert comp_relaciones(set(), set()) == set()

    # Caso de prueba 2: una relación vacía y otra no
    assert comp_relaciones(set(), {(1, 2)}) == set()
    assert comp_relaciones({(1, 2)}, set()) == set()

    # Caso de prueba 3: composición de una relación consigo misma
    assert comp_relaciones({(1, 2)}, {(1, 2)}) == set()

    # Caso de prueba 4: composición de múltiples pares
    assert comp_relaciones({(1, 2), (3, 4)}, {(2, 5), (4, 6)}) == {(1, 5), (3, 6)}

    # Caso de prueba 6: sin pares coincidentes
    assert comp_relaciones({(1, 2)}, {(3, 4)}) == set()

# Relacion inversa
def test_relacion_inversa():
    assert relacion_inversa(set()) == set()
    assert relacion_inversa({(1, 2)}) == {(2, 1)}
    assert relacion_inversa({(1, 2), (3, 4), (5, 6)}) == {(2, 1), (4, 3), (6, 5)}
    assert relacion_inversa({(1, 2), (2, 1)}) == {(2, 1), (1, 2)}
    assert relacion_inversa({(1, 2), (2, 1), (1, 2)}) == {(2, 1), (1, 2)}
    assert relacion_inversa({(1, 1), (2, 2), (3, 3)}) == {(1, 1), (2, 2), (3, 3)}

# es_simetrica
def test_es_simetrica():
    # Caso de prueba 1: relación vacía
    assert es_simetrica(set()) == True

    # Caso de prueba 2: relación con un solo par simétrico
    assert es_simetrica({(1, 1)}) == True

    # Caso de prueba 3: relación con un solo par no simétrico
    assert es_simetrica({(1, 2)}) == False

    # Caso de prueba 4: relación con múltiples pares simétricos
    assert es_simetrica({(1, 2), (2, 1), (3, 4), (4, 3)}) == True

    # Caso de prueba 5: relación con algunos pares no simétricos
    assert es_simetrica({(1, 2), (2, 1), (3, 4)}) == False

    # Caso de prueba 6: relación con pares idénticos
    assert es_simetrica({(1, 1), (2, 2), (3, 3)}) == True

    # Caso de prueba 7: relación mixta de pares simétricos y no simétricos
    assert es_simetrica({(1, 2), (2, 1), (3, 4), (4, 3), (5, 6)}) == False

# es_antisimetrica
def test_es_antisimetrica():
    # Caso de prueba 1: relación vacía
    assert es_antisimetrica(set()) == True

    # Caso de prueba 2: relación con un solo par idéntico
    assert es_antisimetrica({(1, 1)}) == True

    # Caso de prueba 3: relación con un solo par no idéntico
    assert es_antisimetrica({(1, 2)}) == True

    # Caso de prueba 4: relación con múltiples pares, todos diferentes
    assert es_antisimetrica({(1, 2), (3, 4)}) == True

    # Caso de prueba 5: relación con pares simétricos que violan la antisimetría
    assert es_antisimetrica({(1, 2), (2, 1)}) == False

    # Caso de prueba 6: relación con pares idénticos y no idénticos
    assert es_antisimetrica({(1, 1), (2, 2), (3, 3), (4, 5)}) == True

    # Caso de prueba 7: relación mixta con pares que violan la antisimetría
    assert es_antisimetrica({(1, 2), (2, 1), (3, 3), (4, 4)}) == False
