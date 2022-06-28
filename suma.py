def suma_lateral():
    imp:str = input("Ingrese un número: ")
    num:int = int(imp)
    cont:int = 1
    top:int = 10
    while (cont <= top):
        print(num * cont, ", ", end = "")
        cont = cont + 1

suma_lateral()
