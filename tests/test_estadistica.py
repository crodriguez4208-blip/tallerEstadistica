import pytest

from estadistica import media, mediana, rango, normalizar_min_max


def test_media_basica():
    assert media([2, 4, 6]) == 4


def test_media_con_decimales():
    assert media([1, 2]) == pytest.approx(1.5)


def test_media_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        media([])


def test_mediana_cantidad_impar():
    assert mediana([3, 1, 2]) == 2


def test_mediana_cantidad_par():
    assert mediana([4, 1, 3, 2]) == 2.5


def test_rango_basico():
 assert rango([3, 10, 7]) == 7


def test_rango_con_negativos():
 assert rango([-5, 0, 5]) == 10


def test_rango_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        rango([])


def test_normalizar_extremos_quedan_en_0_y_1():
    resultado = normalizar_min_max([10, 20, 30])
    assert resultado == pytest.approx([0.0, 0.5, 1.0])

@pytest.mark.parametrize("datos, esperado", [
 ([1, 2, 3, 4], 2.5),
 ([7], 7),
 ([5, 1], 3),
])
def test_mediana_varios_casos(datos, esperado):
 assert mediana(datos) == esperado