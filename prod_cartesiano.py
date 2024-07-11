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
    assert producto_cartesiano({}, {}) == set()
    assert producto_cartesiano({}, {1, 2}) == set()


# ------ Caracteristicas de relacion ------

# def es_reflexiva(relacion: set):
#     """
#         determina si una relacion es reflexiva
#     """
#     resultado = True
#     for (x, y) in relacion:
#         if (x, x) not in relacion:
#             resultado = False
#             return resultado
#     return restultado
# TODO que no recorra tuplas ya analizadas

# def test_es_reflexiva():
#     assert es_reflexiva(producto_cartesiano({'a', 'b', 'v', 'h'}, {1, 2, 3, 4, 5, 6})) == False
#     assert es_reflexiva(producto_cartesiano({1, 2}, {1,2}))

# ------ MAIN ------

def main():
    to_set = lambda x: sorted(set(x.split(',')))

    conjunto_1 = to_set(input("Ingrese el primer conjunto: "))
    conjunto_2 = to_set(input("Ingrese el segundo conjunto: "))

    print(f"{conjunto_1} X {conjunto_2} = {producto_cartesiano(conjunto_1, conjunto_2)}")

if __name__ == "__main__":
    main()

