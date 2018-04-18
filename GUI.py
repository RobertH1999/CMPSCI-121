import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMenu
from PyQt5.QtGui import QIcon
from PyQT5.QtCore import pyqtSlot

clas App(QMainWindow):
  def __init__(self):
    super().__init__():
      self.title = 'Window with Menu'
      self.left = 20
      self.top = 40
      self.width = 640
      self.height = 480
      self.initUI()
      
   def initUI(self):
    self.setWindowTiel(self.title)
    
