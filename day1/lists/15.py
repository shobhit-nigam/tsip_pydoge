# functions
# copy

lista = ["aa", "bb", "DD", "ww", "cc"]
listb = lista.copy() 

print("lista =",lista)
print("listb =",listb)
lista.sort()
lista.insert(3, "gg")
lista.append("ff")
print("-----")
print("lista =",lista)
print("listb =",listb)


