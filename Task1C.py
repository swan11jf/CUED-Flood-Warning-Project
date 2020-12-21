from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()
    stations_near_cambridge = stations_within_radius(stations, (52.2053, 0.1218), 10)
    station_names = [x.name for x in stations_near_cambridge]
    print(station_names)

if __name__ == '__main__':
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()