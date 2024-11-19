from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget, QCheckBox,
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

        self.entropy_label = QLabel("x bits")

        self.lower_case = QCheckBox("Lower case")
        # self.lower_case.setCheckState()
        self.lower_case.stateChanged.connect(self.update_password)

        self.upper_case = QCheckBox("Upper case")
        # self.upper_case.setCheckState()
        self.upper_case.stateChanged.connect(self.update_password)

        self.numbers = QCheckBox("Numbers")
        # self.numbers.setCheckState(True)
        self.numbers.stateChanged.connect(self.update_password)

        self.special_characters = QCheckBox("Special characters")
        self.special_characters.stateChanged.connect(self.update_password)

        self.remove_ambiguous_characters = QCheckBox("Remove Ambiguous Characters")
        # self.remove_ambiguous_characters.setCheckState(True)
        self.remove_ambiguous_characters.stateChanged.connect(self.update_password)

        layout = QVBoxLayout()
        layout.addWidget(_password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(_regenerate_button)
        layout.addWidget(_length_label)
        layout.addWidget(self.slider)
        layout.addWidget(self.number_of_characters_label)
        layout.addWidget(self.entropy_label)
        layout.addWidget(self.lower_case)
        layout.addWidget(self.upper_case)
        layout.addWidget(self.numbers)
        layout.addWidget(self.special_characters)
        layout.addWidget(self.remove_ambiguous_characters)

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
