# for with range
#
lista = ['aa', 'bb', 'dd', 'tt', 'aa', 'bb', 'tt', 'aa', 'aa', 'bb', 'xx']
avengers = {'ironman':'suit', 'captain':'shield', 'thor':'hammer'}


for val in lista:
    if val == 'tt':
        print(val, "found")
        break
else:
    print("not found")

# else executes if loop does not break
print("------")
for val in lista:
    if val == 'rr':
        print(val, "found")
        break
else:
    print("not found")
