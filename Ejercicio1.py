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
   numero_fibonacci = (n - 2) + (n + 1)
   return print(numero_fibonacci)


start_time = datetime.datetime.now()
fibonacci(1)
end_time = datetime.datetime.now()
print("El tiempo de ejecución es de: ", end_time - start_time)



#BUCLES
import datetime

def fibonacci(n):

  numero_fibonacci = (n - 2) + (n + 1)
  return print(numero_fibonacci)


start_time = datetime.datetime.now()
fibonacci(1)
end_time = datetime.datetime.now()
print("El tiempo de ejecución es de: ", end_time - start_time)
