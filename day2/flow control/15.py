# for with range
#
lista = ['aa', 'bb', 'dd', 'tt', 'aa', 'bb', 'tt', 'aa', 'aa', 'bb', 'xx']
avengers = {'ironman':'suit', 'captain':'shield', 'thor':'hammer'}

index_aa = []

for i in range(len(lista)):
    if lista[i] == 'aa':
        index_aa.append(i)
    if len(index_aa) == 2:
        break

print(index_aa)
