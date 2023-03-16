import csv
import cProfile

nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
                "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
                "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
                "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}
def check_username(nombre):

    return nombre.title()

def check_nif(user_nif):

    nif_number = int(user_nif[0:8])
    letra_correcta = str(nif_number % 23)
    nif_corregido = user_nif[0:8] + nif_dict[letra_correcta]
    return nif_corregido

def check_username(ruta1):
    dict_personas = []
    with open(ruta1, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', dialect=csv.excel)
        for persona in reader:
            dict_personas.append(persona)
    dict_personas.pop(0)
    for usuario in dict_personas:
        usuario[0] = check_username(usuario[0])
        usuario[1] = check_nif(usuario[1])
    with open(ruta1, encoding='utf-8') as end:
        final = open(ruta1, "w", newline="")
        end = csv.writer(final, quotechar='', quating=csv.QUOTE_ALL)
        for linea in dict_personas:
            end.writerow(linea)

cProfile.run("C:\\Users\\Dell\\OneDrive\\Escritorio\\Dapi\\GitHub\\practica0301_Garcia_Jin\\50 - copia (2).csv")
cProfile.run("C:\\Users\\Dell\\OneDrive\\Escritorio\\Dapi\\GitHub\\practica0301_Garcia_Jin\\1000 - copia (2).csv")