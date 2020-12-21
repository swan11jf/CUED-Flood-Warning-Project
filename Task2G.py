from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import *
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations_by_risk = stations_by_risk_level(stations)
    flood_risks = [x.flood_risk_factor for x in stations_by_risk]
    print("Median: ", np.median(flood_risks))
    print("Last Octile: ", np.percentile(flood_risks,100-12.5))
    print("First Quartile: ", np.percentile(flood_risks,25))
    print("Third Quartile: ", np.percentile(flood_risks,75))
    print()
    print("Stations with highest risk of flooding:")
    for station in stations_by_risk:
        if station.readable_risk() != "Severe":
            break
        else:
            print(station.name + ", " + ("_____ " if station.town is None else station.town) + ": ", station.readable_risk() + " | " + str(station.flood_risk_factor))
    pass


if __name__ == '__main__':
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()