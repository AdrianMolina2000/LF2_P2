import re, os
from diccionarios import *

class Error:
    def __init__(self, err, tip, f, c):
        self.error = err
        self.tipo = tip
        self.fila = f
        self.columna = c

def report(tokis):
    file_name = open("Reporte/Errores_lista.html", "w")

    file_name.write("<!DOCTYPE html>\n<html>\n<head>\n")
    file_name.write("   <meta charset='UTF-8'>\n")
    file_name.write("   <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'>\n")
    file_name.write("</head>\n")
    file_name.write("<body class='container grey lighten-1'>\n")
    file_name.write("<h2>ERRORES</h2>\n")
    file_name.write("   <table class='highlight'>\n")
    file_name.write("       <thead>\n")
    file_name.write("           <tr>\n")
    file_name.write("               <th>No.</th>\n")
    file_name.write("               <th>Fila</th>\n")
    file_name.write("               <th>Columna</th>\n")
    file_name.write("               <th>Error</th>\n")
    file_name.write("               <th>Descripcion</th>\n")
    file_name.write("           </tr>\n")
    file_name.write("       </thead>\n")
    file_name.write("       <tbody>\n")
    
    num = 1
    for toke in tokis:
        file_name.write("           <tr>\n")
        file_name.write(f"                <th><strong>{num}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.fila}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.columna}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.error}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.tipo}</strong></th>\n")
        file_name.write("           </tr>\n")
        num +=1

    file_name.write("       </tbody>\n")
    file_name.write("   </table>\n")
    file_name.write("</body>\n</html>\n")

    file_name.close()
    # os.startfile("Reporte\Errores_lista.html")

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

def analizar_matriz_Errores(path):

    errores = []

    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        n_linea = 1
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

                #Error forma
                if separados[3].lower() in formas.keys():
                    p = 2
                else:
                    errores.append(Error(separados[3], "Forma Desconocida", n_linea, (re.search(separados[3], i).start()+1)))

                #Error doble
                if separados[4].lower() == "verdadero" or  separados[4].lower() == "falso":
                    p = 2
                else:
                    errores.append(Error(separados[4], "Valor Desconocido", n_linea, (re.search(separados[4], i).start()+1)))


            elif re.search(pattern_fila, i):
                separado2 = re.findall(r"\).*",i)
                separados2 = separado2[0].replace(")"," ")
                separados2 = separados2.replace(";","")
                separados2 = separados2.replace(" ","")

                #Error Color
                if separados2 == "#":
                    p = 2
                elif separados2.lower() in colores.keys():
                    p = 2
                else:
                    errores.append(Error(separados2, "Color Desconocido", n_linea, (re.search(separados2, i).start()+1)))

            elif re.search(pattern_nodo, i):
                separado = re.findall(r"\(.*,.*,.*\).*;",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")",",")
                separados = separados.replace(";","")

                separados = re.split(r",",separados)
                separados[3] = separados[3].replace(" ","")

                #Error Color
                if separados[3] == "#":
                    p = 2
                elif separados[3].lower() in colores.keys():
                    p = 2
                else:
                    errores.append(Error(separados[3], "Color Desconocido", n_linea, (re.search(separados[3], i).start()+1)))
    
            elif re.search(pattern_defecto, i):
                separado = re.findall(r"\(.*\).*",i)
                separados = separado[0].replace("(","")
                separados = separados.replace(")",",")
                separados = separados.replace(";","")

                separados = re.split(r",",separados)
                separados[0] = separados[0].replace("'","")
                separados[0] = separados[0].replace(" ","")
                separados[1] = separados[1].replace(" ","")

                #Error Color
                if separados[1].lower() in colores.keys():
                    p = 2
                else:
                    errores.append(Error(separados[1], "Color Desconocido", n_linea, (re.search(separados[1], i).start()+1)))

            n_linea += 1
    report(errores)

# analizar_matriz_Errores("Matriz.lfp")