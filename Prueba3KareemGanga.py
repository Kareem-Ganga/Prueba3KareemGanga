from datetime import datetime
import os

def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")
    dv = rut[-1].upper()
    rut = rut[:-1]
    suma = 0
    factor = 2
    for c in reversed(rut):
        suma += int(c) * factor
        factor += 1
        if factor > 7:
            factor = 2
    resto = 11 - (suma % 11)
    if resto == 11:
        dv_esperado = '0'
    elif resto == 10:
        dv_esperado = 'K'
    else:
        dv_esperado = str(resto)
    return dv == dv_esperado

def archivocsv(listareclamo):
    escritorio = os.path.join(os.path.expanduser('~'), 'Desktop') 
    ruta_archivo = os.path.join(escritorio, 'reclamos.csv')
    with open(ruta_archivo, "w") as csvfile:
        csvfile.write("HORA    RUT   MONTO(En Miles de Pesos)    MENSAJE\n")
        for reclamo in listareclamo:
            linea = ' '.join(map(str, reclamo)) + "\n"
            csvfile.write(linea)
    print("Archivo creado exitosamente.")

def listar_reclamos(listareclamo):
    if listareclamo:
        print("HORA    RUT   MONTO(En Miles de Pesos)    MENSAJE\n")
        for reclamo in listareclamo:
            print(' '.join(map(str, reclamo)))
        print("\n")
    else:
        print("No hay reclamos registrados.")

def registrar_reclamo():
    listareclamo = []
    while True:
        reclamo = input("Ingrese el Reclamo (Con el orden:Rut / Monto de su Compra / Mensaje. El mensaje no puede contener mas de 20 caracteres), Salir ingrese 0\n").title()
        hora_reclamo = datetime.now().time()
        hora_reclamo= hora_reclamo.strftime("%H:%M:%S")
        if reclamo == "0":
            break
        try:
            rut , monto, mensaje = reclamo.split('/')
            if validar_rut(rut):
                monto=int(monto)/1000
                if len(mensaje) <= 20:
                    listareclamo.append([hora_reclamo, rut, monto, mensaje])
                    x=0
                if len(mensaje) > 20:
                    print("El mensaje no puede contener mas de 20 caracteres")    
            if validar_rut(rut)== False:
                print(f"El RUT {rut} no es válido.\n")
        except ValueError:
            print("Formato Mal Ingresado. Asegúrese de usar el formato: Reclamo - Monto de su Compra - Mensaje.")
    return listareclamo
if __name__ == "__main__":
    listareclamo = []
    while True:
        opc = input("Elija una opción \n 1)Registrar Reclamo\n 2)Listar Reclamos \n 3)Respaldar Reclamos En el Sistema \n 4)Salir Del Programa\n")
        if opc == "1":
            listareclamo.extend(registrar_reclamo())
        elif opc == "2":
            listar_reclamos(listareclamo)
        elif opc == "3":
            archivocsv(listareclamo)
        elif opc == "4":
            print("Saliendo Del Programa")
            break
        else:
            print("Opción no válida. Intente de nuevo.")