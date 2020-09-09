# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1           #int
# y = 2.5         #float
# name = 'Jhon'   #string -- Pueden usarse comillas simples o dobles
# is_cool = True  #boolean -- El booleano debe estar en mayusculas True/False de lo contrario si pones 'true' lo ve como una variabla a true

# Multiple assigment -- Es lo mismo que arriba, pero mas organizado OJO no es un array
x, y, name, is_cool = (1,2.5,'Jhon',True)


# print('Hello World') # En python2 no se ponian parentesis, en la v3 si
print(x, y, name, is_cool) # Podemos imprimir multiples lineas en una misma funcion

# Basic math
a = x+y

print(x, y, name, is_cool, a)

# We can now the type of a function
print(type(x)) # <class 'int'>

# Casting
x = str(x)
y = int(y) # Antes era un float 2.5, ahora que se imprimira, es un int con valor de 2
z= float(y)
print(type(z), z) # <class 'float'> -- y vuelve a ser un float, solo que logicamente ahora es 2.0 y no 2.5