import sys
import os

# Agrega el directorio src al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from conjuntos import producto_cartesiano


def test_producto_cartesiano():
    assert producto_cartesiano({1, 2, 3}, {1, 2}) == {(1, 1), (1, 2), (2, 1), (2,2), (3, 1), (3, 2)}
    assert producto_cartesiano(set(), set()) == set()
    assert producto_cartesiano(set(), {1, 2}) == set()
