# A function is a block of code which only runs when it is called. In Python, 
# we do not use parentheses and curly brackets, we use indentation with tabs or spaces

'''
Nota importante: aqui se respete el global scope y el function scope
por lo que podemos poner los nombres de queremos en las variables de las
funciones si tener miedo a que se encuetren conflictos en un futuro
'''

'''
Para crear una funcion, se pone la palabra recervada 'def' el nombre de
la funcion, seguida de 2 puntos, de ahi no se ponen brackets, si no que
se usa identacion
'''

# Create function
def sayHello(name):
    print(f'Hello {name}')

sayHello('Jason')

# Create function with default value
def sayHello2(name='Otho'):
    print(f'Hello {name}')

sayHello2()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num= getSum(3,4)
print(num)



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSuma = lambda num1, num2 : num1+num2

print(getSuma(5,3))