class PositionofPointinRectangle:
    """checks if the lat lon is within the rectangle"""

    def __init__(self, rectangle_coords: list) -> None:
        self.rectangle_coords = rectangle_coords

    def is_point_in_rectangle(self, position_obj: list):
        """returns if the point is present inside the rectangle or outside

        Args:
            position_obj (obj): object of the satelite lat lon
            rectangle_coords (list): list of coordinates

        Returns:
            satellite_lists: list of satellites intersecting
        """

        satellite_lists = []
        for i, posi_obj in enumerate(position_obj):
            latitudes = [coord[0] for coord in self.rectangle_coords]
            longitudes = [coord[1] for coord in self.rectangle_coords]

            min_lat = min(latitudes)
            max_lat = max(latitudes)
            min_lon = min(longitudes)
            max_lon = max(longitudes)

            if (
                min_lat <= posi_obj.latitude <= max_lat
                and min_lon <= posi_obj.longitude <= max_lon
            ):
                satellite_lists.append(posi_obj.name)
        return satellite_lists
