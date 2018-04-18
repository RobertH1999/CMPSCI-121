import sys 
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication 
class App(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.title = 'Layout' 
        self.left = 20 
        self.top = 40 
        self.width = 440 
        self.height = 380 
        self.initUI()    
    def initUI(self):  
        grid = QGridLayout() 
        self.setLayout(grid) 
        names = ['Clear', 'Back', '', 'Close', 
                 '7', '8', '9', '/', 
                '4', '5', '6', '*', 
                 '1', '2', '3', '-', 
                '0', '.', '=', '+'] 
        positions = [(i,j) for i in range(5) for j in range(4)] 
        for position, name in zip(positions, names):   
            if name == '': 
                continue 
            button = QPushButton(name) 
            grid.addWidget(button, *position)  
        self.setWindowTitle(self.title) 
set
s
the main layout of the window
The instance of a 
QGridLayout
 is created and set to be the layout for the 
application window
labels that will be used later for buttons 
creates a list of positions in 
the grid 
buttons are created and added to the layout with 
the addWidget() method. Remember, since each 
position is a tuple, you must write an asterisk 
before the identifier. 
11 
        self.setGeometry(self.left, self.top, self.width, self.height)  
        self.show() 
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_()) 
    
