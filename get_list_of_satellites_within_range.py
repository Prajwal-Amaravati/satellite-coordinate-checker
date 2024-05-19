import argparse

from get_lat_lon_of_satellite import GetLatLonofSatellite
from get_objects_from_file import GetOjectsFromFile
from position_of_point_in_rectangle import PositionofPointinRectangle

from .utils import multiprocess_func


class GetListofSatellitesWithinRange:
    """module by passing the list of coordinate"""

    def __init__(self, args) -> None:
        # pass the file path here
        self.file_path = "3000sats.txt"
        for key, value in vars(args).items():
            setattr(self, key, value)

    def main(self):
        """prints the lists of satellites within the rectangular coordinates"""
        tle_data = GetOjectsFromFile().read_tle_file(file_path=self.file_path)
        sate_obj_multi_data = multiprocess_func(
            GetLatLonofSatellite().get_lat_lon(), tle_data
        )
        position_obj_data = [
            item
            for sublist in sate_obj_multi_data
            for item in sublist
            if not item.empty
        ]

        list_of_satellites_within_coordinates_multi = multiprocess_func(
            PositionofPointinRectangle(
                rectangle_coords=self._get_rect_coord()
            ).is_point_in_rectangle(),
            position_obj_data,
        )
        list_of_satellites_within_coordinates = [
            item
            for sublist in list_of_satellites_within_coordinates_multi
            for item in sublist
            if not item.empty
        ]
        print(
            "The list of Satellites within the coordinates given are",
            list_of_satellites_within_coordinates,
        )

    def _get_rect_coord(self):
        """_summary_

        Returns:
            list: rectangle coordinate
        """
        return [
            tuple(self.left_top_coordinate),
            tuple(self.left_bottom_coordinate),
            tuple(self.right_top_coordinate),
            tuple(self.right_bottom_coordinate),
        ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-ltc", "--left_top_coordinate", type=str, required=False, default="0,0"
    )
    parser.add_argument(
        "-lbc", "--left_bottom_coordinate", type=str, required=False, default="0,0"
    )
    parser.add_argument(
        "-rtc", "--right_top_coordinate", type=str, required=False, default="0,0"
    )
    parser.add_argument(
        "-rbc", "--right_bottom_coordinate", type=str, required=False, default="0,0"
    )
    args = parser.parse_args()

    obj = GetListofSatellitesWithinRange(args)
    obj.main()
