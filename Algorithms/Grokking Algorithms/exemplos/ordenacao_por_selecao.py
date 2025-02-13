def buscar_menor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
        
    return menor_indice
    

def ordenacao_por_selecao(arr): 
    novo_arr = []

    while len(arr) > 0:
        indice_menor = buscar_menor(arr)
        novo_arr.append(arr.pop(indice_menor))
        
    return novo_arr
    

arr = [2, 5, 1, 6, 9]

print(ordenacao_por_selecao(arr))