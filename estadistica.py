"""Funciones de estadística descriptiva para el taller de Git + pytest."""


def media(datos):
    """Promedio aritmético de una lista de números."""
    if len(datos) == 0:
        raise ValueError("La lista está vacía")
    return sum(datos) / len(datos)


def mediana(datos):
    """Valor central de los datos ordenados.

    Si la cantidad de datos es par, la mediana es el promedio
    de los dos valores centrales.
    """
    if len(datos) == 0:
        raise ValueError("La lista está vacía")
    ordenados = sorted(datos)
    n = len(ordenados)
    mitad = n // 2
    return ordenados[mitad]


def rango(datos):
    """Diferencia entre el valor máximo y el mínimo."""
    if len(datos) == 0:
        raise ValueError("La lista está vacía")
    return max(datos) - min(datos)


def normalizar_min_max(datos):
    """Escala los datos al intervalo [0, 1]: (x - min) / (max - min)."""
    minimo = min(datos)
    maximo = max(datos)
    return [(x - minimo) / (maximo - minimo) for x in datos]
