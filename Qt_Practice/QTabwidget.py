import sys
from PySide6 import QtGui,QtCore


app = QtGui.QApplication([])
tabwidget = QtGui.QTabWidget()
widget = QtGui.Qtwidget()
layout=QtGui.QGridLayout(widget)
tabwidget.addTab(widget, "Tab 1")
tabwidget.show()
app.excec_()
