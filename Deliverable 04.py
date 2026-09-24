import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QLabel)
from PyQt6.QtCore import QTimer

# Setting up window 
class MyFirstWindow(QMainWindow):
    """
    Window for my game.
    """
    def __init__(self):
        super().__init__()

        # Game timer
        self.game_duration = 40
        self.time_left = 40

        # Window setup for game
        self.setWindowTitle("WhackAMoleGame")
        self.setFixedSize(400, 400)
        
        # Score Variable and mole location
        self.score = 0
        self.game_active = True
        self.current_mole_pos = None

        # Main layout-Header and gridd
        main_layout = QVBoxLayout()

        # Header layout for Score and Time
        header_layout = QHBoxLayout()
        self.score_label = QLabel("Score: 0")
        self.time_label = QLabel(f"Time: {self.time_left}s")

        header_layout.addWidget(self.score_label)
        header_layout.addWidget(self.time_label)
        main_layout.addLayout(header_layout)

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

        main_layout.addLayout(grid_layout)

        # Set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(main_layout)

        # After game has ended
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_timer)
        self.countdown_timer.start(1000)

        # The first mole
        self.spawn_mole()

    def update_timer(self):
        """
        Updates time left every second and finishies game at 0.
        """
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.setText(f"Time: {self.time_left}s")
        else:
            self.countdown_timer.stop()
            self.end_game()

    def spawn_mole(self):
        """
        Disappear previous mole and puts 'mole' on a new random Place.
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
        if not self.game_active:
            return

        if self.current_mole_pos == (row, col):
            self.score += 1
            self.score_label.setText(f"Score: {self.score}")
            print(f"Hit! Score: {self.score}")
            self.spawn_mole()
        else:
            print(f"Missed! Button {row}, col {col}")

    def save_score_to_file(self):
        """
        final game score to score.txt file.
        """
        try:
            with open("score.txt", "a") as file:
                file.write(f"Final Score: {self.score}\n")
            print("Score saved to score.txt")
        except Exception as e:
            print(f"Error saving score: {e}")

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
        
        # To save score (how many times user made hit)
        self.save_score_to_file()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyFirstWindow()
    window.show()
    sys.exit(app.exec())