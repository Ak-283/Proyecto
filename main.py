from configuracion import configurar_recursos, mostrar_configuracion
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
from recursos import recursos_críticos
from resultado import determinar_resultado, mostrar_resumen_final
from utilidades import pausar, pedir_opcion


def ejecutar_mision():
    """Coordina cada fase de la misión espacial."""
    mostrar_introduccion()
    nombre = solicitar_nombre_nave()
    mostrar_tripulacion(nombre)
    tipo = solicitar_tipo_mision()
    descripcion = configurar_recursos(tipo)
    print(f"\n{descripcion}")
    mostrar_configuracion()
    pausar()
    print(evento_asteroides())
    pausar()
    print(evento_viento_solar())
    pausar()
    print(evento_reciclaje())
    pausar()
    print(evento_averia_sistemas())
    pausar()
    print(evento_nebulosa())
    pausar()
    print(evento_rescate())
    pausar()
    mensaje_final = evento_salida()
    print(mensaje_final)
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
