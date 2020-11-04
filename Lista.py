import re
from mapa import graficar_lista

class nodo:
    def __init__(self, n, c):
        self.nombre = n
        self.color = c


pattern_lista = r"\s*[L|l][I|i][S|s][T|t][A|a]\s*\(.*,.*,.*\)\{"
pattern_nodos = r"[N|n][O|o][D|d][O|o][S|s]\s*\(.*,.*\)\s*.*;"
pattern_nodo = r"[N|n][O|o][D|d][O|o]\s*\(.*\).*;"
pattern_defecto = r"\}\s*[D|d][E|e][F|f][E|e][C|c][T|t][O|o]\s*\(.*\).*"

propiedades = {
    'nombre_lista' : '',
    'forma_nodo' : '',
    'lista_doble': ''
}

nodos = []

def leer_archivo_lista(path):   
    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        estadoPadre = "Nada"
        for i in lineas:
            if re.search(pattern_lista, i):
                estadoPadre = "Lista"
                separado = re.findall(r"\(.*,.*,.*\)",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")","")
                separados = re.split(r",",separados)
                separados[0] = separados[0].replace("'","")
                separados[1] = separados[1].replace(" ","")
                separados[2] = separados[2].replace(" ","")

                #Asignar Variables al diccionario
                propiedades['nombre_lista'] = separados[0]
                propiedades['forma_nodo'] = separados[1]
                propiedades['lista_doble'] = separados[2]

            elif re.search(pattern_nodos, i) and estadoPadre == "Lista":
                separado = re.findall(r"\([0-9]*,.*\).*",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")",",")
                separados = separados.replace(";","")

                separados = re.split(r",",separados)
                separados[0] = separados[0].replace(" ","")
                separados[1] = separados[1].replace("'","")
                separados[1] = separados[1].replace(" ","")
                separados[2] = separados[2].replace(" ","")

                for i in range(int(separados[0])):
                    nodos.append(nodo(separados[1], separados[2]))
            
            elif re.search(pattern_nodo, i) and estadoPadre == "Lista":
                separado = re.findall(r"\(.*\).*;",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")",",")
                separados = separados.replace(";","")

                separados = re.split(r",",separados)
                separados[0] = separados[0].replace("'","")
                separados[0] = separados[0].replace(" ","")
                separados[1] = separados[1].replace(" ","")

                nodos.append(nodo(separados[0], separados[1]))
    
            elif re.search(pattern_defecto, i) and estadoPadre == "Lista":
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
                    if nod.color == "#":
                        nod.color = separados[1]
            if estadoPadre == "Lista":
                lista = (propiedades, nodos)
    
    graficar_lista(lista)
                
# leer_archivo_lista("Listas.lfp")

