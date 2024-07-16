from prod_cartesiano import producto_cartesiano

def crear_relacion(prod_cartesiano: set, ley: str) -> set:
    """
        Genera un conjunto que resulta de hacer la relacion de un producto cartesiano.
    """
    relacion = set()
    if ley == '=':
        return relacion | {(x,y) for (x,y) in prod_cartesiano if x == y}
    elif ley == '>':
        return relacion | {(x,y) for (x,y) in prod_cartesiano if x > y}
    elif ley == '>=':
        return relacion | {(x,y) for (x,y) in prod_cartesiano if x >= y}
    elif ley == '<':
        return relacion | {(x,y) for (x,y) in prod_cartesiano if x < y}
    elif ley == '<=':
        return relacion | {(x,y) for (x,y) in prod_cartesiano if x <= y}
    elif ley == '+':
        return relacion | {(x,y) for (x,y) in prod_cartesiano if (x + y == int(input("Ingrese el número al que tenga que ser igual: ")))}
    else:
        raise SyntaxError("Operación no reconocida")
    return relacion

# ------ Reflexividad ------
def es_reflexiva(relacion: set) -> bool:
    """
        Recibe una relación y determina si es reflexiva.
    """
    resultado = True
    for (x, y) in relacion:
        if (x, x) not in relacion or (y, y) not in relacion: # Verifica si están los pares ordenados que cumplen con la propiedad
            resultado = False
            return resultado
    return resultado

def test_es_reflexiva():
    assert es_reflexiva(producto_cartesiano({'a', 'b', 'v', 'h'}, {1, 2, 3, 4, 5, 6})) == False
    assert es_reflexiva(producto_cartesiano({1, 2}, {1, 2})) == True

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
    to_set = lambda x: set(map(int, x.lstrip('{,').rstrip('},').split(',')))

    conjunto_1 = to_set(input("Conjunto A = "))
    conjunto_2 = input("Conjunto B = ")
    if (conjunto_2 == ''):
        conjunto_2 = conjunto_1
    else:
        conjunto_2 = to_set(conjunto_2)
    print(producto_cartesiano(conjunto_1, conjunto_2))
    ley_relacion = input("Ingrese la ley de la relacion: ")
    print(ley_relacion)

    print(f"Relacion: {crear_relacion(producto_cartesiano(conjunto_1,
                                                          conjunto_2),
                                      ley_relacion)}")
    #     print("Reflexividad: ", end=' ')
    # if es_reflexiva(prod_carte, conjunto_1, conjunto_2):
    #     print("Si")
    # else:
    #     print("No")

    # print("Simetría: ", end=' ')
    # if es_simetrica(prod_carte):
    #     print("Si")
    # else:
    #     print("No")

main()
