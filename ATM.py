flag1 = True
flag2 = True
flag3 = True
intentos = 3
saldo = 1000.00

while(flag1) :
    pin = int(input("Ingrese un pin de 4 digitos: "))
    if pin < 9999 and pin > 1000 :
        print("[✅]Pin establecido correctamente. . .")
        flag1 = False
    else :
        print("[❌]Introduzca un pin valido. . .")

while(flag2) :
    tpin = int(input("Introzuca su pin(Solo tiene 3 intentos): "))
    if tpin != pin :
        intentos -= 1
        print(f"[⚠️]Pin incorrecto, le quedan {intentos} intentos. . .")
        if intentos == 0 :
            print("[❌]Demasiados intentos fallidos, bloqueando cuenta. . .")
            flag2 = False

    if pin == tpin :
        flag2 = False
        while(flag3) :
            print("\nBienvenido al Sistema\n1.Consultar saldo\n2.Retirar dinero\n3.Depositar dinero\n4.Salir")
            op = int(input("\nEliga la opcion que desee: "))

            match(op) :
                case 1 :
                    print(f"Su saldo actual es de: ${saldo}")
                case 2 :
                    retiro = float(input("Cuanto dinero desea retirar: $"))
                    if retiro > saldo :
                        print("[❌]Invalido, no se puede retirar. . .")
                    if retiro <= saldo :    
                        saldo = saldo - retiro
                        saldo == saldo
                        print(f"[🔄️]Su saldo final es de: ${saldo}")
                case 3 :
                    deposito = float(input("Cuanto dinero desea depositar: $"))
                    saldo = saldo + deposito
                    saldo == saldo
                    print(f"[🔄️]Su saldo final es de: ${saldo}")
                case 4 :
                    print("Gracias por usar el programa. . .")
                    flag2 = False
                    flag1 = False
                    flag3 = False