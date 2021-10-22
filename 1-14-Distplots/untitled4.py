import numpy as np
import plotly.offline as pyo
import plotly.figure_factory as ff

"""
x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

hist_data = [x1, x2, x3 ,x4]
group_labels = ["X111", "X222","X333","X444"]

fig = ff.create_distplot(hist_data, group_labels,
                         bin_size=[0.2,0.1,0.3,0.4])

pyo.plot(fig)
"""

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

hist_data = [snodgrass, twain]
group_labels = ["Snodgrass", "MT"]

fig = ff.create_distplot(hist_data, group_labels,
                         bin_size=[0.005, 0.005])

pyo.plot(fig)