Analysis FAH: A Glimpse at Folding@Home Leaderboards (rankings)
----------------------------------------------------------------
Here we perform some quick analysis to study the behaviour of
the Folding@Home leaderboards. The goal is to gain some intuition
of how difficult it is to climb the leaderboards.


Data
----
There are two plots of interest shown below. The first is the
plot of the raw data from 2016-01-07 (when exporting the entire
leaderboards was available which it no longer is). The second plot
uses the same data as the first but with some cleansing.

Both plots have the same axis, Points vs Global Rank, and are
plotted on a linear-log graph. Transparency is used to give
a measure of data point density (i.e. the red line in the plots below
is more opaque in regions where less data is available).


Plot - Raw Data
---------------
![](plot_raw_(07-01-2016).png)

Points of interest:

- Given that this data reflects leaderboards, the only time
when two users could have the same global rank is if they exactly have
the same number of points. However, if we examine the raw data
(red line) between 1,500,000 and 1,750,000, there exists data points
that contradict that statement. There are data points with identical
number of points but differ in global rankings. The reason behind
this behaviour is unknown and is most likely tied to the ranking
algorithm that FAH uses.

- The difference between successive ranks plot (green line) is
calculated from the raw data. It contains spikes due to the natural
variation of the raw data. However, there is one particularly large
spike that needs to be filtered, cause by consecutive missing data points.

- There exist many dummy or abandoned user accounts in the leaderboards.
The 'real' leaderboards most likely begin from 500,000 and better. This is
because ranks worse than 500,000 require at most 1 point to progress to a
subsequent rank and even low end machines can produce at least 100 points
per day.

- The plotted curve behaves like an exp(exp(x)) function at glance; the
scale used is linear-log thus any exponential growth is suppressed in the
y-axis yet it still visually looks like an exponential graph.


Plot - Cleansed Data
--------------------
![](plot_cleansed_(07-01-2016).png)

Points of interest:

- After applying a filter on the the raw data (removing data points with the
same number of points but differing global rankings), the data points are
more concentrated at rank 500,000 and better. This supports the theory
that the 'real' leaderboards begins at 500,000.

- After applying a rolling median (10 data points wide) and then a rolling mean
(20 data points wide), the difference between successive ranks (green line) is
visually similar to the curve above it (red line). Given also that the green
line is its derivative, this implies that the curve (red line) obeys an
exponential function since the derivative of an exponential function is
proportional to itself.


Conclusion
----------
- Climbing the rankings from 1,750,000 to 500,000 should be quick due to many
dummy or abandoned user accounts.
- Climbing the rankings from 500,000 to 1 seems to obey a exp(exp(x)) function
thus the difficulty rapidly escalates over that interval.


Author
-------
Othman Alikhan, oz.alikhan@gmail.com
