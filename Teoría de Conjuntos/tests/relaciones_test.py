import sys
import os

# Agrega el directorio src al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from relaciones import comp_relaciones, es_reflexiva, es_simetrica, relacion_inversa
from conjuntos import producto_cartesiano

# Comp de relaciones
def test_composicion_relaciones():
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
# def test_es_reflexiva():
#     assert es_reflexiva(producto_cartesiano({'a', 'b', 'v', 'h'}, {1, 2, 3, 4, 5, 6})) == False
#     assert es_reflexiva(producto_cartesiano({1, 2}, {1, 2})) == True

# def test_es_simetrica():
#     assert es_simetrica(producto_cartesiano({1, 2}, {1, 2})) == True
#     assert es_simetrica(producto_cartesiano({1, 2, 3}, {1, 2})) == False
