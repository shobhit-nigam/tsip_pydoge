avengers = {'ironman':'suit', 
        'captain':['hammer', 'shield'], 
        'black widow':'pure elegance', 
        'thor':'hammer'}

xmen = ['wolverine', 'magneto', 'mystique']

marvel = {'venom':'super strength', 
        'xmen':xmen, 
        'av':avengers}

print("marvel =", marvel)

print("-------")
print("marvel['av'] =", marvel['av'])
print("-------")
print("marvel['av']['captain'] =", marvel['av']['captain'])
print("-------")
print("marvel['av']['captain'][0] =", marvel['av']['captain'][0])
print("-------")
print("marvel['av']['captain'][0][1] =", marvel['av']['captain'][0][1])

