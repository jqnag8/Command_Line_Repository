def producto_cartesiano(set1: set, set2: set):
    """
        Genera el producto cartesiano entre dos conjuntos
    """
    result = set()
    for x in set1:
        for y in set2:
            result.add((x, y))
    return result

def test_producto_cartesiano():
    assert producto_cartesiano({1, 2, 3}, {1, 2}) == {(1, 1), (1, 2), (2, 1), (2,2), (3, 1), (3, 2)}
    assert producto_cartesiano(set(), set()) == set()
    assert producto_cartesiano(set(), {1, 2}) == set()

# ------ MAIN ------
def main():
    to_set = lambda x: set(map(int, x.lstrip('{,').rstrip('},').split(',')))
    conjunto_1 = to_set(input("Conjunto A = "))
    conjunto_2 = input("Conjunto B = ")
    if (conjunto_2 == ''):
        conjunto_2 = conjunto_1
    else:
        conjunto_2 = to_set(conjunto_2)
    prod_carte = producto_cartesiano(conjunto_1, conjunto_2)

    print(f"AxB = {producto_cartesiano(conjunto_1, conjunto_2)}")
    print(f"Ordenado en formato lista: {sorted(prod_carte)}")
    print(f"|AxB| = {len(prod_carte)}")


if __name__ == "__main__":
    main()
