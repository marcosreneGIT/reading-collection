# sem recursão 

caixas = [['...'], ['...'], ['...'], ['KEY'], ['...']]

def sem_recusao(caixas):
    while True:
        for i in range(len(caixas)):
            if caixas[i][0] == 'KEY':
                return print(f'Chave encontrada! Estava na caixa {i + 1}.')
        
            print('Caixa vazia...')
            
        print('Não há chave nas caixas.')
        break
            
sem_recusao(caixas)


print()
# com recursão 


def com_recursao(caixas, i = 0):
    if i >= len(caixas):
        return print('Não há chave nas caixas.')
    
    if caixas[i][0] == 'KEY':
        return print(f'Chave encontrada! Estava na caixa {i + 1}.')
     
    print('Caixa vazia...')
    com_recursao(caixas, i + 1)
    
com_recursao(caixas)

