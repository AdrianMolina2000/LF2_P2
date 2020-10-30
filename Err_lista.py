import re, os

class Error:
    def __init__(self, tip, f):
        self.tipo = tip
        self.fila = f

def report(tokis):
    file_name = open("Reporte/Tokens_lista.html", "w")

    file_name.write("<!DOCTYPE html>\n<html>\n<head>\n")
    file_name.write("   <meta charset='UTF-8'>\n")
    file_name.write("   <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'>\n")
    file_name.write("</head>\n")
    file_name.write("<body class='container grey lighten-1'>\n")
    file_name.write("   <table class='highlight'>\n")
    file_name.write("       <thead>\n")
    file_name.write("           <tr>\n")
    file_name.write("               <th>No.</th>\n")
    file_name.write("               <th>Fila</th>\n")
    file_name.write("               <th>Tipo</th>\n")
    file_name.write("           </tr>\n")
    file_name.write("       </thead>\n")
    file_name.write("       <tbody>\n")
    
    num = 1
    for toke in tokis:
        file_name.write("           <tr>\n")
        file_name.write(f"                <th><strong>{num}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.fila}</strong></th>\n")
        file_name.write(f"                <th><strong>{toke.tipo}</strong></th>\n")
        file_name.write("           </tr>\n")
        num +=1

    file_name.write("       </tbody>\n")
    file_name.write("   </table>\n")
    file_name.write("</body>\n</html>\n")

    file_name.close()
    os.startfile("Reporte\Errores_lista.html")

#PATRONES
pattern_lista = r"[L|l][I|i][S|s][T|t][A|a]\s*\(.*,.*,.*\)\{"
pattern_nodos = r"[N|n][O|o][D|d][O|o][S|s]\s*\(.*,.*\)\s*.*;"
pattern_nodo = r"[N|n][O|o][D|d][O|o]\s*\(.*\).*;"
pattern_defecto = r"\}\s*[D|d][E|e][F|f][E|e][C|c][T|t][O|o]\s*\(.*\).*"


def analizar_archivo_tokens(path):

    tokens = []

    
    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        n_linea = 1

        estadoAntes = "inicio"
        estadoActual = "inicio"
        for linea in lineas:
            #Lista
            if re.search(r"[L|l][I|i][S|s][T|t][A|a]", linea):
                estadoActual = "lista"
                print(estadoActual)
                # error = Error("Estructura Desconocida", n_linea)
                # tokens.append(error)
                # print(error.fila, error.tipo)
            


            n_linea += 1

    # report(tokens)

analizar_archivo_tokens("Listas.lfp")