import floodsystem.flood as flood
from floodsystem.station import MonitoringStation

"""Unit test for floods"""

def test_stations_level_over_threshold():
    # Create station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (2, 3)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    #Set latest level at 0.5 relative level
    s.latest_level = (s.typical_range[0] + s.typical_range[1]) / 2
    s1.latest_level = s.typical_range[0]
    stations = [s,s1]

    assert len(flood.stations_level_over_threshold(stations, 0.4)) == 1

def test_stations_highest_rel_level():
    # Create stations
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (2, 3)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    #Insert latest relative
    s1.latest_level = (trange[0] + trange[1]) / 2
    s2.latest_level = (trange[0] + trange[1]) / 3

    stations = [s1,s2]

    high_stations = flood.stations_highest_rel_level(stations,1)
    assert len(high_stations) == 1
    assert high_stations[0] == s1