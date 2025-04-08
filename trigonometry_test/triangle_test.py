import pytest
from trigonometry.triangle import Triangle


def test_triangle_area_base_2_height_3_should_be_3():
    # Cria uma instância de Triangle com base = 2 e altura = 3 e calcula a área.
    triangle = Triangle(2, 3)
    assert triangle.area() == 3, "A área do triângulo deveria ser 3."


def test_triangle_perimeter_rs2_base_ls3_should_be_6():
    triangle = Triangle(2, 2, 2)
    assert triangle.perimeter() == 6, "O perímetro do triângulo deveria ser 6."


def test_triangle_perimeter_scalene_triangle_should_be_correct():
    triangle = Triangle(2, 3, 4)
    assert triangle.perimeter() == 9, "O perímetro do triângulo escaleno deveria ser 9."


@pytest.mark.parametrize("side1,side2,side3,expected_type", [
    (5, 5, 5, "Equilateral"),
    (5, 5, 3, "Isosceles"),
    (5, 4, 6, "Scalene"),
])
def test_get_triangle_type_returns_correct_type(side1, side2, side3, expected_type):
    triangle = Triangle(side1, side2, side3)
    assert triangle.get_triangle_type() == expected_type, f"O tipo esperado era {expected_type}."


def test_get_triangle_type_performs_well_under_heavy_load():
    import time
    start_time = time.time()
    for _ in range(1000000):
        triangle = Triangle(5, 5, 5)
        triangle.get_triangle_type()
    elapsed_time = time.time() - start_time
    assert elapsed_time < 1, "O método deveria completar em menos de 1 segundo."
