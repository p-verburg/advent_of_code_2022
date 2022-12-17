from shapely import MultiPolygon, Point
from shapely.geometry import Polygon

from navigation.beaconmap import calculate_sensor_ranges


def find_uncharted_zone(sensor_list, boundaries):
    min_x, max_x, min_y, max_y = boundaries

    uncovered_polygon = Polygon([(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)])

    sensor_list = calculate_sensor_ranges(sensor_list)
    for sensor, _, sensor_range in sensor_list:
        sensor_polygon = Polygon([(sensor.x - sensor_range, sensor.y),
                                  (sensor.x, sensor.y + sensor_range),
                                  (sensor.x + sensor_range, sensor.y),
                                  (sensor.x, sensor.y - sensor_range)])
        uncovered_polygon = uncovered_polygon - sensor_polygon

    return uncovered_polygon


def find_points_in_polygon(polygon):
    if polygon.is_empty:
        return []

    (min_x, min_y, max_x, max_y) = polygon.bounds

    def round_up(coordinate):
        if coordinate == float(int(coordinate)):
            return int(coordinate)
        return int(coordinate) + 1

    def round_down(coordinate):
        if coordinate == float(int(coordinate)):
            return int(coordinate)
        return int(coordinate)

    min_x = round_up(min_x)
    min_y = round_up(min_y)
    max_x = round_down(max_x)
    max_y = round_down(max_y)

    points = []

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            point = Point(x, y)
            if polygon.contains(point):
                points.append(point)

    return points


def find_points_in_polygons(polygons):
    if isinstance(polygons, Polygon):
        return find_points_in_polygon(polygons)
    if isinstance(polygons, MultiPolygon):
        return find_points_in_polygons(list(polygons.geoms))
    if isinstance(polygons, list):
        points = []
        for polygon in polygons:
            polygon_points = find_points_in_polygons(polygon)
            if polygon_points and isinstance(polygon_points, list):
                points.extend(polygon_points)
        return points
    return []
