from configuracion import configurar_recursos, mostrar_configuracion
from estado import ajustar_riesgo, avanzar_progreso, reiniciar_estado
from eventos import (
    evento_asteroides,
    evento_averia_sistemas,
    evento_nebulosa,
    evento_reciclaje,
    evento_rescate,
    evento_salida,
    evento_viento_solar,
)
from intro import (
    mostrar_introduccion,
    mostrar_tripulacion,
    solicitar_nombre_nave,
    solicitar_tipo_mision,
)
from monitoreo import mostrar_panel
from recursos import aplicar_desgaste_base, recursos_críticos
from resultado import determinar_resultado, mostrar_resumen_final
from utilidades import pausar, pedir_opcion


def ejecutar_evento(nombre, funcion_evento, avance, riesgo_delta):
    """Ejecuta un evento, aplica desgaste y muestra panel táctico."""
    print(funcion_evento())
    aplicar_desgaste_base()
    avanzar_progreso(avance)
    ajustar_riesgo(riesgo_delta)
    mostrar_panel(nombre)
    pausar()


def ejecutar_mision():
    """Coordina cada fase de la misión espacial."""
    reiniciar_estado()
    mostrar_introduccion()
    nombre = solicitar_nombre_nave()
    mostrar_tripulacion(nombre)
    tipo = solicitar_tipo_mision()
    descripcion = configurar_recursos(tipo)
    print(f"\n{descripcion}")
    mostrar_configuracion()
    pausar()
    ejecutar_evento("los asteroides", evento_asteroides, 12, 10)
    ejecutar_evento("la tormenta solar", evento_viento_solar, 14, 12)
    ejecutar_evento("el reciclador", evento_reciclaje, 10, 8)
    ejecutar_evento("la avería", evento_averia_sistemas, 12, 10)
    ejecutar_evento("la nebulosa", evento_nebulosa, 16, 14)
    ejecutar_evento("el rescate", evento_rescate, 14, 10)
    mensaje_final = evento_salida()
    print(mensaje_final)
    aplicar_desgaste_base()
    avanzar_progreso(12)
    ajustar_riesgo(20)
    mostrar_panel("la maniobra final")
    etapa_final = not recursos_críticos()
    exito = determinar_resultado(etapa_final)
    mostrar_resumen_final(nombre, exito)


def preguntar_reinicio():
    """Preguntar al jugador si desea volver a intentar la misión."""
    print("\n¿Deseas reiniciar la misión o retirarte?")
    print("1) Reiniciar y comandar de nuevo.")
    print("2) Finalizar la sesión de comando.")
    return pedir_opcion(2) == 1


def main():
    """Punto de entrada principal del simulador."""
    while True:
        ejecutar_mision()
        if not preguntar_reinicio():
            print("Gracias por comandar la misión. Hasta la próxima comandante.")
            break


if __name__ == "__main__":
    main()
