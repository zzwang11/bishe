import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import matplotlib.pyplot as plt
from PyQt5 import QtGui

def pic_2d(self,a):
    # 二维图
    self.pyqtgraph1.clear()
    self.c = self.pyqtgraph1.addPlot(title=a, pen=pg.mkPen(color='b', width=2))
    self.c.setLabel('left', "Y Axis", units='A')
    self.c.setLabel('bottom', "Y Axis", units='s')
    self.c.setLogMode(x=True, y=False)

def draw_2d(self,a):
    self.c.plot(x=a[0], y=a[1])



def pic_3d(self,a):

    # n = 51
    # y = np.linspace(-10, 10, n)
    # x = np.linspace(-10, 10, 100)
    # zz = pg.gaussianFilter(np.zeros([20, 20]), (1, 1))
    #
    print(a)
    # 三维图
    # self.graph = gl.GLViewWidget(self.centralwidget)
    # self.graph.setObjectName("graph")
    # self.graph.setBackgroundColor(QtGui.QColor('white'))
    # self.graph.opts['distance'] = 40
    # self.gx = gl.GLGridItem()
    # self.gx.rotate(90, 0, 1, 0)
    # self.gx.translate(-10, 0, 0)
    # self.gx.setColor(QtGui.QColor('black'))
    # self.graph.addItem(self.gx)
    # self.gy = gl.GLGridItem()
    # self.gy.rotate(90, 1, 0, 0)
    # self.gy.translate(0, -10, 0)
    # self.gy.setColor(QtGui.QColor('black'))
    # self.graph.addItem(self.gy)
    # self.gz = gl.GLGridItem()
    # self.gz.translate(0, 0, -10)
    # self.gz.setColor(QtGui.QColor('black'))
    # self.graph.addItem(self.gz)
    # self.gridLayout_2.addWidget(self.graph, 0, 0, 1, 1)

    # 画线
    # for i in range(n):
    #     yi = np.array([y[i]] * 100)
    #     d = (x ** 2 + yi ** 2) ** 0.5
    #     z = 10 * np.cos(d) / (d + 1)
    #     pts = np.vstack([x, yi, z]).transpose()
    #     cmap = plt.get_cmap('jet')
    #
    #     minZ = -4
    #     maxZ = 10
    #     rgba_img = cmap((z - minZ) / (maxZ - minZ))
    #     # plt = gl.GLLinePlotItem(pos=pts, color=pg.glColor((i, n * 1.3)), width=(i + 1) / 10., antialias=True)
    #     plt1 = gl.GLLinePlotItem(pos=pts, color=rgba_img, width=5., antialias=True)
    #     self.graph.addItem(plt1)
    # 画平面
    # z = np.random.rand(len(x), len(y)) * 10
    # cmap = plt.get_cmap('jet')
    # color = cmap((z - np.min(z)) / np.max(z) - np.min(z))
    # plz = gl.GLSurfacePlotItem(x=x, y=y, z=z, colors=color)
    # self.graph.addItem(plz)

    # # 应该的标尺
    #
    # self.wang = gl.GLSurfacePlotItem(z=zz, color=(0.5, 0.5, 1, 1))
    # self.wang.setGLOptions('translucent')
    #
    # self.wang.setDepthValue(1)
    # self.wang.translate(-10, -10, 8)
    # self.graph.addItem(self.wang)
