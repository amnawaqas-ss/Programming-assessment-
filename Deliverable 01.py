import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
#Setting up Window 
class MyFirstWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        
        self.setWindowTitle("WhackAMoleGame")
        set.size(500, 800)
        
        grid_layout = QGridLayout()
        self.buttons = []
        for row in range(4):
            row_buttons = []
            for col in range(4):
                button = QPushButton("")
                button.setFixedSize(70, 70)
                
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
                button.clicked.connect(lambda clicked, r=row, c=col: self.button_clicked(r, c))
            self.buttons.append(row_buttons)
            
        central_widget = QWidget()
        self.selfcentralWidget(central_widget)
        central_widget.setLayout(grid_layout)
        
    def button_clicked(self, row, col):
        print(f"button {row}, {col}")
        
app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())