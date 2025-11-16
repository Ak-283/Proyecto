from recursos import establecer_recursos, nivel_moral


def configurar_recursos(tipo_mision):
    """Define los recursos iniciales según la dificultad seleccionada."""
    if tipo_mision == 1:
        establecer_recursos(90, 90, 75, 80)
        return "Ruta directa: el avance rápido exige agresividad desde el inicio."
    if tipo_mision == 2:
        establecer_recursos(95, 95, 85, 88)
        return "Ruta segura: menos margen de error y más presión sobre los sistemas."
    establecer_recursos(92, 93, 78, 85)
    return "Ruta de exploración: mantenemos curiosidad, pero sin reservas extras."


def mostrar_configuracion():
    """Informa al jugador cómo quedan los recursos y el ánimo."""
    print("\nConfiguración inicial ajustada:")
    print(f"Nivel de moral: {nivel_moral()}% (el equipo está preparado).")
