def producto_cartesiano(set1: set, set2: set):
    """
        Genera el producto cartesiano entre dos conjuntos
    """
    result = set()
    for x in set1:
        for y in set2:
            result.add((x, y))
    return result

#  ------ MAIN ------ ---
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
