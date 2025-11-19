energia_actual = 0
oxigeno_actual = 0
combustible_actual = 0
moral_actual = 0


def establecer_recursos(
    energia_inicial, oxigeno_inicial, combustible_inicial, moral_inicial
):
    """Configura los recursos básicos de la misión."""
    global energia_actual, oxigeno_actual, combustible_actual, moral_actual
    energia_actual = energia_inicial
    oxigeno_actual = oxigeno_inicial
    combustible_actual = combustible_inicial
    moral_actual = moral_inicial


def ajustar_energia(cambio):
    """Aplica un cambio sobre la reserva de energía y evita valores negativos."""
    global energia_actual
    energia_actual += cambio
    if energia_actual < 0:
        energia_actual = 0
    if energia_actual > 100:
        energia_actual = 100


def ajustar_oxigeno(cambio):
    """Aplica un cambio sobre el oxígeno restante."""
    global oxigeno_actual
    oxigeno_actual += cambio
    if oxigeno_actual < 0:
        oxigeno_actual = 0
    if oxigeno_actual > 100:
        oxigeno_actual = 100


def ajustar_combustible(cambio):
    """Ajusta el combustible tras una maniobra."""
    global combustible_actual
    combustible_actual += cambio
    if combustible_actual < 0:
        combustible_actual = 0
    if combustible_actual > 100:
        combustible_actual = 100


def ajustar_moral(cambio):
    """Modifica la moral de la tripulación."""
    global moral_actual
    moral_actual += cambio
    if moral_actual < 0:
        moral_actual = 0
    if moral_actual > 100:
        moral_actual = 100


def nivel_energia():
    """Devuelve el nivel actual de energía."""
    return energia_actual


def nivel_oxigeno():
    """Devuelve el nivel actual de oxígeno."""
    return oxigeno_actual


def nivel_combustible():
    """Devuelve el nivel actual de combustible."""
    return combustible_actual


def nivel_moral():
    """Devuelve el ánimo actual de la tripulación."""
    return moral_actual


def estado_recursos():
    """Genera un resumen textual de los recursos."""
    return (
        "Energía: " + str(nivel_energia()) + "% | "
        "Oxígeno: " + str(nivel_oxigeno()) + "% | "
        "Combustible: " + str(nivel_combustible()) + "% | "
        "Moral: " + str(nivel_moral()) + "%"
    )


def recursos_críticos():
    """Indica si alguno de los recursos está por debajo de un umbral crítico."""
    return (
        nivel_energia() < 20
        or nivel_oxigeno() < 25
        or nivel_combustible() < 20
        or nivel_moral() < 20
    )


def aplicar_desgaste_base():
    """Simula el consumo natural de recursos entre eventos."""
    ajustar_energia(-4)
    ajustar_oxigeno(-3)
    ajustar_combustible(-5)
    ajustar_moral(-1)


def recursos_en_peligro():
    """Regresa True si los recursos están en zona amarilla."""
    return (
        nivel_energia() < 40
        or nivel_oxigeno() < 40
        or nivel_combustible() < 35
        or nivel_moral() < 35
    )
