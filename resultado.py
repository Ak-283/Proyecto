from recursos import (
    nivel_combustible,
    nivel_energia,
    nivel_moral,
    nivel_oxigeno,
    recursos_críticos,
)


def determinar_resultado(etapa_final_exitosa):
    """Calcula si la misión fue un éxito real según recursos y decisiones."""
    if etapa_final_exitosa and not recursos_críticos():
        return True
    if etapa_final_exitosa and nivel_combustible() > 10 and nivel_oxigeno() > 20:
        return True
    return False


def mostrar_resumen_final(nombre_nave, exito):
    """Imprime el resumen final con estado de recursos."""
    print("\n=== RESUMEN DE MISIÓN ===")
    print(f"Nave: {nombre_nave}")
    print(f"Energía final: {nivel_energia()}%")
    print(f"Oxígeno final: {nivel_oxigeno()}%")
    print(f"Combustible final: {nivel_combustible()}%")
    print(f"Moral final: {nivel_moral()}%")
    if exito:
        print("Resultado: VICTORIA. Alcanzaste el destino con la tripulación viva.")
    else:
        print("Resultado: DERROTA. La nave quedó varada o los recursos colapsaron.")
