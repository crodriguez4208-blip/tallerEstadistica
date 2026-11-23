"""Funciones de estadística descriptiva para el taller de Git + pytest."""
import math

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
    if n % 2 == 0:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2
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
    if maximo == minimo:
        raise ValueError("No se puede normalizar: todos los valores son iguales")
    return [(x - minimo) / (maximo - minimo) for x in datos]



def porcentaje_faltantes(datos):
    """Porcentaje (0-100) de valores None en la lista."""
    if len(datos) == 0:
        raise ValueError("La lista está vacía")
    faltantes = sum(1 for x in datos if x is None)
    return 100 * faltantes / len(datos)



def desviacion_estandar(datos):
    """Desviación estándar muestral (dividiendo por n-1)."""
    if len(datos) < 2:
        raise ValueError("Se necesitan al menos 2 datos para calcular la desviación estándar")
    promedio = media(datos)
    suma_cuadrados = sum((x - promedio) ** 2 for x in datos)
    varianza = suma_cuadrados / (len(datos) - 1)
    return math.sqrt(varianza)