# -*- coding: utf-8 -*-
"""
This example demonstrates the use of GLSurfacePlotItem.
"""

## Add path to library (just for examples; you do not need this)
# import initExample

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import matplotlib.pyplot as plt

## Create a GL View widget to display data
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
w.setCameraPosition(distance=300)

## Add a grid to the view
g = gl.GLGridItem()
g.setSize(10,10,1)
g.scale(20, 20, 1)
g.setDepthValue(100)  # draw grid after surfaces since they may be translucent
w.addItem(g)

wave = pg.PlotWidget(QtGui.QColor(0, 0, 0, 0))
wave.plot([1,2,3], [1,2,1], pen=(0,0,255), fillLevel=-0, brush=(255,215,0))
w.addItem(wave)
a=gl.GLAxisItem()
a.setSize(100,1,1)
a.translate(0,0,10)
w.addItem(a)


## Simple surface plot example
## x, y values are not specified, so assumed to be 0:50
# z = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
# p1 = gl.GLSurfacePlotItem(z=z, shader='shaded', color=(0.5, 0.5, 1, 1))
# p1.scale(16. / 49., 16. / 49., 1.0)
# p1.translate(-18, 2, 0)
# w.addItem(p1)

# Saddle example with x and y specified
# x = np.linspace(-8, 8, 50)
# y = np.linspace(-8, 8, 50)
# z = 0.1 * ((x.reshape(50, 1) ** 2) - (y.reshape(1, 50) ** 2))
# p2 = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader='normalColor')
# p2.translate(-10, -10, 0)
# w.addItem(p2)

# # Manually specified colors
# z = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
# x = np.linspace(-12, 12, 50)
# y = np.linspace(-12, 12, 50)
# colors = np.ones((50, 50, 4), dtype=float)
# colors[..., 0] = np.clip(np.cos(((x.reshape(50, 1) ** 2) + (y.reshape(1, 50) ** 2)) ** 0.5), 0, 1)
# colors[..., 1] = colors[..., 0]
#
# p3 = gl.GLSurfacePlotItem(z=z, colors=colors.reshape(50 * 50, 4), shader='shaded', smooth=False)
# p3.scale(16. / 49., 16. / 49., 1.0)
# p3.translate(2, -18, 0)
# w.addItem(p3)

## Animated example
## compute surface vertex data
# cols = 90
# rows = 100
# x = np.linspace(-8, 8, cols + 1).reshape(cols + 1, 1)
# y = np.linspace(-8, 8, rows + 1).reshape(1, rows + 1)
# d = (x ** 2 + y ** 2) * 0.1
# d2 = d ** 0.5 + 0.1

## precompute height values for all frames
# phi = np.arange(0, np.pi * 2, np.pi / 20.)
# z = np.sin(d[np.newaxis, ...] + phi.reshape(phi.shape[0], 1, 1)) / d2[np.newaxis, ...]

## create a surface plot, tell it to use the 'heightColor' shader
## since this does not require normal vectors to render (thus we
## can set computeNormals=False to save time when the mesh updates)
# y = np.linspace(0, 100, 100)
#
# x = np.linspace(0,100, 100)
# z = np.random.rand(len(x),len(y))*100
#
# cmap = plt.get_cmap('jet')
# minZ=np.min(z)
# maxZ=np.max(z)
# rgba_img = cmap((z-minZ)/(maxZ -minZ))
# p4 = gl.GLSurfacePlotItem(x=x,y=y,z=z,colors=rgba_img)
#
# # p4 = gl.GLSurfacePlotItem(x=x[:, 0], y=y[0, :], shader='heightColor', computeNormals=False, smooth=False)
# # p4.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
# # p4.shader()['colorMap'] = np.array([0.45, 0, 0.1, 0.005, 0.5, 2, 0, 0.05, 0.2])
# p4.translate(10, 10, 0)
# w.addItem(p4)


zz = pg.gaussianFilter(np.zeros([200,200]), (1, 1))

wang = gl.GLSurfacePlotItem(z=zz, color=(0.5, 0.5, 1, 1))
wang.setGLOptions('translucent')
wang.setDepthValue(1)
wang.translate(-100, -100, 90)
# self.wang.setColor(QtGui.QColor('black'))
w.addItem(wang)

# def update():
#     global p4, z, index
#     index -= 1
#     p4.setData(z=z[index % z.shape[0]])
#
#
# timer = QtCore.QTimer()
# timer.timeout.connect(update)
# timer.start(30)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()