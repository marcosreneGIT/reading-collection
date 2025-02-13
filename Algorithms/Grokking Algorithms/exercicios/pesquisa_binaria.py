numeros = []

numero = 128 * 2
for i in range(1, numero + 1):
    numeros.append(i)

def pesquisa_binaria(lista, item):
    baixo = 0
    alto  = len(lista)
    contador_etapas = 0
    
    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lista[meio]

        contador_etapas += 1

        if chute == item:
            return contador_etapas 
        
        if chute < item:
            baixo = meio + 1
        else:
            alto =  meio - 1

        
print(pesquisa_binaria(numeros, 128))