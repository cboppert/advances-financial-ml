# Let's import matplotlib and futz around with the quick start
# https://matplotlib.org/stable/users/explain/quick_start.html#quick-start

import matplotlib.pyplat as plt
import numpy as np

# Matplotlib plots on Figures
# Which have Axes

def showPlot():
  fig, ax = plt.subplots() # Create Figure containing single Axes
  ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) # Plot some data on the Axes
  plt.show() # Show the figure
