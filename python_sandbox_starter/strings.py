# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Jason'
age = 37

# Concatenate
# print('Hello my name is ' + name) -- Se concatena igual que en Js
# print('Hello my name is' + name + 'and I am' + age) # -- Esto retorna un error, ya que solo se pueden concatenar strings, no tiene autocast al parecer
print('1. Hello my name is ' + name + ' and I am ' + str(age)) # Debemos de hacer el cast de forma manual, y ahi si funcionara

# String Formatting

# Arugments by position
'''
Esta forma es como en C, se ponen 'placeholders' dentro del string
y por fuera usando la funcion 'format()' se especifican las 
variables de los placeholders ({name},{age})
'''
print('2. My name is {name} and I am {age}'.format(name=name,age=age))


# F-Strings (Python V3.6+)
'''
Es como en JS, solo que en vez de poner `` (comillas inversas, 'backtips')
se pone una f al principio y no se usa el simbolo de dolar $
'''
print(f'3. Hello 2, my name is {name} and I am {age}')


# String Methods
s = 'hello world'

# Capitalize string
print(s.capitalize()) # Solo la primera letra es afectada NO todo el string

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case - Las mayusculas las pasa a minusculas y las mayusculas a minusculas
sc= 'HeLLo WoRlD'
print('Swap case: ' + sc.swapcase())

# Get length 
'''
This length is a function can be used on string, list, vectors,
basic any data type and is gonna get the lenght
'''
print(len(s))

# Replace
'''
Reempleza todas las palabras del primer argumento, por la palabra
del segundo argumento
'''
print(s.replace('world', 'everyone')) 

# Count
'''
Retorna cuantas letras hay en el string especificado en el
argumento
'''
# print('Count:')
sub = 'h'
print(s.count(sub))

# Starts with
'''
Pregunta si el string empieza con lo que se pone en el argumento
'''
print(s.startswith('hello'))

# Ends with
'''
Pregunta si el string termina con lo que se pone en el argumento
'''
print(s.endswith('d'))

# Split into a list
'''
Al parecer una lista es un array, separa las letras en un array
'''
print(s.split())

# Find position
'''
Encuentra la posicion de un caracter (el primero que encuentre)
'''
print(s.find('r'))

# Is all alphanumeric -- return boolean, retorna false por el espacio -- FALTA INVESTIGAR MAS
print(s.isalnum())

# Is all alphabetic -- return boolean, retorna false por el espacio -- FALTA INVESTIGAR MAS
print(s.isalpha())

# Is all numeric -- return boolean
print(s.isnumeric())