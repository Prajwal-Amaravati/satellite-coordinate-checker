import pytest

@pytest.fixture
def rectangle_coords():
    return [(-50, -90), (-50, 90), (50, -90), (50, 90)]

@pytest.fixture
def position_checker(rectangle_coords):
    return PositionofPointinRectangle(rectangle_coords)