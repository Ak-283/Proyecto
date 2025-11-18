from estado import progreso, riesgo
from recursos import estado_recursos, recursos_críticos, recursos_en_peligro


def mostrar_panel(nombre_evento):
    """Muestra un panel resumen tras cada evento."""
    print("\n--- Panel táctico tras " + nombre_evento + " ---")
    print("Progreso hacia el destino: " + str(progreso()) + "%")
    print("Nivel de riesgo acumulado: " + str(riesgo()) + "%")
    print(estado_recursos())
    if recursos_críticos():
        print("ALERTA: recursos en nivel crítico, cualquier decisión puede fallar.")
    elif recursos_en_peligro():
        print("Atención: las reservas están en zona amarilla, ajusta tu estrategia.")
