flag1 = True

frase = input("Ingrese su frase: ")

palabras = frase.split()

for l in palabras :
    print(l.upper())

while (flag1) :
    op = int(input("==========================================================\n1.Buscar Palabra\n2.Reemplazar Palabra\n3.Imprimir Frase\n4.Salir\nOpcion: "))

    match(op) :
        case 1 :

            buscar = input("Ingrese la palabra que quieres buscar: ")
            palabraC = frase.count(buscar)
            print (f"La palabra {buscar} aparece {palabraC} veces. . .")

        case 2 :
            reemplazar = input("Que palabra quieres reemplazar?: ")
            nuevaP = input("Cual quieres que sea la nueva palabra?: ")

            frase = frase.replace(reemplazar,nuevaP)

            print(f"La palabra {reemplazar} fue reemplazada exitosamente por {nuevaP}. . .")
        case 3 :
            print(frase)
        case 4 :
            flag1 = False