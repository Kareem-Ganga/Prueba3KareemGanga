import random
import csv
from pathlib import Path
import os
from functools import reduce
sueldos=[]
tra_suel=[]
opc=""
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
def sueldoaleatorio():
    i=0
    sueldos=[]
    while i < 10:
        sueldos.append(random.randint(300000, 2500000))
        i+=1
    return sueldos
def media_geometrica(valoresnoma):
    if len(valoresnoma) == 0:
        raise ValueError("La lista no puede estar vacía")
    producto = reduce(lambda x, y: x * y, valoresnoma)
    media_geo = producto ** (1 / len(valoresnoma))
    return media_geo

def archivocsv():
    datos_csv = []
    for i in range(0, len(tra_suel), 2):
        nombre = tra_suel[i]
        sueldo = tra_suel[i + 1]
        sueldosalud=int(sueldo*0.07)
        sueldoafp=int(sueldo*0.12)
        sueldoliquido=sueldo-sueldosalud-sueldoafp
        datos_csv.append([nombre, sueldo,sueldosalud,sueldoafp,sueldoliquido])

    nombre_archivo = 'datos_sueldos.csv'
    ruta_escritorio = os.path.join(Path.home(), 'Desktop', nombre_archivo)
    with open(ruta_escritorio, mode='w', newline='', encoding='utf-8-sig') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL, quotechar='"')
        escritor_csv.writerow(['Nombre', 'Sueldo Base','Descuento Salud','Descuento AFP','Sueldo liquido'])  # Escribir encabezados
        for fila in datos_csv:
            escritor_csv.writerow(fila)

    print(f'Se ha creado el archivo CSV "{ruta_escritorio}" con los datos de sueldos en el escritorio del usuario.')

while opc != "5":
    opc = input("Seleccione una opcion:\n 1)Asignar sueldos aleatorios\n 2)Clasificar Sueldos\n 3)Ver estadisticas\n 4)Reporte de sueldos\n 5)Salir del programa \n")
    if opc == "1":
        sueldos=sueldoaleatorio()
    if opc == "2":
        tra_suel=[]
        lis8kk=[]
        lis8kkk=[]
        lis2kkk=[]
        sueldototal=0
        if len(sueldos) != 0:
            i=0
            for trabajador in trabajadores:
                tra_suel.append(trabajador)
                tra_suel.append(sueldos[i])
                i+=1
            i=0
            for valor in tra_suel:
                try:
                    if int(valor) < 800000:
                        lis8kk.append(tra_suel[i-1])
                        lis8kk.append(tra_suel[i])
                        sueldototal+=int(valor)
                    if int(valor) > 800000 and int(valor) < 2000000:
                        lis8kkk.append(tra_suel[i-1])
                        lis8kkk.append(tra_suel[i])
                        sueldototal+=int(valor)
                    if int(valor) > 2000000:
                        lis2kkk.append(tra_suel[i-1])
                        lis2kkk.append(tra_suel[i])
                        sueldototal+=int(valor)
                    i+=1
                except:
                    i+=1
            print("Sueldos menores a $800000 TOTAL:",len(lis8kk)//2,"\n")
            print("Nombre empleado        Sueldo")
            i=0
            while i < len(lis8kk):
                print(lis8kk[i],"        $",lis8kk[i+1],)
                i+=2
            print("\n\nSueldos entre $800000 y $2.000.000 TOTAL:",len(lis8kkk)//2,"\n")
            print("Nombre empleado        Sueldo")
            i=0
            while i < len(lis8kkk):
                print(lis8kkk[i],"        $",lis8kkk[i+1])
                i+=2
            print("\n\nSueldos superiores a $2.000.000 TOTAL:",len(lis2kkk)//2,"\n")
            print("Nombre empleado        Sueldo")
            i=0
            while i < len(lis2kkk):
                print(lis2kkk[i],"        $",lis2kkk[i+1])
                i+=2
            print("\nTOTAL SUELDOS: $",sueldototal,"\n")
        else:
            print("No hay sueldos disponibles para clasificar\n")
    if opc == "3":
        sueldomenor=30000000
        sueldomayor=0
        sueldototal2=0
        valoresnoma=[]
        if len(sueldos)!=0 and len(tra_suel)!=0:
            for sueldoto in tra_suel:
                try:
                    if int(sueldoto) < sueldomenor:
                        sueldomenor = int(sueldoto)
                except:
                    sueldomenor=sueldomenor
            print("Sueldo mas bajo: $",sueldomenor)
            for sueldoto in tra_suel:
                try:
                    sueldototal2+=int(sueldoto)
                    if int(sueldoto) > sueldomayor:
                        sueldomayor = int(sueldoto)
                except:
                    sueldomayor=sueldomayor
            print("Sueldo mas alto: $",sueldomayor)
            print("El promedio de sueldos es: $", sueldototal2//10)
            for valores in tra_suel:
                try:
                    valoresnoma.append(int(valores))
                except:
                    valoresnoma=valoresnoma
            media_geo_sueldos = media_geometrica(valoresnoma)
            print(f"La media geométrica de los sueldos es: {round(media_geo_sueldos,2)}")
        if len(tra_suel)==0:
            print("Elegir la opcion numero 2 para clasificar los sueldos")
        if len(sueldos)==0:
            print("No hay sueldos disponibles para clasificar\n")
    if opc == "4":
        if tra_suel != []:
            archivocsv()
        if tra_suel == []:
            print("Elegir la opcion numero 2 para clasificar los sueldos")
    elif opc != "1" and opc != "2" and opc != "3" and opc != "4" and opc != "5":
        print("Opcion Incorrecta")
print("Saliendo del programa")
print("Desarrollado por Kareem Ganga")
print("Rut: 20676000-1")



