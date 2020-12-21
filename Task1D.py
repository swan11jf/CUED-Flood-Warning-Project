from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    rivers_sorted = sorted(rivers)
    print(rivers_sorted[:10])
    print()
    dict = stations_by_river(stations)

    check_rivers = ['River Aire', 'River Cam', 'River Thames']
    for check_river in check_rivers:
        list1 = dict[check_river]
        station_names = [x.name for x in list1]
        station_names = sorted(station_names)
        print(station_names)

if __name__ == '__main__':
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()