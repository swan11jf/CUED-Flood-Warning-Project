from datetime import datetime
from floodsystem.analysis import polyfit, determine_numerical_risk, stations_by_risk_level
from floodsystem.station import MonitoringStation


def test_polyfit():
    dates = [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)]
    levels = [4, 5, 6]

    poly, d0 = polyfit(dates, levels, 1)
    assert round(poly(0.1),1) == 4.1
    assert d0 == 737425

def test_determine_numerical_risk():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0, 1) # because trange is 0,1 relative range is equal to latest level
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "some station 1"
    river = "River Y"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "some station 4"
    river = "River A"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "some station 5"
    river = "River A"
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s.latest_level = 0.4
    s1.latest_level = 0.75

    s4.latest_level = 4
    s5.latest_level = 0

    stations = [s,s1,s4,s5]
    determine_numerical_risk(stations)

    assert round(s.flood_risk_factor,1) == round(0.4 * 0.5 - 0.1,1)
    assert round(s1.flood_risk_factor,3) == round(0.75 * 0.5 + (0.75- 0.5),3)
    assert round(s5.flood_risk_factor) == round((4+0)/2 - 0.5)

def test_stations_by_risk_level():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0, 1)  # because trange is 0,1 relative range is equal to latest level
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "some station 1"
    river = "River Y"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "some station 4"
    river = "River A"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "some station 5"
    river = "River A"
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s.latest_level = 0.4
    s1.latest_level = 0.75

    s4.latest_level = 4
    s5.latest_level = 0

    stations = [s, s1, s4, s5]
    correct_order = [s4,s5,s1,s]
    ordered_stations = stations_by_risk_level(stations)

    for i in range(0, len(correct_order)):
        assert correct_order[i] == ordered_stations[i]



