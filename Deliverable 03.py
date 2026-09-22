import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget)
from PyQt6.QtCore import QTimer

#Setting up window 
class MyFirstWindow(QMainWindow):
    """
    Window for my game.
    """
    def __init__(self):
        super().__init__()

        # Game timer 
        self.game_duration = 40

        # Window setup for game
        self.setWindowTitle("WhackAMoleGame")
        self.setFixedSize(400, 400)

        # Score Variable and mole location 
        self.score = 0
        self.current_mole_pos = None

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

        # After time has ended
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.end_game)
        self.timer.start(self.game_duration * 1000)

        # The first mole
        self.spawn_mole()

    def spawn_mole(self):
        """
        Disappear previous mole and add mole on a new random place.
        """
        if self.current_mole_pos:
            prev_row, prev_col = self.current_mole_pos
            self.buttons[prev_row][prev_col].setText("")

        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.current_mole_pos = (row, col)
        self.buttons[row][col].setText("mole")

    def button_clicked(self, row, col):
        """
        For button click events to make sure grid coordinates and check mole hit.
        """
        if self.current_mole_pos == (row, col):
            self.score += 1
            print(f"Hit! : {self.score}")
            self.spawn_mole()
        else:
            print(f"Missed! Button {row}, col {col}")
    def end_game(self):
        """
         When 40 seconds obver.
        """
        self.game_active = False  
        
        # Disable buttons and mole text.
        if self.current_mole_pos:
            r, c = self.current_mole_pos
            self.buttons[r][c].setText("")

        for row_buttons in self.buttons:
            for btn in row_buttons:
                btn.setEnabled(False)
                
        print(f"Game Over! Final Score: {self.score}")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyFirstWindow()
    window.show()
    sys.exit(app.exec())