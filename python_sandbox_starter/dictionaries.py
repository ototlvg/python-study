# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

'''
Bueno, nos dicen que los dictionaries son como los objetos json en javascript

Resumeen: Son como obj json, pero al momento de llamar a una de sus propiedades en vez de usar
. o ->
usas [] como si fuera un array
'''

# Create dict
person = {
    'first_name': 'Jhon',
    'last_name': 'Doe',
    'age':30
}

print(person, type(person))

# Create dict with constructor
# person2= dict('first_name='Sara, last_name='Williams')

# Get value
'''
Cualquier de las dos es valida, pero la primera es la mas comun
'''
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-555'
print(person)

# Get dict keys
'''
Esto retorna las PROPIEDADES de los dictionaries
'''
print(person.keys())

# Get items
print(person.items())

# Copy dict - dice que se parece al 'spread operator' de javascript
person2= person.copy()
person2['city'] = 'Boston'

print(person2)

# Remove item
'''
Los dos hacen lo mismo
'''
del(person['age'])
person.pop('phone')

# Clear
'''
Deja vacio un dictionary
'''
person.clear()
print(person)

# Get length
print( len(person2) )

# List of dict
'''
Arreglo de dictionaries
'''
people = [
    {'name': 'Martha', 'age':30},
    {'name': 'Kevin', 'age':25}
] 

print(people[1]['name'])