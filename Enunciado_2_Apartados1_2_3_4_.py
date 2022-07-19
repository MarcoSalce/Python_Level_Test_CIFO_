import io
import stopwords_final #Apartado_2_B: Import stopwords_final de la lista 'prohibidos'

class Frase: 
    def __init__(self, text):
        self.text = text
    
    def minuscules(self):
        """ Convierte una frase en minusculas"""
        self.text = self.text.lower()
        
    def limpiafrase(self):
        """ Sustituye los caracteres de la frase que no sean letras o espacios 
        por espacios """
        for letra in self.text:
            if letra not in 'áéíóúabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':  #Apartado_2_A: Agregar 'áéíóú'
               self.text = self.text.replace(letra," ")
           
    def listapalabras(self):
        """ Convierta la frase en una lista de palabras"""
        lista_2 = []
        lista = self.text.split()
        for palabra in lista:
            if not palabra in stopwords_final.prohibides: #Apartado_2_C: Excluir las palabras que hay en la lista 'prohibidas'
                lista_2.append(palabra)
        return lista_2
    
    def setpalabras(self):
        """ Obtiene un set con las palabras distintas"""
        return set(self.listapalabras())
       
    def getfrase(self): 
        """Pregunta que frase quieres convertir en objeto"""    
        self.text = input("")
  
    def __str__(self):
        """ Describe el objeto"""
        return f"La cadena es {self.text}"


llibre = io.open("document.txt","r", encoding = 'utf-8')
linies = llibre.readlines()
llibre.close()

listafinal =[]
conjuntofinal = set()
f1 = Frase("")
for frase in linies:
    f1.text = frase
    f1.limpiafrase()
    f1.minuscules()
    listafinal += f1.listapalabras()
    conjuntofinal.update(f1.setpalabras())

diccionario = {}
salida = io.open("resultat.txt","a")
for word in conjuntofinal:
    diccionario[word] = listafinal.count(word)
for palabra in diccionario.keys():
    if diccionario[palabra] > 50:
        salida.write(palabra +'\n')

sortida_ordenada = sorted(diccionario.items(), key=lambda x: x[1], reverse = True) #Apartado_3_A: Lo que hace este codigo es ordenar los elementos del diccionario de mayor a menor
salida_sortida = io.open("resultado_sortida.txt","a")
for tupla in sortida_ordenada:
    salida_sortida.write(str(tupla) + '\n')
salida_sortida.close() #Apartado_3_B: La salida de 'sortida_ordenada' te da un fichero en formato txt, donde te muestra una lista de elementos, donde esta la palabra con su mayor ocurrencia



#Apartado_4_A: En mi caso yo imprimi otro archivo para evitar confuciones con respecto al anterior por lo que no reemplace resultat.txt
salida_sortida = io.open("resultado_sortida.txt","r")
linies = salida_sortida.readlines()
lista_3 = []
contador = 1
while contador <= 40:
    lista_3.append(linies[contador])
    contador += 1
salida_sortida.close() #Apartado_4_B: Para cada valor que se ha generado en 'salida_sortida' se imprime las 40 primeras palabras


print(lista_3) #Comprobacion de lista_3
print(sortida_ordenada) #Comprobacion de salida 'sortida_ordenada'
print("guarde los resultados en resultat.txt")
salida.close()        





