# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Create tuple (with constructor) 
# fruits2 = tuple('Apples', 'Oranges','Grapes')

print(fruits)

'''
Los dos son equivalentes, pero de nuevo, usar la version con 
constructor no es popular y la mayoria usa la primera opcion, 
exactamente el mismo caso que con los lists
'''

# Single value needs trailing comma

'''
Si nosotros hacemos algo como esto
fruits2= ('Apples')

Y lo imprimimos
print(fruits2, type(fruits2))

Retornaria
~ Apples <class 'str'>

Como observamos, dice que es un string, pero al ponerlo con 
parentesis, pues quermos que sea un tuple, pero al ser un solo valor
python lo toma como si fuera un string normal, para corregir esto
se le agrega una coma al final
fruits2= ('Apples',)

'''
fruits2= ('Apples',)
print(fruits2, type(fruits2)) # Ahora si nos dice que es un tuple, retorna ('Apples',) <class 'tuple'>

# Get a Value from tuple
print(fruits[1]) #Es igual que con los list, se usan index

# Can't change value
'''
Como bien lo dice al principio del documento, las listas son como
constantes en C, no se pueden cambiar ni modificar cuando el codigo
se esta ejecutando, claro es posible llamarlos por el index PERO
no es posible modificarlo, si ejecutamos el codigo de la linea 50
el programa retornara un error.
'''
# fruits[0] = 'Nueva fruta!!'

# Delete tuple
'''
Elimina un tuple COMPLETO no solo un elemento, si con lo de abajo
tratamos de imprimir fruits2 QUE SI ESTA DECLARADO ARRIBA el programa
retornara un error, porque se elimino el fruits2 con el comando del
'''
del fruits2
# print(fruits2)

# Get length of tuple
print( len(fruits) )






# A Set is a collection which is unordered and unindexed. No duplicate members.
'''
Menciono que si necesitas una coleccion en una variable con elementos que no se repitan,
ahi podrias usar un set.
'''

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
'''
A diferencia de los tuples, los sets si pueden ser modificados en produccion
'''
fruits_set.add('Grape')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Remember we cant add duplicates
fruits_set.add('Apples')
'''
Ya existe Apples en el set, por lo que si lo intetamos
agregar de nuevo, no retornara un error, pero tampoco
lo agregara, porque ya existe
'''


# Clear set
'''
Esto vacia el set
'''
fruits_set.clear()
print(fruits_set)

# Delete set
'''
Este comando ELIMINA el set, arriba al momento de imprimirlo (despues de aplicar la) 
funcion clear() simplemente retorna
set()
Osea, regresa el set pero vacio
Pero al momento  de usar la funcion del, elimina por completo el set, por lo que
al momento de imprimirlo retornara un error, se puede observar 
'''
del fruits_set
print(fruits_set)