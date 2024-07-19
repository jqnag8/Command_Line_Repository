from conjuntos import producto_cartesiano

def crear_relacion(prod_cartesiano: set[tuple[int, int]], ley: str) -> set[tuple[int, int]]:
    """
        Genera un conjunto que resulta de hacer la relacion de un producto cartesiano.
    """
    if ley == '=':
        return {(x,y) for (x,y) in prod_cartesiano if x == y}
    elif ley == '>':
        return {(x,y) for (x,y) in prod_cartesiano if x > y}
    elif ley == '>=':
        return {(x,y) for (x,y) in prod_cartesiano if x >= y}
    elif ley == '<':
        return {(x,y) for (x,y) in prod_cartesiano if x < y}
    elif ley == '<=':
        return {(x,y) for (x,y) in prod_cartesiano if x <= y}
    elif ley == '+':
        return {(x,y) for (x,y) in prod_cartesiano if (x + y == int(input("Ingrese el número al que tenga que ser igual: ")))}
    else:
        raise SyntaxError("Operación no reconocida")

# ------ Inversa ------
def relacion_inversa(relacion: set[tuple[int, int]]) -> set:
    """
    Crea una realacion inversa a partir de una relacion dada
    """
    resultado = set()
    for (x,y) in relacion:
        resultado.add((y,x))
    return resultado

# ------ Composicion ------
def comp_relaciones(relacion1: set[tuple[int, int]], relacion2: set[tuple[int, int]]) -> set[tuple[int, int]]:
    """
    Crea una composicion entre relacion1 y relacion2
    """
    resultado = set()
    for (a, b) in relacion1:
        for (c, d) in relacion2:
            if b == c:
                resultado.add((a, d))
    return resultado

# ------ Reflexividad ------
def es_reflexiva(relacion: set[tuple[int, int]]) -> bool:
    """
        Recibe una relación y determina si es reflexiva.
    """

    for (x, y) in relacion:
        if (x, x) not in relacion or (y, y) not in relacion:
            return False
    return True

# ------ Simetria ------
def es_simetrica(relacion: set[tuple[int, int]]) -> bool:
    """
    Determina si una relacion es simétrica.
    """

    for (x, y) in relacion:
        if (y, x) not in relacion:
            return False
    return True

# ------ Antisimetria ------
def es_antisimetrica(relacion: set[tuple[int, int]]) -> bool:
    """
    Determina si una relacion es antisimetrica
    """

    for (x, y) in relacion:
        if (x != y) and (y, x) in relacion:
            return False
    return True

# ------ Transitividad ------
def es_transitiva(relacion: set[tuple[int, int]]) -> bool:
    """
    Determina si una relacion es transitiva.
    """

    for (a, b) in relacion:
        for (c, d) in relacion:
            if (b == c) and ((a, d) not in relacion):
                return False
    return True

# ------ MAIN ------
def main():
    to_set = lambda x: set(map(int, x.lstrip('{,').rstrip('},').split(','))) # toma una lista de valores y lo formatea de forma que devuelva un conjunto

    relacion_extension = input("Crear relacion? (s/N)")

    if relacion_extension == 'si':
        relacion_final = to_set(input("Ingrese la relación: "))
    else:
        conjunto_1 = to_set(input("Conjunto A = "))
        conjunto_2 = input("Conjunto B = ")
        if (conjunto_2 == ''):
            conjunto_2 = conjunto_1
        else:
            conjunto_2 = to_set(conjunto_2)
        print(producto_cartesiano(conjunto_1, conjunto_2))
        relacion_final = crear_relacion(producto_cartesiano(conjunto_1, conjunto_2),
            input("Ingrese la ley de la relacion: "))
        print(f"Relacion: {relacion_final}")

    print("Reflexividad: ", end=' ')
    if es_reflexiva(relacion_final):
        print("Si")
    else:
        print("No")

    print("Simetría: ", end=' ')
    if es_simetrica(relacion_final):
        print("Si")
    else:
        print("No")

    print("Antisimetría: ", end=' ')
    if es_antisimetrica(relacion_final):
        print("Si")
    else:
        print("No")

    print("Transitividad: ", end=' ')
    if es_transitiva(relacion_final):
        print("Si")
    else:
        print("No")

if __name__ == "__main__":
    main()
