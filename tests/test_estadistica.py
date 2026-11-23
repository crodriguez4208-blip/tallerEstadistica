import pytest

from estadistica import media, mediana

# === Media ===
def test_media_basica():
    assert media([2, 4, 6]) == 4


def test_media_con_decimales():
    assert media([1, 2]) == pytest.approx(1.5)


def test_media_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        media([])

# === Mediana ===
def test_mediana_cantidad_impar():
    assert mediana([3, 1, 2]) == 2


def test_mediana_cantidad_par():
    assert mediana([4, 1, 3, 2]) == pytest.approx(2.5)
