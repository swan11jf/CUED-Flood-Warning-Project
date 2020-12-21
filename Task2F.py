import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    stations = build_station_list()
    update_water_levels(stations)
    top_stations = stations_highest_rel_level(stations, N=5)

    stations_top_stations = []
    for entry in top_stations:
        for station in stations:
            if entry.name == station.name:
                stations_top_stations.append(station)

    for station in stations_top_stations:
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == '__main__':
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()