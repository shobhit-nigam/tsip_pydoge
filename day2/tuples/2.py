# immutable
listx = ['aa', 'rr', 'dd', 'ww', 'tt', 'bb']
print(type(listx))
tup_x = ('aa', 'rr', 'dd', 'ww', 'tt', 'bb')
print(type(tup_x))

listx[2] = 'ss'

# error
tup_x[2] = 'ss'
