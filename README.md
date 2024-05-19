## Satellite Coordinate Checker

This project allows you to determine which satellites are within a specified rectangular area on the Earth. The application reads satellite data from a Two-Line Element (TLE) file, calculates the latitude and longitude of each satellite, and checks if these coordinates fall within the specified rectangle.

Installation
# 1. Clone the repository:
```
git clone https://github.com/prajwal-amaravati/satellite-coordinate-checker.git
cd satellite-coordinate-checker

```
# 2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate 
```
# 3. Install the required dependencies:
```
pip install -r requirements.txt

```

##  Usage
# Command Line Arguments
```
--left_top_coordinate or -ltc: The top left coordinate of the rectangle (default: "0,0").
--left_bottom_coordinate or -lbc: The bottom left coordinate of the rectangle (default: "0,0").
--right_top_coordinate or -rtc: The top right coordinate of the rectangle (default: "0,0").
--right_bottom_coordinate or -rbc: The bottom right coordinate of the rectangle (default: "0,0").
```
# Example

To run the application with custom coordinates, use the following command:
```
python get_list_of_satellites_within_range.py -ltc "50,-90" -lbc "50,-85" -rtc "55,-90" -rbc "55,-85"
```

## Running Tests
To run tests for the application, you will need to have pytest installed. If it is not already installed, you can install it using:
```
pip install pytest
```
# Running Tests
Execute the following command to run the tests:
```
pytest -v
```