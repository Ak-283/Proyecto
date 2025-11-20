import os


def pedir_opcion(max_opcion):
    """Solicita al usuario una opción numérica entre 1 y max_opcion."""
    while True:
        respuesta = input("Selecciona una opción (número): ").strip()
        if respuesta.isdigit():
            valor = respuesta
            if 1 <= valor <= max_opcion:
                return valor
        print(f"Ingresa un número entre 1 y {max_opcion}.")


def pausar():
    """Espera a que el usuario presione Enter para continuar."""
    input("Presiona Enter para continuar...")


def limpiar_pantalla():
    """Limpia la terminal para evitar saturar el texto."""
    comando = "" if os.name == "nt" else "clear"
    os.system(comando)
