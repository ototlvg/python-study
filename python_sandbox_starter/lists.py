# A List is a collection which is ordered and changeable. Allows duplicate members.
'''
Al parecer las listas son los equivalentes de los arrays
'''

# Create a list
numbers = [1,2,3,4,5]
fruits = ['Manzanas', 'Naranjas', 'Uvas', 'Peras']

# Using a constructor
numbers2 = list( (1,2,3,4,5) )

print(numbers, numbers2)

'''
Usar la forma de 'Using a constructor' puede que sea mas semantico
al momento de llamarlo como realmente se llama 'list', pero no
tiene ninguna otra ventaja sobre la primera opcion, en donde lo
tratamos como si fuera un array de verdad, por lo que la mayoria
prefiere tratarlo como array, asi que podemos usar ese siempre
'''

# Get a value
print(fruits[1])

# Get length of list
print( len(fruits) )

# Appen to list
fruits.append('Mangos')
print(fruits)

# Remove from list
'''
Aqui un comportamiento interesante y nuevo, para listas de strings
es posible el remover un elemento por el valor del array y no 
necesariamente por su posicion del index, aqui en vez de decir 
elimina el elemento en el index 2 del list fruits, dijimos, 
'elimina el elemento con valor Uvas'
'''
fruits.remove('Uvas')
print(fruits)

# Insert into position
'''
Es posible insertar un nuevo elemento en un index especifico,
el elemento que ocupaba la posicion simplemente se recorre hacia la izquierda
'''
fruits.insert(2, 'Cerezas')
print(fruits)

# Change value
fruits[0] = 'Blueberries'
print('Cambio de valor directo', fruits)

# Remove element by index with pop() function
fruits.pop(2)
print(fruits)

# Reverse list
'''
Algo importante a tener en cuenta, es que esta funcion no retorna
una copia de la lista original con los elementos en reversa, si no
que pone en reversa los elementos de LA LISTA ORIGINAL directamente,
por lo que es algo a tomar en cuenta y recordar
'''
fruits.reverse()
print(fruits)

# Sort list
'''
Organiza alfabeticamente los elementos del array original, aqui es
el mismo caso que con la funcion reverse, modifica directamente al
list original, no retorna una copia
'''
fruits.sort()
print(fruits)

# Reverse sort
'''
Lo mismo que sort, la diferencia es que ahora se hara el acomodo
de izquierda a derecha
'''
fruits.sort(reverse=True)
print(fruits)










