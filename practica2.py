def leer_texto(entrada):
    texto=""
    lineas = entrada.readlines()
    for linea in lineas:
        texto=texto+linea.strip('\n')
    
    return texto

def preprocesado(texto):
    aux=texto.upper()
    respuesta=""
    for i in aux:
        if(i!=',' and i!=';' and i!='?' and i!='¿' and i!='!' and i!='¡' and i!='(' and i!=')' and i!='"' and i!=':' and i!='.' ):
            respuesta=respuesta+i
    return respuesta

def intercambiar(datos):
    datos=datos.lower()
    aux=""
    for i in datos:
        for j in i:
            if(j=='á'):
                aux=aux+'a'
            else:
                if(j=='é'):
                    aux=aux+'e'
                else:
                    if(j=='í'):
                        aux=aux+'i'
                    else:
                        if(j=='ó'):
                            aux=aux+'o'
                        else:
                            if(j=='ú'):
                                aux=aux+'u'
                            else:
                                if(j!=' '):
                                    aux=aux+j
    return aux


def Vignere(palabras,clave,modulo):
    Letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Codigo=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    dicc = dict(zip(Letras, Codigo))

    clave=clave.upper()
    cifrado=""
    for i in palabras:
        aux=i
        aux2=clave*(len(i)//len(clave)+1)
        for j in range(len(aux)):
            #a1=ord(aux[j])-65
            #a2=ord(aux2[j])-65
            #a3=(a1+a2)%modulo+65
            #cifrado=cifrado+chr(a3)
            
            a1=dicc[aux[j]]
            a2=dicc[aux2[j]]
            a3=(a1+a2)%modulo
            cifrado=cifrado+Letras[a3]                        
            
        #cifrado=cifrado+" "
    
    return cifrado

def nuevaClave(clave , longitud):
    key=""
    j=0
    i=0
    for i in range(longitud):
        if i>0 and(i%len(clave)==0):
            j=0
        key=key+clave[j]
        j=j+1
    return key

def Vignere191(mensaje,clave,modulo):
    cifrado=""
    mensaje=texto.replace(" ","")
    key=nuevaClave(clave,len(mensaje))
    c=0
    i=0
    n=0
    for i in mensaje:
        c=((ord(i)+ord(key[n])))%(int(modulo))
        cifrado=cifrado+chr(c)
        n=n+1
    return cifrado

def Autoclave(palabras,clave,modulo):
    Letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Codigo=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    dicc = dict(zip(Letras, Codigo))

    clave=clave.upper()
    cifrado=""
    for i in palabras:
        aux=i
        aux2=clave+i*(len(i)//len(clave))
        for j in range(len(aux)):
            #a1=ord(aux[j])-65
            #a2=ord(aux2[j])-65
            #a3=(a1+a2)%modulo+65
            #cifrado=cifrado+chr(a3)
            
            a1=dicc[aux[j]]
            a2=dicc[aux2[j]]
            a3=(a1+a2)%modulo
            cifrado=cifrado+Letras[a3]                        
            
        #cifrado=cifrado+" "
    
    return cifrado

def VignereReverso(palabras,clave,modulo):
    Letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Codigo=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    dicc = dict(zip(Letras, Codigo))

    clave=clave.upper()
    cifrado=""
    for i in palabras:
        aux=i
        aux2=clave*(len(i)//len(clave)+1)
        for j in range(len(aux)):
            #a1=ord(aux[j])-65
            #a2=ord(aux2[j])-65
            #a3=(a1+a2)%modulo+65
            #cifrado=cifrado+chr(a3)
            
            a1=dicc[aux[j]]
            a2=dicc[aux2[j]]
            #print(str(a1)+" "+aux2[j])
            a3=(a1-a2)%modulo
            cifrado=cifrado+Letras[a3]                        
            
        #cifrado=cifrado+" "
    
    return cifrado


def triagramas(texto):
    triagramas = []
    #separamos en grupos de 3
    for indice, c in enumerate(texto):
      if (indice == len(texto)-3):
        break
      sequencia = texto[indice] + texto[indice+1] + texto[indice+2]
      triagramas.append(sequencia)
    
    #contamos las veces que se repite cada triagrama
    frecTriang = {}
    for trigram in triagramas:
      frecTriang[trigram] = texto.count(trigram)
    
    #armamos un diccionario con las frecuencias ordenadas  
    frecTriang = {k: v for k, v in sorted(frecTriang.items(), key=lambda item: item[1], reverse=True)}
    
    frec_triang = {}
    
    #imprimimos los 15 traiagrams con mas frecuencia
    i = 0
    for k, v in frecTriang.items():
      if i == 15:
        break
      frec_triang[k] = v
      print(k, v)
      i += 1
    return frec_triang

def frecuencias(texto,frec_triang):
    frec_triang_indice = {}
    #creamos un diccionario con los indices
    for k in frec_triang.keys():
      frec_triang_indice[k] = [i for i in range(len(texto)) if texto.startswith(k, i)]
    
    #creamos un diccionario con los delta
    frec_triang_deltas = {}
    for k, v in frec_triang_indice.items():
      t = []
      for i in range(len(frec_triang_indice[k])-1):
        t.append(frec_triang_indice[k][i+1]-frec_triang_indice[k][i])
      frec_triang_deltas[k] = t
    print(frec_triang_indice)
    print("")
    print(frec_triang_deltas)


entrada = open("texto.txt", "r",encoding='utf8')

texto=leer_texto(entrada)

print("Datos Iniciales: ")
print(texto)
print("")
#print("Palabras: ")
palabras=preprocesado(intercambiar(texto)).split(" ")
#print(palabras)

modulo=27
clave="positivo"
print("Cifrado Vigenere 27: ")
m=Vignere(palabras,clave,modulo)
print(m)
print("")
print("Descifrado Vigenere 27: ")
mm=VignereReverso([m],clave,modulo)
print("")
#modulo=191
#clave="positivo"
#f=open("texto.txt","r",encoding='utf8')
#texto=f.read()
#print("Cifrado Vigenere 191: ")
#m=Vignere191(palabras,clave,modulo)
#f.close()
#print(m)


modulo=27
clave="HIELO"
texto2=["WPIXHVYYOSRTECSZBEEGHUUFWRWTZGRWUFSRIWESSXVOHAIHOHWWHCWHUZOBOZEAOYBMCRLTEYOTI"]
mm=VignereReverso(texto2,clave,modulo)
print(mm)
print("")

#print("")
#n=Autoclave(palabras,clave,modulo)
#print(n)
#print("")
#print("Los triagramas son: ")
#frec_triang=triagramas(m)
#print("")
#print("Las frecuencias son: ")
#frecuencias(m,frec_triang)


entrada.close()