import re
from mapa import graficar_tabla

class fila:
    def __init__(self, cont, c):
        self.contenido = cont
        self.color = c


pattern_tabla = r"[T|t][A|a][B|b][L|l][A|a]\s*\(.*,.*\)\{"
pattern_fila = r"[F|f][I|i][L|l][A|a]\s*\(.*\).*;"
pattern_encabezado = r"[E|e][N|n][C|c][A|a][B|b][E|e][Z|z][A|a][D|d][O|o][S|s]\s*\(.*\).*;"
pattern_defecto = r"\}\s*[D|d][E|e][F|f][E|e][C|c][T|t][O|o]\s*\(.*\).*"

propiedades = {
    'columna' : '',
    'nombre_tabla' : '',
}

filas = []
encabezados = []

nombre_def = ""
color_def = ""
def leer_archivo_matriz(path):   
    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        num_fila = 0
        estado = ""
        for i in lineas:
            if re.search(pattern_tabla, i):
                separado = re.findall(r"\(.*,.*\)",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")","")
                separados = re.split(r",",separados)
                separados[0] = separados[0].replace(" ","")
                separados[1] = separados[1].replace("'","")
                separados[1] = separados[1].replace(" ","")

                #Asignar Variables al diccionario
                propiedades['columna'] = separados[0]
                propiedades['nombre_tabla'] = separados[1]

            elif re.search(pattern_fila, i):
                separado2 = re.findall(r"\).*;",i)
                separados2 = separado2[0].replace(")"," ")
                separados2 = separados2.replace(";","")
                separados2 = separados2.replace(" ","")

                separado = re.findall(r"\(.*\)",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")","")
                separados = separados.replace(";","")
                separados = separados.replace(" ","")

                separados = re.split(r",",separados)
                contenido = []
                for nom in separados:
                    nom = nom.replace("'", "")
                    nom = nom.replace(" ", "")
                    contenido.append(nom)
                
                filas.append(fila(contenido, separados2))

            elif re.search(pattern_encabezado, i):
                separado2 = re.findall(r"\).*;",i)
                separados2 = separado2[0].replace(")"," ")
                separados2 = separados2.replace(";","")
                separados2 = separados2.replace(" ","")

                separado = re.findall(r"\(.*\)",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")","")
                separados = separados.replace(";","")
                separados = separados.replace(" ","")

                separados = re.split(r",",separados)
                contenido = []
                for nom in separados:
                    nom = nom.replace("'", "")
                    nom = nom.replace(" ", "")
                    contenido.append(nom)

                encabezados.append(fila(contenido, separados2))

    
            elif re.search(pattern_defecto, i):
                separado = re.findall(r"\(.*\).*",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")",",")
                separados = separados.replace(";","")

                separados = re.split(r",",separados)
                separados[0] = separados[0].replace("'","")
                separados[0] = separados[0].replace(" ","")
                separados[1] = separados[1].replace(" ","")

                for nod in filas:
                    if nod.color == "#":
                        nod.color = separados[1]

                    for i in range(0,len(nod.contenido)):
                        if nod.contenido[i] == '#':
                            nod.contenido[i] = separados[0]
                
                for nod in filas:
                    while len(nod.contenido) <= int(propiedades["columna"])-1:
                        nod.contenido.append(separados[0])

                #Encabezados
                for nod in encabezados:
                    if nod.color == "#":
                        nod.color = separados[1]

                    for i in range(0,len(nod.contenido)):
                        if nod.contenido[i] == '#':
                            nod.contenido[i] = separados[0]
                
                for nod in encabezados:
                    while len(nod.contenido) <= int(propiedades["columna"])-1:
                        nod.contenido.append(separados[0])                
        
        tabla = (propiedades, encabezados, filas)


    graficar_tabla(tabla)
                
leer_archivo_matriz("Tabla.lfp")