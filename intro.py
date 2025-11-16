from utilidades import pedir_opcion


def mostrar_introduccion():
    """Presenta la historia y contexto de la misión."""
    print("\n=== MISIÓN ESPACIAL: COMANDANTE INTERACTIVO ===")
    print("El destino está a millones de kilómetros. Cada decisión pesa.")


def solicitar_nombre_nave():
    """Solicita al jugador el nombre de la nave y la tripulación."""
    nombre = input("Ingresa el nombre de tu nave y tripulación: ").strip()
    if nombre == "":
        nombre = "La DSS"  # Nombre predeterminado si no responde
    return nombre


def mostrar_tripulacion(nombre):
    """Muestra el equipo que acompaña al comandante."""
    print(f"Tripulación asignada: {nombre} y su equipo de élite.")


def solicitar_tipo_mision():
    """Describe las opciones de misión y valida la elección."""
    print("\nElige el perfil de la misión:")
    print("1) Ruta directa con riesgos, más rápida. (Difícil)")
    print("2) Ruta segura con más maniobras, más lenta. (Normal)")
    print("3) Ruta de exploración con investigación adicional. (Fácil)")
    opcion = pedir_opcion(3)
    return opcion
