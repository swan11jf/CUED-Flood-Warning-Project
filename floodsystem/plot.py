import matplotlib.pyplot as plt
import matplotlib
from .datafetcher import fetch_measure_levels
from .analysis import polyfit
import numpy as np


def plot_water_levels(station, dates, levels):
    """Plots water levels for given dates and shows the typical low and high levels."""

    plt.plot(dates, levels, color='mediumslateblue', label="$Water Level$")
    plt.plot([dates[-1], dates[0]], [station.typical_range[0], station.typical_range[0]], color='lightsalmon', label="$Typical Low$")
    plt.plot([dates[-1], dates[0]], [station.typical_range[1], station.typical_range[1]], color='forestgreen', label="$Typical High$")

    plt.xlabel('Date')
    plt.xticks(rotation=90)
    plt.ylabel('Water level (m)')
    plt.title(str(station.name) + ' Station Water Level')

    plt.legend()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots water levels with polynomial fit."""

    poly, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)

    plt.plot(dates, levels)

    x1 = np.linspace(x[0], x[-1])
    plt.plot(x1, poly(x1 - d0))

    plt.xlabel('Date')
    plt.xticks(rotation=90)
    plt.ylabel('Water level/ m')
    plt.title(station.name)

    plt.show()