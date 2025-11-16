from recursos import (
    ajustar_combustible,
    ajustar_energia,
    ajustar_moral,
    ajustar_oxigeno,
    estado_recursos,
    recursos_críticos,
)
from utilidades import pedir_opcion


def evento_asteroides():
    """Presenta un campo de asteroides con dos rutas posibles."""
    print("\nEvento: Campo de asteroides detectado en la trayectoria.")
    print("1) Acelerar entre los fragmentos, arriesgando energía y combustible.")
    print("2) Rodear el campo con maniobras suaves y aumentar tiempo de viaje.")
    opcion = pedir_opcion(2)
    if opcion == 1:
        ajustar_energia(-20)
        ajustar_combustible(-25)
        ajustar_moral(4)
        mensaje = "Se logró atravesar rápido, pero el reactor sintió el esfuerzo."
    else:
        ajustar_energia(-8)
        ajustar_combustible(-12)
        ajustar_moral(-4)
        mensaje = "La nave esquivó con cuidado, la tripulación está nerviosa."
    print(estado_recursos())
    if recursos_críticos():
        mensaje += " Recursos cercanos a crítico."
    return mensaje


def evento_viento_solar():
    """El viento solar puede dañar sistemas o dar impulso."""
    print("\nEvento: Tormenta solar en curso.")
    print("1) Activar escudos y mantener rumbo, consumiendo energía.")
    print("2) Desviar para aparcar detrás de un asteroide y esperar.")
    opcion = pedir_opcion(2)
    if opcion == 1:
        ajustar_energia(-22)
        ajustar_moral(3)
        mensaje = "Los escudos protegieron la nave, pero quedamos con poca energía."
    else:
        ajustar_combustible(-15)
        ajustar_moral(-6)
        mensaje = "El cambio de rumbo fue seguro, aunque el combustible sufrió."
    print(estado_recursos())
    if recursos_críticos():
        mensaje += " Se sienten las tensiones en la tripulación."
    return mensaje


def evento_reciclaje():
    """La tripulación debe elegir cómo usar el sistema de reciclaje."""
    print("\nEvento: Mantenimiento del reciclador de oxígeno.")
    print("1) Reforzar la filtración, mejora el oxígeno pero gasta energía.")
    print(
        "2) Confiar en el sistema automático, mantiene energía pero arriesga oxígeno."
    )
    opcion = pedir_opcion(2)
    if opcion == 1:
        ajustar_oxigeno(8)
        ajustar_energia(-16)
        mensaje = "El oxígeno mejora, pero la tripulación nota el esfuerzo energético."
    else:
        ajustar_oxigeno(-8)
        ajustar_energia(5)
        ajustar_moral(-4)
        mensaje = "Ahorramos energía, pero la confianza se resiente."
    print(estado_recursos())
    if recursos_críticos():
        mensaje += " Las reservas se equilibran con dificultad."
    return mensaje


def evento_salida():
    """Decisión final para llegar al destino."""
    print("\nEvento: Llegada al objetivo - último tramo conflictivo.")
    print(
        "1) Usar el impulso completo del reactor, arriesgando recursos pero llegando rápido."
    )
    print("2) Hacer un acoplamiento lento con la estación, conservando combustible.")
    opcion = pedir_opcion(2)
    if opcion == 1:
        ajustar_combustible(-28)
        ajustar_energia(-19)
        ajustar_moral(5)
        mensaje = "El acelerón final promete éxito, pero los tanques quedaron vacíos."
    else:
        ajustar_combustible(-12)
        ajustar_energia(-8)
        ajustar_moral(1)
        mensaje = "El acoplamiento suave mantiene recursos, pero el tiempo aumenta."
    print(estado_recursos())
    if recursos_críticos():
        mensaje += " Sin embargo, los recursos se mantuvieron en el límite."
    return mensaje


def evento_averia_sistemas():
    """La nave sufre una avería en los sistemas secundarios."""
    print("\nEvento: Avistamos una falla en los sistemas secundarios.")
    print("1) Desviar potencia para reparar de inmediato, perdiendo energía.")
    print("2) Activar modos de reserva y seguir, afectando la moral.")
    opcion = pedir_opcion(2)
    if opcion == 1:
        ajustar_energia(-18)
        ajustar_moral(3)
        mensaje = "La reparación fue exitosa, pero los reactores quedaron tensos."
    else:
        ajustar_energia(-5)
        ajustar_moral(-7)
        mensaje = "Seguimos con memorias de falla, la tripulación pierde confianza."
    print(estado_recursos())
    if recursos_críticos():
        mensaje += " La nave lucha con las consecuencias."
    return mensaje


def evento_nebulosa():
    """Navegar a través de una nebulosa cargada de partículas."""
    print("\nEvento: Nebulosa densa bloquea sensores.")
    print("1) Encender emisores de alta potencia y avanzar a ciegas, gastando energía.")
    print("2) Esperar a que pase la nube, estresando combustible y moral.")
    opcion = pedir_opcion(2)
    if opcion == 1:
        ajustar_energia(-20)
        ajustar_combustible(-8)
        ajustar_moral(2)
        mensaje = "Fue un impulso agresivo, pero llegamos al otro lado rápido."
    else:
        ajustar_combustible(-18)
        ajustar_moral(-5)
        mensaje = "El tiempo se perdió, el equipo está agotado por la espera."
    print(estado_recursos())
    if recursos_críticos():
        mensaje += " El ambiente espacial no perdona."
    return mensaje


def evento_rescate():
    """Decide si ayudar a una pequeña nave en distress."""
    print("\nEvento: Una señal de socorro distante pide ayuda.")
    print("1) Desviar para asistir, perdiendo combustible y tiempo.")
    print("2) Ignorar la llamada y mantener la ruta, manteniendo recursos.")
    opcion = pedir_opcion(2)
    if opcion == 1:
        ajustar_combustible(-15)
        ajustar_oxigeno(-10)
        ajustar_moral(4)
        mensaje = "Ayudaste a la nave; la tripulación gana moral pero queda exhausta."
    else:
        ajustar_moral(-6)
        mensaje = (
            "Continuamos; las reservas se salvan pero el equipo reprende la decisión."
        )
    print(estado_recursos())
    if recursos_críticos():
        mensaje += " Esta decisión deja secuelas."
    return mensaje
