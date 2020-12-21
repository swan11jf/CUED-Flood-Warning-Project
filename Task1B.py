from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    stations = build_station_list()
    sorted_stations = stations_by_distance(stations, (52.2053, 0.1218))
    print('Closest Stations: ', [(x[0].name, x[0].town, x[1]) for x in sorted_stations[:10]])
    print('Furthest Stations: ', [(x[0].name, x[0].town, x[1]) for x in sorted_stations[-10:]])

if __name__ == '__main__':
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()