from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """
    Creates a list of stations from the inputted list that have a relative water level over the threshold

    :param stations: A list of stations to be tested
    :param tol: The threshold to be compared against
    :return: A list of tuples with (station, relative water level) that have relative water levels that exceed the tol
    """
    stations_over = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None:
            if relative_level > tol:
                stations_over.append((station, station.relative_water_level()))
    return stations_over

def stations_highest_rel_level(stations, N):
    """
    Sorts list of stations by highest to lowest relative water level and returns highest N stations

    :param stations: Stations to be sorted
    :param N: Number of stations to be returned
    :return: List of N stations with highest relative water level
    """
    stations_level = []
    for station in stations:
        if station.relative_water_level() is not None:
            stations_level.append((station,station.relative_water_level()))
    sorted_levels = sorted_by_key(stations_level, 1, True)
    return [x[0] for x in sorted_levels[:N]]