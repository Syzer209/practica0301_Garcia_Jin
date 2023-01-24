import csv


def check_username(nombre):


   return nombre.title()


def check_nif(user_nif):
   nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
               "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
               "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
               "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}


   nif_number = int(user_nif[0:8])
   letra_correcta = str(nif_number % 23)
   nif_corregido = user_nif[0:8] + nif_dict[letra_correcta]
   return nif_corregido




def check_50(ruta1):
   with open(ruta1, "r", encoding='utf-8',newline="") as file1:
       reader1 = csv.DictReader(file1, fieldnames=["nombre","dni"])
       check_50_mod = []
       for user1 in reader1:
           user1["nombre"] = check_username(user1["nombre"])
           user1["dni"] = check_nif(user1["dni"])
           check_50_mod.append(user1)
   with open(ruta1, "w", encoding='utf-8',newline="") as file1:
       writer1 = csv.DictWriter(file1, fieldnames=["nombre","dni"])
       writer1.writeheader()
       for user1 in check_50_mod:
           writer1.writerow(user1)




def check1000(ruta2):
   with open(ruta2, "r", encoding='utf-8',newline="") as file2:
       reader2 = csv.DictReader(file2, fieldnames=["nombre","dni"])
       check_1000_mod = []
       for user2 in reader2:
           user2["nombre"] = check_username(user2["nombre"])
           user2["dni"] = check_nif(user2["dni"])
           check_1000_mod.append(user2)
   with open(ruta2, "w", encoding='utf-8',newline="") as file2:
       writer2 = csv.DictWriter(file2, fieldnames=["nombre","dni"])
       writer2.writeheader()
       for user2 in check_1000_mod:
           writer2.writerow(user2)



check_50("C:\\Users\\Dell\\OneDrive\\Escritorio\\Dapi\\GitHub\\practica0301_Garcia_Jin\\50 - copia (2).csv")
check1000("C:\\Users\\Dell\\OneDrive\\Escritorio\\Dapi\\GitHub\\practica0301_Garcia_Jin\\1000 - copia (2).csv")


import cProfile
cProfile.run("C:\\Users\\Dell\\OneDrive\\Escritorio\\Dapi\\GitHub\\practica0301_Garcia_Jin\\50 - copia (2).csv")
cProfile.run("C:\\Users\\Dell\\OneDrive\\Escritorio\\Dapi\\GitHub\\practica0301_Garcia_Jin\\1000 - copia (2).csv")