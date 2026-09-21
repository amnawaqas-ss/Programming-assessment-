import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
#Setting up window 
class MyFirstWindow(QMainWindow):
    """
     Window for my game.
        """
    def __init__(self):
        super().__init__()

        # Window setup for game
        self.setWindowTitle("WhackAMoleGame")
        self.setFixedSize(400, 400)

        # Making 4x4 grid layout
        grid_layout = QGridLayout()
        self.buttons = []

        for row in range(4):
            row_buttons = []
            for col in range(4):
                button = QPushButton("")
                button.setFixedSize(80, 80)
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
                
                # To print row and column
                button.clicked.connect(lambda checked, r=row, c=col: self.button_clicked(r, c))
                
            self.buttons.append(row_buttons)

        # Set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(grid_layout)

    def button_clicked(self, row, col):
        """
        For button click events to make sure grid coordinates.
        """
        print(f"Button {row}, col {col}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyFirstWindow()
    window.show()
    sys.exit(app.exec())
