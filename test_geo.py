from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo
from floodsystem.station import MonitoringStation
import haversine

"""Unit test for geo module"""

def test_stations_by_distance():
    #Builds station list
    stations = build_station_list()
    centre = (0,0)
    sorted_stations = geo.stations_by_distance(stations, centre)

    #Checks that list exists and in order
    assert len(sorted_stations) > 0
    for i in range(1, len(sorted_stations)):
        assert sorted_stations[i][1] >= sorted_stations[i-1][1]

def test_stations_within_radius():
    #Builds station list
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord1 = (6.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord1, trange, river, town)
    coord2 = (1000,1000)
    s1 = MonitoringStation(s_id, m_id, label, coord2, trange, river, town)
    stations = [s,s1]
    centre = (0, 0)
    radius = haversine.haversine(centre, coord1, haversine.Unit.KILOMETERS) + 1
    radius_stations = geo.stations_within_radius(stations,centre,radius)

    #Checks that list exists
    assert len(radius_stations) == 1
    assert radius_stations[0] == s

def test_river_with_station():

    # builds stations and list of rivers
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (6.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River X"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Y"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Y"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Z"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s, s1, s2, s3, s4]
    rivers = geo.rivers_with_station(stations)

    #Makes sure that data processing is valid
    assert rivers is not None
    assert len(rivers) == 3
    assert "River X" in rivers
    assert "River Y" in rivers
    assert "River Z" in rivers

def test_stations_by_river():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (6.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Y"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s, s1]
    dict = geo.stations_by_river(stations)

    assert len(dict["River X"]) == 1
    assert len(dict["River Y"]) == 1

def rivers_by_station_number():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (6.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River X"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Y"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Y"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Z"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s, s1,s2,s3,s4]
    N = 2
    output_list = geo.rivers_by_station_number(stations, N)

    assert len(output_list) == 3

    for i in range(1, len(output_list)):
        assert output_list[i][1] >= output_list[i-1][1]