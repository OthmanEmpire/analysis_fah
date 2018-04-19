Analysis FAH: A Glimpse at Folding@Home Leaderboards (rankings)
----------------------------------------------------------------
Here we perform some quick analysis to study the behaviour of
the Folding@Home leaderboards. The goal is to gain some intuition
of how difficult it is to climb the leaderboards.

There are two plots of interest shown below. The first is the
plot of the raw data from 2016-01-07 (when exporting the entire
leaderboards was available which it no longer is). The second plot
uses the same data as the first but with some cleansing.

Both plots have the same axis, Points vs Global Rank, and are
plotted on a linear-log graph. Transparency is used to give
a measure of data point density (i.e. the red line in the plots below
is more opaque in regions where less data is available).


Raw Data Plot
-------------
![](plot_raw_(07-01-2016).png)

Points of interest:

- Given that this data reflects leaderboards, the only time
when two users could have the same global rank is if they exactly have
the same number of points. However, if we examine the raw data
(red line) between 1,500,000 and 1,750,000, there exists data points
that contradict that statement. There are data points with identical
number of points but differ in global rankings. The reason behind
this behaviour is unknown and is most likely tied to the ranking
algorithm that FAH uses. Notice that the raw data file contains
roughly 5,000,000 entries but the leaderboard only starts from
near 2,000,000. This is where users are 'crunched' in.

- The difference between successive ranks plot (green line) is
calculated from the raw data. It contains spikes due to the natural
variation fo the raw data. However, there is one particularly large
spike that needs to be filtered, cause by several missing data points.

- There exist many dummy or abandoned user accounts in the leaderboards.
The 'real' leaderboards most likely begin from 500,000 and better. This is
because ranks worse than 500,000 require at most 1 point to progress to a
subsequent rank and even low end machines can produce at least 100 points
per day.

- The leaderboards behaves like a e^e^x function at glance. As the scale
used to plot is linear-log, thus any exponential growth is suppressed in the
y-axis, it still visually looks like an exponential graph.


Cleansed Data Plot
------------------
![](plot_cleansed_(07-01-2016).png)

Points of interest:
- Global ranks above 1,000,000 have a lot of points removed because of log graph
- Rolling median(10) then rolling median(20)... Therefore?

Conclusion
----------
- Climbing from X to Y is fast due to many fake ranks
- Climbing from Y to Z is steady exponentional growth (steady difficulty?)
- Climbing from Z to A is asymptotic



Requirements
------------
See `requirements.txt`.

Author
-------
Othman Alikhan, oz.alikhan@gmail.com
