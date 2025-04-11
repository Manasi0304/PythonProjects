import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setPlaceholderText("0")
        self.result_display.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.result_display)

        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        for button_text in self.buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_clicked)
            button.setStyleSheet("background-color: #d3d3d3; border: none; padding: 10px;")
            self.layout.addWidget(button)

        self.setLayout(self.layout)

    def button_clicked(self):
        button = self.sender()
        button_text = button.text()

        if button_text == "=":
            expression = self.result_display.text()
            try:
                result = eval(expression)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        else:
            current_text = self.result_display.text()
            if current_text == "0" and button_text.isdigit():
                self.result_display.setText(button_text)
            else:
                self.result_display.setText(current_text + button_text)
            button.setStyleSheet("background-color: #a9a9a9; border: none; padding: 10px;")  # Change color


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
