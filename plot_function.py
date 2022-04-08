from math import sin, cos, tan, asin, acos, atan, log
import numpy as np
from matplotlib import pyplot as plt
import os

def function(expression, x_value):
  # py_expression = expression.replace('^', '**')
  f = lambda x: eval(expression)
  return f(x_value)

def draw_graph(expression, FILE_NAME):
  RANGE = 20
  x_range = np.arange(-RANGE, RANGE, 0.1)
  y_range = np.array([function(expression, x) for x in x_range])
  plt.clf()
  ax = plt.gca()
  ax.spines['top'].set_color('none')
  ax.spines['bottom'].set_position('zero')
  ax.spines['left'].set_position('zero')
  ax.spines['right'].set_color('none')
  plt.plot(x_range, y_range)
  plt.savefig(FILE_NAME)

if __name__ == "__main__":
  draw_graph("x**2", 'graph.png')