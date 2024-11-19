from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SesameGen")

        _password_label = QLabel("Password")

        self.password_input = QLineEdit()

        _regenerate_button = QPushButton()
        _regenerate_button.setText("Generate")
        _regenerate_button.clicked.connect(self.update_password)

        _length_label = QLabel("Length")

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(1)
        self.slider.setMaximum(64)
        self.slider.setValue(16)
        self.slider.valueChanged.connect(self.update_password)

        self.number_of_characters_label = QLabel("16 Characters")

        layout = QVBoxLayout()
        layout.addWidget(_password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(_regenerate_button)
        layout.addWidget(_length_label)
        layout.addWidget(self.slider)
        layout.addWidget(self.number_of_characters_label)

        container = QWidget()

        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def update_password(self):
        self.number_of_characters_label.setText(f"{self.slider.value()} Characters")


def start_gui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


start_gui()
