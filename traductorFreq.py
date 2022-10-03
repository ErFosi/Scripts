

def traducir():
    nombreFch = input("Inserte el nombre del archivo:") #insertar la direccion con el archivo
    f=open(nombreFch)
    freq_ord=["E","A","O","L","S","N","D","R","U","I","T","C","P","M","Y","Q","B","H","G","F","V","J","Ñ","Z","X","K","W"]
    freq_dic={"E":0.1678,"A":0.1196,"O":0.0869,"L":0.0837,"S":0.0788,"N":0.0701,"D":0.0687,"R":0.0494,"U":0.048,"I":0.0415,"T":0.0331,"C":0.0292,"P":0.02776,"M":0.0212,"Y":0.0154,"Q":0.0153,"B":0.0092,"H":0.0089,"G":0.0073,"F":0.0052,"V":0.0039,"J":0.003,"Ñ":0.0029,"Z":0.0015,"X":0.006,"K":0,"W":0}
    alfabeto_dic={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"Ñ":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
    alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    cont=0
    for i in f:
        for char in i:
            if char in alfabeto_dic:            #Por cada char añadir uno en el diccionario
                if char.islower():
                    char=char.Upper()
                cont=cont+1
                alfabeto_dic[char]=alfabeto_dic[char]+1

    for clave in alfabeto_dic:
        alfabeto_dic[clave]=alfabeto_dic[clave]/cont        #Pasar de contador a frecencia
        alfabetoTrad=alfabeto_dic

    i=0;
    alfabeto_dic=dict(reversed(sorted(alfabeto_dic.items(), key=lambda item: item[1])))     #Ordenar de mayor a menor freq
    print(alfabeto_dic)
    alfabetoTrad=alfabeto_dic
    for clave in alfabetoTrad:
        alfabetoTrad[clave]=freq_ord[i]                 #Crear el traductor recorriendo por orden el cifrado
        i=i+1
    print("El fichero tiene:"+str(cont)+" letras")
    print("Las frecuencias son las siguientes:")
    print(freq_ord)
    print("El alfabeto traductor aproximado es el siguiente a falta de comprobar y ajustar:")
    print(alfabetoTrad)
    #RESULTADO
    alfabetoTrad={'X': 'E', 'E': 'A', 'K': 'O', 'I': 'L', 'C': 'S', 'J': 'N', 'T': 'D', 'A': 'R', 'R': 'U', 'Z': 'I', 'N': 'T', 'H': 'C', 'P': 'P', 'D': 'M', 'Q': 'Y', 'O': 'Q', 'V': 'B', 'S': 'H', 'G': 'G', 'U': 'F', 'M': 'V', 'L': 'J', 'F': 'Ñ', 'Y': 'Z', 'W': 'X', 'Ñ': 'K', 'B': 'W'}
    #SE MODIFICA PARA AJUSTARLO A LA RESPUESTA
    alfabetoTrad={'X': 'E', 'E': 'A', 'K': 'R', 'I': 'O', 'C': 'I', 'J': 'N', 'T': 'L', 'A': 'D', 'R': 'C', 'Z': 'U', 'N': 'S', 'H': 'T', 'P': 'M', 'D': 'P', 'Q': 'B', 'O': 'F', 'V': 'V', 'S': 'Q', 'G': 'J', 'U': 'G', 'M': 'Y', 'L': 'Z', 'F': 'Ñ', 'Y': 'H', 'W': 'X', 'Ñ': 'K', 'B': 'W'}
    f=open(nombreFch)
    print("El texto traducido es el siguiente:\n")
    for linea in f:  #traducir e imprimir
        lane = ""
        for char in linea:
            if char in alfabetoTrad:
                lane=lane+(alfabetoTrad[char])
            else:
                lane=lane+(char)
        print(lane)

if __name__ == '__main__':
    traducir()

