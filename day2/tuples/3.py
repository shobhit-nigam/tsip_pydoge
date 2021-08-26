# immutable
tup_x = ('aa', 'rr', 'dd', 'ww', 'tt', 'bb')
print(type(tup_x))

print(tup_x.index('ww'))

# error
tup_x[2] = 'ss'

tup_x.sort()
