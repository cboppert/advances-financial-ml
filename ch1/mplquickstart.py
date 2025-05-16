# Let's import matplotlib and futz around with the quick start
# https://matplotlib.org/stable/users/explain/quick_start.html#quick-start

# If you come in here in 6 months... activate your python venv - `source py-venv/bin/activate`
# `python mplquickstart

import matplotlib.pyplot as plt
import numpy as np

# Matplotlib plots on Figures
# Which have Axes

def showPlot():
  # fig - Figure - keeps track of Axes, and Artists
  # ax - Axes - Artist attached to Figure. Contains a region in 2 or 3D (generally) for plotting data
  # There are also Axis with scales, limits, ticks and ticklabels.
  fig, ax = plt.subplots() # Create Figure containing single Axes
  ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) # Plot some data on the Axes
  plt.show() # Show the figure

# Plots expect numpy.array or numpy.ma.masked_array inputs
# "Array like" data such as Pandas data and numpy.matrix may not work
# Convert to nmupy arrays first

def getMoreInterestingPlot():
  # Deterministic prng
  np.random.seed(518716)
  # arange returns evenly spaced values within a given range
  data = { 'a': np.arange(50),
           'c': np.random.randint(0, 50, 50),
           'd': np.random.randn(50)}
  data['b'] = data['a'] + 10 * np.random.randn(50)
  data['d'] = np.abs(data['d']) * 100

  fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
  ax.scatter('a', 'b', c='c', s='d', data=data)
  ax.set_xlabel('entry a')
  ax.set_ylabel('entry b')

  plt.show()


# Explicit and Implicit Coding Styles

# Explicitly create Figures and Axes and call methods on them (Object Oriented (OO) style)

def explicitStyle():
  x = np.linspace(0, 2, 100)
  
  fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
  ax.plot(x, x, label='linear')
  ax.plot(x, x**2, label='quadratic')
  ax.plot(x, x**3, label='cubic')
  ax.set_xlabel('x label')
  ax.set_ylabel('y label')
  ax.set_title("Simple plot")
  ax.legend()

  plt.show()

# Work with pyplot to implicitly create/manage Figures and Axes, and use pyplot functions to plot

def pyplotStyle():
  x = np.linspace(0, 2, 100)
  
  plt.figure(figsize=(5, 2.7), layout='constrained')
  plt.plot(x, x, label='linear')
  plt.plot(x, x**2, label='quadratic')
  plt.plot(x, x**3, label='cubic')

  plt.xlabel('x label')
  plt.ylabel('y label')
  plt.title("Simple plot")
  plt.legend()

  plt.show()

# helpers

def my_plotter(ax, data1, data2, param_dict):
  """
  A helper function to make a graph
  """
  # Are we dereferencing?
  out = ax.plot(data1, data2, **param_dict)
  return out

def callingHelper():
  data1, data2, data3, data4, = np.random.randn(4, 100)
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
  my_plotter(ax1, data1, data2, {'marker': 'x'})
  my_plotter(ax2, data3, data4, {'marker': 'o'})

  plt.show()

def styles():
  data1, data2, data3, data4, = np.random.randn(4, 100)
  fig, ax = plt.subplots(figsize=(5, 2.7))
  x = np.arange(len(data1))
  ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
  l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
  l.set_linestyle(':')

  plt.show()


# Have to close each plot to get to the next plot
# showPlot()
# getMoreInterestingPlot()
# explicitStyle()
# pyplotStyle()

callingHelper()
styles()
