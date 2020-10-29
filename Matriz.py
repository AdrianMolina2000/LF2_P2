import re
from mapa import graficar_lista, graficar_matriz

class nodo:
    def __init__(self, x, y, n, c):
        self.columna = x
        self.fila = y
        self.nombre = n
        self.color = c


pattern_matriz = r"[M|m][A|a][T|t][R|r][I|i][Z|z]\s*\(.*,.*,.*,.*,.*\)\{"
pattern_fila = r"[F|f][I|i][L|l][A|a]\s*\(.*\)\s*.*;"
pattern_nodo = r"[N|n][O|o][D|d][O|o]\s*\(.*,.*,.*\).*;"
pattern_defecto = r"\}\s*[D|d][E|e][F|f][E|e][C|c][T|t][O|o]\s*\(.*\).*"

propiedades = {
    'fila' : '',
    'columna' : '',
    'nombre_matriz' : '',
    'forma_nodo' : '',
    'matriz_doble': '',
}

nodos = []
nombre_def = ""
color_def = ""
def leer_archivo_matriz(path):   
    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        num_fila = 0
        estado = ""
        for i in lineas:
            if re.search(pattern_matriz, i):
                separado = re.findall(r"\(.*,.*,.*,.*,.*\)",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")","")
                separados = re.split(r",",separados)
                separados[0] = separados[0].replace(" ","")
                separados[1] = separados[1].replace(" ","")
                separados[2] = separados[2].replace("'","")
                separados[2] = separados[2].replace(" ","")
                separados[3] = separados[3].replace(" ","")
                separados[4] = separados[4].replace(" ","")

                #Asignar Variables al diccionario
                propiedades['fila'] = separados[0]
                propiedades['columna'] = separados[1]
                propiedades['nombre_matriz'] = separados[2]
                propiedades['forma_nodo'] = separados[3]
                propiedades['matriz_doble'] = separados[4]

            elif re.search(pattern_fila, i):
                separado2 = re.findall(r"\).*",i)
                separados2 = separado2[0].replace(")"," ")
                separados2 = separados2.replace(";","")
                separados2 = separados2.replace(" ","")

                separado = re.findall(r"\(.*\)",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")","")
                separados = separados.replace(";","")
                separados = separados.replace(" ","")

                separados = re.split(r",",separados)
                num = 0
                for nom in separados:
                    nom = nom.replace("'", "")
                    nom = nom.replace(" ", "")
                    nodos.append(nodo(num, num_fila, nom, separados2))
                    num = num+1 

                num_fila = num_fila + 1

            elif re.search(pattern_nodo, i):
                separado = re.findall(r"\(.*,.*,.*\).*;",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")",",")
                separados = separados.replace(";","")

                separados = re.split(r",",separados)
                separados[0] = separados[0].replace(" ","")
                separados[1] = separados[1].replace(" ","")
                separados[2] = separados[2].replace("'","")
                separados[2] = separados[2].replace(" ","")
                separados[3] = separados[3].replace(" ","")

                nodos.append(nodo(int(separados[0])-1, int(separados[1])-1, separados[2], separados[3]))
    
            elif re.search(pattern_defecto, i):
                separado = re.findall(r"\(.*\).*",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")",",")
                separados = separados.replace(";","")

                separados = re.split(r",",separados)
                separados[0] = separados[0].replace("'","")
                separados[0] = separados[0].replace(" ","")
                separados[1] = separados[1].replace(" ","")

                for nod in nodos:
                    if nod.nombre == "#":
                        nod.nombre = separados[0]
                        nombre_def = separados[0]
                    if nod.color == "#":
                        nod.color = separados[1]
                        color_def = separados[1]
        
        mat = []
        for i in range(0,int(propiedades["columna"])):
            mat.append([])
            for j in range(0, int(propiedades["fila"])):
                mat[i].append(nodo(str(j),str(i),nombre_def, color_def))
        
        for i in range(0,int(propiedades["columna"])):
            for j in range(0, int(propiedades["fila"])):
                for k in nodos:
                    if mat[i][j].fila == str(int(k.fila)) and mat[i][j].columna == str(int(k.columna)):
                        mat[i][j] = k
        
        # for i in range(0,int(propiedades["columna"])):
        #     for j in range(0, int(propiedades["fila"])):
        #         print(mat[i][j].fila, mat[i][j].columna,mat[i][j].nombre, mat[i][j].color)
        
        # print(mat)

        
        matriz = (propiedades, mat)

        # for i in nodos:
        #     print(i.nombre, i.color, i.columna, i.fila)

    graficar_matriz(matriz)
                
leer_archivo_matriz("Matriz.lfp")