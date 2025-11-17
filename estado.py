progreso_actual = 0
riesgo_actual = 10


def reiniciar_estado():
    """Reinicia los indicadores de progreso y riesgo."""
    global progreso_actual, riesgo_actual
    progreso_actual = 0
    riesgo_actual = 10


def avanzar_progreso(cambio):
    """Incrementa el porcentaje de avance de la misión."""
    global progreso_actual
    progreso_actual += cambio
    if progreso_actual > 100:
        progreso_actual = 100
    if progreso_actual < 0:
        progreso_actual = 0


def ajustar_riesgo(cambio):
    """Modifica el riesgo general de la misión."""
    global riesgo_actual
    riesgo_actual += cambio
    if riesgo_actual > 100:
        riesgo_actual = 100
    if riesgo_actual < 0:
        riesgo_actual = 0


def progreso():
    """Devuelve el avance acumulado."""
    return progreso_actual


def riesgo():
    """Devuelve el riesgo acumulado."""
    return riesgo_actual
