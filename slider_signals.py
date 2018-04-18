import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QWidget):
  def __init__(self):
    super().__init__()
    self.title = 'Text and Slider'
    self.initUI()
  def initUI(self):
    global mySlider, myTextmySlider = QSlider(Qt.Horizontal, self)
    mySlider.setRange(0, 100)
    myText = QLineEdit()
    vbox = QVBoxLayout()
    vbox.addWidget(mySlider)
    vbox.addWidget(myText)
    self.setLayout(vbox)
    mySlider.valueChanged.connect(self.updateText)
    myText.textChanged.connect(self.updateSlider)
    self.setWindowTitle(self.title)
    self.show()
  def updateText(self, value):
    myText.setText(str(value))
  def updateSlider(self, text):
    try:
      mySlider.setValue(int(text))
    except ValueError:
      passif __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())
