# -*- coding: utf-8 -*-
"""
A quick demo analysis of the Kentucky Derby data.
"""

import os
import statistics

from matplotlib import pyplot
import numpy  # noqa: F401
import pandas
import seaborn
import statsmodels.formula.api as smf


# %% Helper function

def print_section(content, title):
    """Print some output as a neat section with title.
    """

    header = '#### {} ####'.format(title)
    print(header, content, sep='\n\n', end='\n\n\n')


# %% Load

filepath = os.path.join('data', 'kentucky_derby.csv')
kd = pandas.read_csv(filepath)

print_section(kd, 'Data frame')


# %% Explore

# In what year was the distance of the derby changed?
time_periods = kd.groupby('Version').aggregate({'Year': [min, max]})
print_section(time_periods, 'Time periods of derby versions')

# Which horse in which year was the fastest?
max_speed = max(kd['Speed'])
best_horse = kd[kd['Speed'] == max_speed]
print_section(best_horse, 'Fastest horse ever')

# Summarize the winning speeds for the two versions of the race.
summary_stats = [min, statistics.median, statistics.mean, statistics.stdev, max]
summary = kd.groupby('Version').aggregate({'Speed': summary_stats})
print_section(summary, 'Distribution of winning speeds')


# %% Visualize

# Full labels for figure axes.
label_time = 'Winning time (s)'
label_speed = 'Winning speed (mph)'

# Show the difference in winning times for the two versions of the race.
seaborn.boxplot(x='Version', y='Time', data=kd)
pyplot.ylabel(label_time)
pyplot.show()

# Show that this difference reverses if we consider instead winning *speed*.
seaborn.boxplot(x='Version', y='Speed', data=kd)
pyplot.ylabel(label_speed)
pyplot.show()

# Show the increase in winning speeds over the years.
seaborn.scatterplot(x='Year', y='Speed', hue='Version', data=kd)
pyplot.ylabel(label_speed)
pyplot.show()


# %% Linear model

formula_linear = 'Speed ~ 1 + Year'

# Summary.
m_linear = smf.ols(formula_linear, data=kd).fit()
print_section(m_linear.summary(), 'Model: '+formula_linear)

# Plot.
seaborn.lmplot(x='Year', y='Speed', data=kd)
pyplot.title(formula_linear)
pyplot.ylabel(label_speed)
pyplot.show()


# %% Polynomial model.

degree = 2
formula_poly = 'Speed ~ 1 + Year + numpy.power(Year, {})'.format(degree)

# Summary.
m_poly = smf.ols(formula_poly, data=kd).fit()
print_section(m_poly.summary(), 'Model: '+formula_poly)

# Plot.
seaborn.lmplot(x='Year', y='Speed', data=kd, order=degree)
pyplot.title(formula_poly)
pyplot.ylabel(label_speed)
pyplot.show()
