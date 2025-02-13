def pesquisa_binaria(lista, item): # lista precisa esta ordenada

    baixo = 0 
    alto  = len(lista) - 1 
    

    while baixo <= alto:
        meio = (baixo + alto) // 2 # divisao inteira
        chute = lista[meio]

        if  chute == item:
            return meio
        elif chute > item:
            alto  = meio - 1
        else:
            baixo = meio + 1

    return None

lista = [0, 1, 3, 4, 7, 8, 10, 15, 16, 18, 19]

print(pesquisa_binaria(lista, 15))
print(lista[pesquisa_binaria(lista, 15)])

        