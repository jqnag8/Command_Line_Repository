from prod_cartesiano import producto_cartesiano

def crear_relacion(prod_cartesiano: set, ley: str) -> set:
    """
        Genera un conjunto que resulta de hacer la relacion de un producto cartesiano.
    """
    relacion = set()
    if ley == '=':
        return relacion | {(x,y) for (x,y) in prod_cartesiano if x == y}
    elif ley == '>':
        relacion | {(x,y) for (x,y) in prod_cartesiano if x > y}
    elif ley == '>=':
        relacion | {(x,y) for (x,y) in prod_cartesiano if x >= y}
    elif ley == '<':
        relacion = relacion | {(x,y) for (x,y) in prod_cartesiano if x < y}
    elif ley == '<=':
        relacion = relacion | {(x,y) for (x,y) in prod_cartesiano if x <= y}
    elif ley == '+':
        relacion = relacion | {(x,y) for (x,y) in prod_cartesiano if (x + y == int(input("Ingrese el número al que tenga que ser igual: ")))}
    else:
        raise SyntaxError("Operación no reconocida") 
    return relacion

# ------ Reflexividad ------
def es_reflexiva(relacion: set) -> bool:
    """
        determina si una relacion es reflexiva. Toma una relacion hecho por producto_cartesiano y el primer conjunto del A X B.
    """
    resultado = True
    a  # Devuelve la union de los conjuntos
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
