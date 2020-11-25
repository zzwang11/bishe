# -*- coding: utf-8 -*-
"""
Demonstrate use of GLLinePlotItem to draw cross-sections of a surface.

"""
## Add path to library (just for examples; you do not need this)
# import initExample

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 100
w.show()
w.setWindowTitle('pyqtgraph example: GLLinePlotItem')

gx = gl.GLGridItem()
gx.setSize(1,1,1,QtGui.QVector3D(50,20,1))# 设置网格的大小
gx.setSpacing(2,2,2,QtGui.QVector3D(2,2,100))# 设置网格密度

gx.rotate(90, 0, 1, 0)#旋转
# gx.translate(-10, 0, 0)#整个平移
w.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
# gy.translate(0, -10, 0)
w.addItem(gy)
gz = gl.GLGridItem()
# gz.translate(0, 0, -10)
w.addItem(gz)



# n = 51
# y = np.linspace(-15,0,n)
# x = np.linspace(-15,15,100)
# for i in range(n):
#     yi = np.array([y[i]]*100)
#     d = (x**2 + yi**2)**0.5
#     z = 10 * np.cos(d) / (d+1)
#     pts = np.vstack([x,yi,z]).transpose()
#     # plt = gl.GLLinePlotItem(pos=pts, color=pg.glColor((i,n*1.3)), width=(i+1)/10., antialias=True)
#     plt = gl.GLLinePlotItem(pos=pts, color=pg.glColor((i, n * 1.3)), width=(i + 1) / 10., antialias=True)
#     w.addItem(plt)

cols = 90
rows = 100
x = np.linspace(-8, 8, cols + 1).reshape(cols + 1, 1)
y = np.linspace(-8, 8, rows + 1).reshape(1, rows + 1)
d = (x ** 2 + y ** 2) * 0.1
d2 = d ** 0.5 + 0.1
phi = np.arange(0, np.pi * 2, np.pi / 20.)
z = np.sin(d[np.newaxis, ...] + phi.reshape(phi.shape[0], 1, 1)) / d2[np.newaxis, ...]
plt = gl.GLSurfacePlotItem(x=x[:, 0], y=y[0, :], shader='heightColor', computeNormals=False, smooth=False)
plt.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
w.addItem(plt)
index = 0


def update():
    global plt, z, index
    index -= 1
    plt.setData(z=z[index % z.shape[0]])

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
