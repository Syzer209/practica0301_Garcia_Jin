#RECURSIVA

import datetime

def fibonacci(n):

  """
  La función sirve para recibir un número entero positivo n

  y calcule el número de fibonacci asociado a ese número con bucles.

  Parametros:

      - n: numero entero positivo introducido por el usuario

  Salidas:

      - numero_fibonacci: es el (numero-2)+(numero+1)
  """

  if n == 0:
      return 0
  if n == 1:
      return 1
  return fibonacci(n-1) + fibonacci(n-2)

#BUCLES

def fibonaccibucle(n):

   a = 0
   b = 1

   for i in range(n):

       c = b + a
       a = b
       b = c

   return a

start_time = datetime.datetime.now()

print(fibonaccibucle(20))

end_time = datetime.datetime.now()

print("El tiempo de ejecución es de: ", end_time - start_time)
