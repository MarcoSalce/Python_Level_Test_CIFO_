# EJERCICIO 1 #
def factorial(nume):
    factorial = 1
    for element in range(1,nume+1):
        factorial = factorial*element
    return factorial

nume=int(input("Ingresa numeros: "))
lista = []   
while nume!=0:
    print(f"El factorial de: {nume} es {factorial(nume)}")
    print(f"La cantidad de numeros leidos es: {len(lista)}")
    nume=int(input("Ingresa numeros: "))
    if nume !=0:
        lista.append(nume)

## EJERCICIO 2 ##
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

nume=int(input("Ingresa numeros: ")) 
while nume!=0:
    print(f"La suma de los digitos de: {nume} es {sumaDigitos(nume)}")
    nume=int(input("Ingresa numeros: "))

### EJERCICIO 3 ###
def ultimalen(oracion):
    longi = 0
    new = oracion.strip()
    for element in range(len(new)):
        if new[element] == " ":
            longi = 0
        else:
            longi += 1
    return longi
 
cadena = "  Tinc tnta  son que a les cinc tinc son  "
print(f"La longitud de la ultima palabra es: {ultimalen(cadena)}")

#### EJERCICIO 4 ####
def maxim(numeros):
    valor_max = 0
    for nume in lista:
        if nume > valor_max:
            valor_max = nume
    return valor_max

lista = [7,3,8]
print(f"El valor maximo de la lista es: {maxim(lista)}")

##### EJERCICIO 5 #####
def dinsrang(numero, rango1, rango2):
    return numero in range(rango1,rango2)

print(dinsrang(3,2,5))
print(dinsrang(5,2,3))

###### EJERCICIO 6 ######
def aparicions(cadena):
    cadena = cadena.replace(',','').replace(' ','')
    indice = 0
    mayus = 0
    minus = 0
    while indice < len(cadena):
        letra = cadena[indice]
        if letra.isupper() == True:
            mayus +=1
        else:
            minus +=1
        indice += 1
    return f"La cadena tiene {mayus} mayusculas y {minus} minusculas"

cadena = "Hola Caracola, a tu bola"
print(aparicions(cadena))

####### EJERCICIO 7 #######
def perfecte(numero):
    suma = 0
    for element in range(1,numero):
        if (numero % element == 0):
            suma += element
    if numero == suma:
        return True
    else:
        return False

num = int(input("introduzca un numero:"))
if perfecte(num):
    print(perfecte(num))
else:
    print(perfecte(num))

######## EJERCICIO 8 ########
def pangrama(cadena): 
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for element in alfabeto: 
        if element not in cadena.lower(): 
            return False
    return True

cadena = "The quick brown fox jumps over the lazy dog"
print(pangrama(cadena))
cadena_1 = 'Aquesta no es pangrama'
print(pangrama(cadena_1))
