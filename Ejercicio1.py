#RECURSIVA

import datetime

def fibonacci_recursiva(numero):
    """
    La función sirve para recibir un número entero positivo n

    y calcule el número de fibonacci asociado a ese número con bucles.

    Parametros:

        - n: numero entero positivo introducido por el usuario

    Salidas:

        - numero_fibonacci: es el (numero-2)+(numero+1)
        """

    if numero < 2:
        return numero
    else:
        return fibonacci_recursiva(numero-1) + fibonacci_recursiva(numero-2)

inicio_recursiva = datetime.datetime.now()
print(fibonacci_recursiva(40))
fin = datetime.datetime.now()
print(fin - inicio_recursiva)

#BUCLES

def fibonacci_bucles(numero):
    numero1 = 0
    numero2 = 1
    if numero == 1:
        return 0
    elif numero == 2:
        return 1
    for i in range(2,numero):
            total = numero1 + numero2
            numero1 = numero2
            numero2 = total
    return numero2

inicio_bucles = datetime.datetime.now()
print(fibonacci_bucles(40))
fin = datetime.datetime.now()
print(fin - inicio_bucles)