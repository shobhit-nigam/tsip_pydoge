# functions

lista = ["aa", "bb", "DD", "ww", "cc"]
listc = ["aa", "bb", "DD", "ww", "cc"]
listx = ["xx", "yy", "zz", "uu"]

print(lista)
lista.append(listx)
print("-----")
print(lista)

print("-----")
print("-----")

print(listc)
listc.extend(listx)
print("-----")
print(listc)

