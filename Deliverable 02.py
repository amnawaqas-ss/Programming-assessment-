import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget

# Setting up Window 
class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("WhackAMoleGame")
        self.setFixedSize(500, 500)
        
        # Central widget setupn
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #1a0933;")  # Dark purple background
        self.setCentralWidget(central_widget)
        
        # Lay out setup 
        grid_layout = QGridLayout()
        self.buttons = []
        
        for row in range(4):
            row_buttons = []
            for col in range(4):
                # Row and Column Setup
                button = QPushButton(f"({row}, {col})")
                button.setFixedSize(80, 80)
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
                button.clicked.connect(lambda clicked, r=row, c=col: self.button_clicked(r, c))
            self.buttons.append(row_buttons)
            
        central_widget.setLayout(grid_layout)
        
    def button_clicked(self, row, col):
        print(f"button {row}, {col}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyFirstWindow()
    window.show()
    sys.exit(app.exec())