# for with sequence
# dy default takes keys in dict
seta = {'aa', 'bb', 'dd', 'tt'}
avengers = {'ironman':'suit', 'captain':'shield', 'thor':'hammer'}

for x in avengers:
    print("x =", x)

print("----")

for x in avengers.values():
    print("x =", x)
