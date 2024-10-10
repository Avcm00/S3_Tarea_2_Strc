#1. Define una función que tome dos números como argumentos y retorne su suma.
def add_two_numbers():
    a=2         #O(1)
    b=3         #O(1)
    return f'{a + b}'   # O(1)
print(add_two_numbers())
#Big #O(1)

#2. Escribe una función que convierta grados Celsius a Fahrenheit.
def celcius_to_farenheit(cel):
    return f' {(cel*1.8)+32}'       #O(1)
print(celcius_to_farenheit(0))
#Big #O(1)

#3. Crea una función que reciba una lista de números y retorne el promedio
list=[a for a in range(1,6)]  # O(1)
def list_prom(list):
    sum= 0      # O(1)
    for x in list:      # O(n)
        sum += x        # O(1)
    return f'{sum/len(list)}'   # O(1)
print(list_prom(list))
#Big O: O(n)

#4. Define una función que tome un string como argumento y retorne True si es un
#palíndromo, False en caso contrario.
def palindromo(string):
    pal =''     # O(1)
    if len(string) == 1:    # O(1)
        return True     # O(1)
    else:
        for i in string:    # O(n)
            pal= i + pal    # O(1)
        return pal == string    # O(1)
print(palindromo('anas'))
# Big O: O(1)

#5. Crea una función que retorne el mayor de tres números.
def mayor_tres(x,y,z):
    if x > y and x > z: # O(1)
        return f'{x} es el numero mayor'
    elif y > x and y > z:   # O(1)
        return f'{y} es el numero mayor'
    elif z > x and z > y:   # O(1)
        return f'{z} es el numero mayor'
    elif x == y or x == z or z== y: # O(1)
        return f'dos numero son iguales'
    else:   # O(1)
        return f'los tres numeros son iguales'
print(mayor_tres(1,2,2))
#Big O: O(1)

#6. Define una función que compruebe si un número es primo.
def n_primo(x):
    if x <= 1:      # O(1)
        return 'El numero no es primo'
    if x == 2 or x == 3:    # O(1)
        return 'El numero es primo'
    if x % 2 == 0 or x % 3 == 0:    # O(1)
        return 'El numero no es primo'
    
    i = 5   # O(1)
    while i * i <= x:   # O(√n)
        if x % i == 0 or x % (i + 2) == 0:  # O(1)
            return 'El numero no es primo'
        i += 6  # O(1)
    
    return 'El numero es primo'

print(n_primo(5))
#Big O: O(√n)

#7. Defisadne una función que reciba 2 strings y verifique que ambos tengan la misma cantidad y valor en sus caracteres.
#  Ejemplo “earth” contiene la misma cantidad y valores que “heart”
def m_caracter(string_1, string_2):
   return 'iguales en caracteres y en longitud' if sorted(string_1) == sorted(string_2) else  'no son iguales' #O(nlog n)
print(m_caracter("ana",'naaa'))
#Big O: O(n log n)
#8. Escribe una función que retorne una lista con los primeros n números primos.
def list_primos(x):
    primos = [] # O(1)
    if x <= 1:  # O(1)
        return primos
    
    for num in range(2, x + 1): # O(n)
        es_primo = True     # O(1)
        for i in range(2, int(num**0.5) + 1):   # O(n)
            if num % i == 0:    # O(1)
                es_primo = False
                break
        if es_primo:    # O(1)
            primos.append(num)
    
    return primos

print(list_primos(9))
#Big O: O(n^2)
#9. Diseña una función que calcule el MCD (máximo común divisor) de dos números.
def MCD(n1,n2):
    while n2 != 0:  # O(n log n)
        n1, n2 = n2, n1 % n2    # O(1)
    return n1   # O(1)
