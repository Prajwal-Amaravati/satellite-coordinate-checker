from typing import List

from models.two_element_line import TwoElementLine


class GetOjectsFromFile:
    """convert the files from the .txt and return as objects"""

    def __init__(self, filepath: str) -> None:
        self.filename = filepath

    def read_tle_file(self):
        """returns the list of elements from the file

        Returns:
            list: file paths
        """
        tle_data = []
        with open(self.file_path, "r") as file:
            tle_lines = []
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    tle_lines.append(stripped_line)
                    if len(tle_lines) == 3:
                        name, line1, line2 = tle_lines
                        tle_data.append({"name": name, "line1": line1, "line2": line2})
                        tle_lines = []
        return [TwoElementLine(**tle) for tle in tle_data]
