from models.sate_lat_lon_data import SateLatLonData
from position_of_point_in_rectangle import PositionofPointinRectangle

class TestPositionofPointInsideRectangle:
    
    def test_point_inside_rectangle(position_checker):
        positions = [
            SateLatLonData(name="Satellite1", latitude=0, longitude=0, altitude=400),
            SateLatLonData(name="Satellite2", latitude=30, longitude=30, altitude=400),
        ]

        result = position_checker.is_point_in_rectangle(positions)
        assert result == ["Satellite1", "Satellite2"]

    def test_point_outside_rectangle(position_checker):
        positions = [
            SateLatLonData(name="Satellite1", latitude=60, longitude=0, altitude=400),
            SateLatLonData(name="Satellite2", latitude=30, longitude=-100, altitude=400),
        ]

        result = position_checker.is_point_in_rectangle(positions)
        assert result == []

    def test_point_on_edge_of_rectangle(position_checker):
        positions = [
            SateLatLonData(name="Satellite1", latitude=-50, longitude=0, altitude=400),
            SateLatLonData(name="Satellite2", latitude=50, longitude=90, altitude=400),
        ]

        result = position_checker.is_point_in_rectangle(positions)
        assert result == ["Satellite1", "Satellite2"]

    def test_point_within_rectangle_with_decimal_coords(position_checker):
        rectangle_coords = [(-50.5, -90.5), (-50.5, 90.5), (50.5, -90.5), (50.5, 90.5)]
        position_checker = PositionofPointinRectangle(rectangle_coords)

        positions = [
            SateLatLonData(name="Satellite1", latitude=-50.5, longitude=-90.5, altitude=400),
            SateLatLonData(name="Satellite2", latitude=50.5, longitude=90.5, altitude=400),
        ]

        result = position_checker.is_point_in_rectangle(positions)
        assert result == ["Satellite1", "Satellite2"]