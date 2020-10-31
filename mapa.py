from graphviz import Digraph
from diccionarios import *

def graficar_lista(lista):
    propiedades = lista[0]
    nodos = lista[1]


    t = Digraph('Ruta', filename='Ruta', format="svg", directory="Reporte/")

    

    index = 0

    #GRAFICAR NODOS
    for nod in nodos:
        index +=1

        t.attr('node', shape=formas[propiedades["forma_nodo"]], fixedsize='true', width="1", color="black", style="filled", fillcolor=colores[nod.color])
        
        t.node(f"nodo{index}", label=nod.nombre)

    #GRAFICAR FLECHAS
    index = 0
    for i in range(len(nodos)):
        index +=1
        if (i+1) < len(nodos) :
            t.edge(f"nodo{index}", f"nodo{index+1}")

    
    #GRAFICAR FLECHAS DOBLES
    if propiedades["lista_doble"] == "verdadero":
        index = 0
        for i in range(len(nodos)):
            index +=1
            if (i+1) < len(nodos) :
                t.edge(f"nodo{index+1}", f"nodo{index}")


    #penwidth = "5"
    t.attr(overlap='false')
    t.attr(label= propiedades["nombre_lista"])
    t.attr(fontsize='20')
    t.attr(rankdir="LR")

    # t.view()
    t.render()





def graficar_matriz(lista):
    propiedades = lista[0]
    mat = lista[1]

    t = Digraph('Ruta', filename='Ruta', format="svg", directory="Reporte/")
    # t = Digraph('Ruta', filename='Ruta', format="png", directory="Reporte/")

    index = 0

    #GRAFICAR NODOS
    for i in range(0,int(propiedades["columna"])):
        for j in range(0, int(propiedades["fila"])):
            t.attr('node', shape=formas[propiedades["forma_nodo"]], fixedsize='true', width="1", color="black", style="filled", fillcolor=colores[mat[i][j].color])
            t.node(f"nodo{i,j}", label=mat[i][j].nombre)
    
    #GRAFICAR FLECHAS
    for i in range(0,int(propiedades["columna"])):
        for j in range(0, int(propiedades["fila"])):

            if (i+1) < int(propiedades["columna"]):
                t.edge(f"nodo{i,j}", f"nodo{i+1,j}")

            # if (j+1) < int(propiedades["fila"]):
                # t.edge(f"nodo{i,j}", f"nodo{i,j+1}")

    
    #GRAFICAR FLECHAS DOBLES
    if propiedades["matriz_doble"] == "verdadero":
        for i in range(0,int(propiedades["columna"])):
            for j in range(0, int(propiedades["fila"])):

                if (i+1) < int(propiedades["columna"]):
                    t.edge(f"nodo{i+1,j}", f"nodo{i,j}")

                # if (j+1) < int(propiedades["fila"]):
                    # t.edge(f"nodo{i,j+1}", f"nodo{i,j}")


    #penwidth = "5"
    t.attr(overlap='false')
    t.attr(label= propiedades["nombre_matriz"])
    t.attr(fontsize='20')
    # t.attr(rankdir="LR")
    # t.view()
    t.render()




def devolver(cont, color):
    dato = ""

    for i in cont:
        dato += f"<TD bgcolor='{color}'>{i}</TD>"
    
    return dato


def graficar_tabla(lista):
# def graficar_tabla():
    propiedades = lista[0]
    encabezados = lista[1]
    filas = lista[2]

    s = Digraph('Ruta', filename='Ruta', format="png", directory="Reporte/", node_attr={'shape': 'plaintext'})
    # t = Digraph('Ruta', filename='Ruta', format="svg", directory="Reporte/")

    titulos = list(map(lambda x: devolver(x.contenido, colores[x.color.lower()]), encabezados))

    filo2 = list(map(lambda x: devolver(x.contenido, colores[x.color.lower()]), filas))
    tablita = list(map(lambda x: f"<TR>{x}</TR>", filo2))


    s.node('struct1', f'''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        {titulos}
    </TR>
    {tablita}
    </TABLE>>''')

    s.attr(overlap='false')
    s.attr(label= propiedades["nombre_tabla"])
    s.attr(fontsize='20')
    s.view()
    # s.render()
