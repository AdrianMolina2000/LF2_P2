import re
import os


class Token:
    def __init__(self, lex, tok, f, c):
        self.lexema = lex
        self.token = tok
        self.fila = f
        self.columna = c


def report(tokis):
    file_name = open("Reporte/Tokens_lista.html", "w")

    file_name.write("<!DOCTYPE html>\n<html>\n<head>\n")
    file_name.write("   <meta charset='UTF-8'>\n")
    file_name.write(
        "   <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'>\n")
    file_name.write("</head>\n")
    file_name.write("<body class='container grey lighten-1'>\n")
    file_name.write("<h2>TOKENS</h2>\n")
    file_name.write("   <table class='highlight'>\n")
    file_name.write("       <thead>\n")
    file_name.write("           <tr>\n")
    file_name.write("               <th>No.</th>\n")
    file_name.write("               <th>Fila</th>\n")
    file_name.write("               <th>Columna</th>\n")
    file_name.write("               <th>Lexema</th>\n")
    file_name.write("               <th>Token</th>\n")
    file_name.write("           </tr>\n")
    file_name.write("       </thead>\n")
    file_name.write("       <tbody>\n")

    num = 1
    for toke in tokis:
        file_name.write("           <tr>\n")
        file_name.write(f"                <th><strong>{num}</strong></th>\n")
        file_name.write(
            f"                <th><strong>{toke.fila}</strong></th>\n")
        file_name.write(
            f"                <th><strong>{toke.columna}</strong></th>\n")
        file_name.write(
            f"                <th><strong>{toke.lexema}</strong></th>\n")
        file_name.write(
            f"                <th><strong>{toke.token}</strong></th>\n")
        file_name.write("           </tr>\n")
        num += 1

    file_name.write("       </tbody>\n")
    file_name.write("   </table>\n")
    file_name.write("   <hr>\n")
    file_name.write("<h2>GRAFICA</h2>\n")
    file_name.write("<img src='Ruta.svg' alt='Grafica' ")
    file_name.write("</body>\n</html>\n")

    file_name.close()
    # os.startfile("Reporte\Tokens_lista.html")

# PATRONES


pattern_tabla = r"[T|t][A|a][B|b][L|l][A|a]\s*\(.*,.*\)\{"
pattern_encabezado = r"[E|e][N|n][C|c][A|a][B|b][E|e][Z|z][A|a][D|d][O|o][S|s]\s*\(.*\).*;"
pattern_fila = r"[F|f][I|i][L|l][A|a]\s*\(.*\).*;"
pattern_defecto = r"\}\s*[D|d][E|e][F|f][E|e][C|c][T|t][O|o]\s*\(.*\)\.*"


def analizar_tabla_tokens(path):

    tokens = []

    with open(path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        n_linea = 1
        for linea in lineas:
            # Matriz
            if re.search(pattern_tabla, linea):
                obtener = re.sub(
                    r"\(.*,.*\)\{", "", re.findall(pattern_tabla, linea)[0])
                tok = Token(obtener, "Tabla", n_linea, re.search(
                    pattern_tabla, linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # Fila
            if re.search(pattern_fila, linea):
                obtener = re.sub(r"\(.*\).*;", "",
                                 re.findall(pattern_fila, linea)[0])
                tok = Token(obtener.replace(" ",""), "Fila", n_linea, re.search(
                    pattern_fila, linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)
            
            # Encabezado
            if re.search(pattern_encabezado, linea):
                obtener = re.sub(r"\(.*\).*;", "",
                                 re.findall(pattern_encabezado, linea)[0])
                tok = Token(obtener.replace(" ",""), "Encabezado", n_linea, re.search(
                    pattern_encabezado, linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # Parentesis-Apertura
            if re.search(r"\(", linea):
                obtener = re.search(r"\(", linea)
                tok = Token(obtener.group(), "Parentesis_Apertura",
                            n_linea, re.search(r"\(", linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # Nombre
            if re.search(r"'.*'", linea):
                obtener = re.search(r"'.*'", linea)
                tok = Token(obtener.group(), "Nombres", n_linea,
                            re.search(r"'.*'", linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # Parentesis-Cerradura
            if re.search(r"\)", linea):
                obtener = re.search(r"\)", linea)
                tok = Token(obtener.group(), "Parentesis_Cerradura",
                            n_linea, re.search(r"\)", linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # Llave-Apertura
            if re.search(r"\{", linea):
                obtener = re.search(r"\{", linea)
                tok = Token(obtener.group(), "Llave_Apertura",
                            n_linea, re.search(r"\{", linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # Llave-Cerradura
            if re.search(r"\}", linea):
                obtener = re.search(r"\}", linea)
                tok = Token(obtener.group(), "Llave_Cerradura",
                            n_linea, re.search(r"\}", linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # punto y coma
            if re.search(r";", linea):
                obtener = re.search(r";", linea)
                tok = Token(obtener.group(), "Fin de Instruccion",
                            n_linea, re.search(r";", linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # Defecto
            if re.search(pattern_defecto, linea):
                obtener = re.sub(
                    r"\(.*\).*", "", re.findall(pattern_defecto, linea)[0])
                obtener = obtener.replace("}", "")
                obtener = obtener.replace(" ", "")
                tok = Token(obtener, "Defecto", n_linea, re.search(
                    pattern_defecto, linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            # Comentario
            if re.search(r"//", linea):
                obtener = re.search(r"//", linea)
                tok = Token(obtener.group(), "Comentario", n_linea,
                            re.search(r"//", linea).start()+1)
                tokens.append(tok)
                # print(tok.fila, tok.columna, tok.lexema, tok.token)

            n_linea += 1

    report(tokens)

# analizar_tabla_tokens("Tabla.lfp")
