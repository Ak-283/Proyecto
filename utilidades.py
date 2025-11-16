def pedir_opcion(max_opcion):
    """Solicita al usuario una opción numérica entre 1 y max_opcion."""
    while True:
        respuesta = input("Selecciona una opción (número): ").strip()
        if respuesta.isdigit():
            valor = int(respuesta)
            if 1 <= valor <= max_opcion:
                return valor
        print(f"Ingresa un número entre 1 y {max_opcion}.")


def pausar():
    """Espera a que el usuario presione Enter para continuar."""
    input("Presiona Enter para continuar...")
