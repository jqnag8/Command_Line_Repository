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


# ------ Reflexividad ------
def es_reflexiva(relacion: set, conjunto1: set, conjunto2: set):
    """
        determina si una relacion es reflexiva. Toma una relacion hecho por producto_cartesiano y el primer conjunto del A X B.
    """
    resultado = True
    union1_2 = conjunto1 | conjunto2  # Devuelve la union de los conjuntos
    for elemento in union1_2: # Toma los primeras componentes de los pares ordenados para verificar la reflexividad.
        if (elemento, elemento) not in relacion:
            resultado = False
            return resultado
    return resultado

def test_es_reflexiva():
    assert es_reflexiva(producto_cartesiano({'a', 'b', 'v', 'h'}, {1, 2, 3, 4, 5, 6}), {'a', 'b', 'v', 'h'}, {1,2,3,4,5,6}) == False
    assert es_reflexiva(producto_cartesiano({1, 2}, {1, 2}), {1, 2}, {1, 2}) == True 

# ------ Simetria ------
def es_simetrica(relacion: set):
    resultado = True
    
    for (x, y) in relacion:
        if (y, x) not in relacion:
            resultado = False
            return resultado
    return resultado

def test_es_simetrica():
    assert es_simetrica(producto_cartesiano({1, 2}, {1, 2})) == True
    assert es_simetrica(producto_cartesiano({1, 2, 3}, {1, 2})) == False

# ------ MAIN ------
def main():
    to_set = lambda x: set(x.lstrip('{,').rstrip('},').split(','))
    conjunto_1 = to_set(input("Conjunto A = "))
    conjunto_2 = to_set(input("Conjunto B = "))

    if (conjunto_2 == {''}):
        conjunto_2 = conjunto_1
    prod_carte = producto_cartesiano(conjunto_1, conjunto_2)

    print(f"A X B = {producto_cartesiano(conjunto_1, conjunto_2)}")

    print("Reflexividad: ", end=' ')
    if es_reflexiva(prod_carte, conjunto_1, conjunto_2):
        print("Si")
    else:
        print("No")

    print("Simetría: ", end=' ')
    if es_simetrica(prod_carte):
        print("Si")
    else:
        print("No")

if __name__ == "__main__":
    main()

