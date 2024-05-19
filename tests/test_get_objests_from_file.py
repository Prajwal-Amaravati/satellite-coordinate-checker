import pytest
from unittest.mock import mock_open, patch
from models.two_element_line import TwoElementLine
from get_objects_from_file import GetOjectsFromFile 

class TestGetObjectsFromFile:
    
    def test_read_tle_file():
        mock_file_content = """Satellite 1
        1 25544U 98067A   23055.36715531  .00017001  00000+0  31285-3 0  9996
        2 25544  51.6387 167.3561 0005418  22.9195  99.0673 15.49284681384295
        Satellite 2
        1 25545U 98067B   23055.36715531  .00017002  00000+0  31285-3 0  9997
        2 25545  51.6388 167.3562 0005419  22.9196  99.0674 15.49284681384296
        """

        # Mock the open function in the GetOjectsFromFile class's module
        with patch("get_objects_from_file.open", mock_open(read_data=mock_file_content)) as mocked_file:
            filepath = "dummy_path.txt"
            get_objects_from_file = GetOjectsFromFile(filepath)
            result = get_objects_from_file.read_tle_file()

            # Assert the file was opened with the correct filepath
            mocked_file.assert_called_once_with(filepath, "r")

            # Assert the results
            expected_result = [
                TwoElementLine(
                    name="Satellite 1",
                    line1="1 25544U 98067A   23055.36715531  .00017001  00000+0  31285-3 0  9996",
                    line2="2 25544  51.6387 167.3561 0005418  22.9195  99.0673 15.49284681384295",
                ),
                TwoElementLine(
                    name="Satellite 2",
                    line1="1 25545U 98067B   23055.36715531  .00017002  00000+0  31285-3 0  9997",
                    line2="2 25545  51.6388 167.3562 0005419  22.9196  99.0674 15.49284681384296",
                ),
            ]

            assert result == expected_result