print(MCD(9,3))
#Big O: O(nlog n)
#10. Usa list comprehension para crear una lista de los cuadrados de los números del 1 al 10.
lista_n_cuadrado = [x**2 for x in range(1,11)] # O(1)
print(lista_n_cuadrado)
#Big O: # O(1)
#11. Crea una lista de los números impares de una lista existente de números del 1 al 20.
lista_1_20 = [x for x in range(1, 21)] # O(1)
lista_impar = [x for x in lista_1_20 if x % 2 != 0]# O(1)
print(lista_impar)
#Big O: # O(1)
#12. Usa list comprehension para convertir una lista de temperaturas en Celsius a Fahrenheit
lista_celcius=[32,34,29,30,31] # O(1)
lista_celsius_to_farenheit = [(x *1.8)+32 for x in lista_celcius]   # O(1)
print(lista_celsius_to_farenheit)
# Big O: O(1)
#13. Filtra todos los números mayores a 10 en una lista usando list comprehension.
lista_mayor_10 = [ x for x in lista_1_20 if x > 10] # O(1)
#14. Utiliza map para convertir todos los elementos de una lista de números enteros a flotantes
lista_1_25 = [x for x in range(1,26)]   # O(1)
lista_float = list(map(float, lista_1_25))  # O(1)

print(lista_float)
#Big O: O(1)
#15. Aplica filter para obtener sólo los números pares de una lista.

lista_par = list(filter(lambda x:x%2==0, lista_1_20))# O(1)
print(lista_par)
#Big O: O(1)
#16. Usa map para crear una lista con las longitudes de cada palabra en una frase.
long_frase = list(map(lambda x: len(x),lista_n_cuadrado))# O(1)
print(long_frase)
#Big O: O(1)
#17. Combina filter y map para convertir a mayúsculas las palabras que tengan más de 3 letras en 
# una lista de palabras.
lista_pa = ['ana','pedro','pe','a','m','che']# O(1)
lista_filt = list(map(lambda x: x.upper(), filter(lambda x: len(x) > 3, lista_pa)))# O(1)
print(lista_filt)
#Big O: O(1)
#18. Escribe una función recursiva que calcule el factorial de un número.
def factorial(x):
    if x == 1:  # O(1)
        return 1
    else:
        x * factorial(x - 1)    # O(n)
print(factorial(5))
#Big O: O(n)
#19. Implementa una función recursiva que cuente el número de dígitos de un número entero.
def contar_digitos(n):
    if abs(n) < 10: # O(1)
        return 1
    else:
        return 1 + contar_digitos(n // 10)  # O(n)

print(contar_digitos(12323412))
#Big O: O(n)
#20. Desarrolla una función recursiva que retorne la suma de los dígitos de un número.
def suma_digitos(x):
    if x < 10:  # O(1)
        return x
    else:
        return (x % 10) + suma_digitos(x // 10) # O(n)

print(suma_digitos(123))
#Big O: O(n)
#21. Crea una función recursiva que verifique si un string es un palíndromo
def palindromo(x):
    if len(x) <= 1:     # O(1)
        return True
    elif x[0] == x[-1]:     # O(1)
        return palindromo(x[1:-1])      # O(n)
    else:
        return False
    
print(palindromo('ana'))
#Big O: O(n)
#22. Escribe una función recursiva que genere el reverso de una lista.
def reverse(lista):
    if len(lista)==0:   # O(1)
        return []
    else:
        return [lista[-1]] + reverse(lista[:-1])    # O(n)
print(reverse([1,2,3,4,5]))
#Big O: O(n)
##23. Implementa una función recursiva que sume los números de 0 a n
def suma_recursiva(n):
    if n == 0:  # O(1)
        return 0
    else: 
        return n + suma_recursiva(n-1) # O(n)
print(suma_recursiva(12345))
#Big O: O(n)
#24. Crea una función recursiva que encuentre el enésimo número de Fibonacci.
def fibonacci(x):
    if x==0:    # O(1)
        return 0
    elif x==1:  # O(1)
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)  # O(2^n)
print(fibonacci(6))
#Big O: O(2^n)
#25. Desarrolla una función recursiva que invierta un string.
def invertir_string(s):
    if len(s) == 0: # O(1)
        return s
    else:
        return s[-1] + invertir_string(s[:-1])# O(n)
    
print(invertir_string('pedro'))
#Big O: O(n)
