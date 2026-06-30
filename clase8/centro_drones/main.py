from clases.entrega import EntregaMedicamentos
from menu import mostrar_menu

def play():
    while True:
        mostrar_menu()
        opcion = input()
        if(opcion == "5"):
            print("saliendo del programa...")
            break
        elif opcion in ["1", "2", "3", "4"]:
            # este es el bloque donde vamos a ejecutar de acuerdo a la opcion elegida
            if opcion == "1":
                codigo = input("Codigo: ")
                cliente = input("cliente: ")
                piloto = input("piloto: ")
                peso = input("peso: ")
                destino = input("destino: ")
                entrega = EntregaMedicamentos(codigo, cliente, piloto, peso, destino)
                entrega.ejecutar()
            elif opcion == "2":
                pass

        else:
            print("opcion no valida")

play()