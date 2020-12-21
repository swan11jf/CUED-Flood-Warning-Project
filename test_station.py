# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
import floodsystem.station as station


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    #Create a station with invalid data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert not s.typical_range_consistent()
    #Change range to be another type of inconsistent
    s.typical_range = (3,-2)

    assert not s.typical_range_consistent()
    #Change range to be consistent
    s.typical_range = (-2,3)

    assert s.typical_range_consistent()

def test_readable_risk():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (6.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.flood_risk_factor = None
    assert s.readable_risk() == "Unknown"
    s.flood_risk_factor = 0.25 - 0.01
    assert s.readable_risk() == "Low"
    s.flood_risk_factor = 0.25 * 2.5 - 0.01
    assert s.readable_risk() == "Moderate"
    s.flood_risk_factor = 0.25 * 4 - 0.01
    assert s.readable_risk() == "High"
    s.flood_risk_factor = 0.25 * 4 + 0.01
    assert s.readable_risk() == "Severe"

def test_inconsistent_typical_range_stations():
    #Create station with inconsistent range
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (6.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    trange = (-1,2)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s,s1]

    assert len(station.inconsistent_typical_range_stations(stations)) ==1

def test_relative_water_level():
    #Create station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (2, 3)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.relative_water_level() is None

    s.latest_level = s.typical_range[0]

    assert round(s.relative_water_level()) == 0

    s.latest_level = s.typical_range[1]

    assert round(s.relative_water_level()) == 1