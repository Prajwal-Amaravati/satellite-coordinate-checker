from datetime import datetime, timezone

from pyproj import Proj, Transformer
from sgp4.api import Satrec, jday

from models.sate_lat_lon_data import SateLatLonData


class GetLatLonofSatellite:
    """returns list of lat lon of the satellites passes, the line1, line2 are passed to sgp4 api,
    for a particular date given by user we calculate the lan lon present on earth
    """

    def get_lat_lon(self, sate_obj):
        """get lat long og the satellite

        Args:
            sate_obj (list): object og the satellite

        Raises:
            RuntimeError: error if the error_code is 0

        Returns:
            list: Satelatlondata
        """

        satellite = Satrec.twoline2rv(sate_obj.line1, sate_obj.line2)
        now = datetime.now(timezone.utc)
        julian_date, fractional_part = jday(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second + now.microsecond / 1e6,
        )
        error_code, position_velocity, velocity_vector = satellite.sgp4(
            julian_date, fractional_part
        )
        if error_code != 0:
            raise RuntimeError(f"SGP4 propagation error: {error_code}")
        x_coord, y_coord, z_coord = position_velocity

        ecef_proj = Proj(proj="geocent", datum="WGS84")
        wgs84 = Proj(proj="latlong", datum="WGS84")

        transformer = Transformer.from_proj(ecef_proj, wgs84)
        longitude, latitude, altitude = transformer.transform(x_coord, y_coord, z_coord)
        sate_obj.name, longitude, latitude, altitude
        return SateLatLonData(
            name=sate_obj.name,
            latitude=latitude,
            longitude=longitude,
            altitude=altitude,
        )
