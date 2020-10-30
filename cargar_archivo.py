import re, os
from Tokens_lista import analizar_lista_tokens
from Tokens_matriz import analizar_matriz_tokens
from Lista import leer_archivo_lista
from Matriz import leer_archivo_matriz

pattern_lista = r"[L|l][I|i][S|s][T|t][A|a]\s*\(.*,.*,.*\)\{"
pattern_matriz = r"[M|m][A|a][T|t][R|r][I|i][Z|z]\s*\(.*,.*,.*,.*,.*\)\{"

def carga_archivo():
    ruta = input("Ingrese la ruta del archivo: ")
    if os.path.exists(ruta): 
        if re.search(r"\.lfp", ruta):
            print("==========================================\n\n")
            
            with open(ruta, 'r', encoding='utf-8') as f:
                lineas = f.readlines()
                for linea in lineas:
                    #Lista
                    if re.search(pattern_lista, linea):
                        analizar_lista_tokens(ruta)
                        leer_archivo_lista(ruta)

                    elif re.search(pattern_matriz, linea):
                        analizar_matriz_tokens(ruta)
                        leer_archivo_matriz(ruta)
                    else:
                        continue

            var = input("Ingrese Enter para continuar: ")
            print("Regresando a menu principal...")
        # else:
        #     print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        #     print("////Error -> Unicamente archivos .txt ////")
        #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

    # else:
    #     print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    #     print("/////  Error -> Ruta no encontrada  /////")
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
