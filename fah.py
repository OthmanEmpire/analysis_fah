"""
Creates graphs that provide insight to the behaviour of Folding@Home
leaderboards.

In particular, the following is examined:
        - User rank vs Points
        - Difference between successive ranks vs Points

With the objective of understanding how difficult it is to climb
the leaderboards (i.e. is it a linear function? logarithmic? or
otherwise?).
"""


__author__ = "Othman Alikhan"
__email__ = "oz.alikhan@gmail.com"


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plotRawData(df):
    """
    Plots the raw FAH statistics.

    In particular, the following lines should be plotted:
        - User rank vs Points
        - Difference between successive ranks vs Points
    """
    title = "Folding@Home"
    fileName = "Folding@Home_Statistics (07-01-2016)"

    # Creating the plots
    fig = plt.figure()
    fig.canvas.set_window_title(fileName)
    subplot = fig.add_subplot(111)

    # Plotting the raw data
    subplot.scatter(df.index,
                    df["points"],
                    color="r",
                    label="Raw data",
                    s=1,
                    alpha=0.1)

    # Plotting diff data
    diff = df
    diff["points"] = diff["points"].diff(-1)
    subplot.plot(diff.index,
                 diff["points"],
                 color="g",
                 label="Difference between successive ranks",
                 linewidth=1)

    # Adjusting graph settings
    _adjustPlotSettings(subplot, title)
    plt.show()


def plotCleansedData(df):
    """
    Plots FAH statistics after some data cleansing.

    In particular, the following lines should be plotted:
        - User rank vs Points
        - Difference between successive ranks vs Points
    """
    title = "Folding@Home"
    fileName = "Folding@Home_Statistics (07-01-2016)"

    # Creating the plots
    fig = plt.figure()
    fig.canvas.set_window_title(fileName)
    subplot = fig.add_subplot(111)

    # Plotting the raw data
    df = df[~df.index.duplicated(keep="first")]
    df = df[~df["points"].duplicated(keep="first")]
    df = df.dropna()
    subplot.scatter(df.index,
                    df["points"],
                    color="r",
                    label="Raw data (with some data cleansing)",
                    s=1,
                    alpha=0.1)

    # Plotting diff data
    diff = df
    diff["points"] = diff["points"].diff(-1)
    diff = diff.rolling(10).median()
    diff = diff.rolling(20).mean()
    subplot.plot(diff.index,
                 diff["points"],
                 color="g",
                 label="Difference between successive ranks (averaged)",
                 linewidth=1)

    _adjustPlotSettings(subplot, title)
    plt.show()


def _adjustPlotSettings(plot, title):
    """
    Adjusts the plot settings to be more visually clearer.

    :param plot: matplotlib Axes, the object used to plot.
    :param title: String, the title of the plot.
    """
    # Adjusting graph settings
    plt.title(title, fontweight="bold")
    plt.legend(loc='upper right', fontsize=12)
    plt.xlabel('Global Rank (Linear)')
    plt.ylabel('Points (Log)')
    plot.set_yscale("log", basey=10)

    # Allows better visibility of the graph
    plt.yticks([10**n for n in range(11)])
    plt.xticks(np.arange(0, 2*(10**6), 2.5*(10**5)))
    plt.ylim(1, 2*plt.ylim()[1])
    plt.xlim(-10000, plt.xlim()[1])


def main():
    """
    Main point of execution (runs the program).
    """
    csvFile = "input_data_(07-01-2016).csv"
    df = pd.read_csv(csvFile, index_col=0)
    plotCleansedData(df)
    plotRawData(df)


if __name__ == "__main__":
    main()
