from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)

from sesamegen import get_password


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

        self.number_of_characters_label = QLabel()
        self.number_of_characters_label.setMinimumWidth(100)
        self.number_of_characters_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.entropy_label = QLabel()
        self.entropy_label.setMinimumWidth(70)
        self.entropy_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.lower_case = QCheckBox("Lower case")
        self.lower_case.setChecked(True)
        self.lower_case.stateChanged.connect(self.update_password)

        self.upper_case = QCheckBox("Upper case")
        self.upper_case.setChecked(True)
        self.upper_case.stateChanged.connect(self.update_password)

        self.numbers = QCheckBox("Numbers")
        self.numbers.setChecked(True)
        self.numbers.stateChanged.connect(self.update_password)

        self.special_characters = QCheckBox("Special characters")
        self.special_characters.stateChanged.connect(self.update_password)

        self.remove_ambiguous_characters = QCheckBox("Remove Ambiguous Characters")
        self.remove_ambiguous_characters.setChecked(True)
        self.remove_ambiguous_characters.stateChanged.connect(self.update_password)

        layout = QVBoxLayout()

        password_row = QHBoxLayout()
        password_row.addWidget(_password_label)
        password_row.addWidget(self.password_input)
        password_row.addWidget(_regenerate_button)

        slider_row = QHBoxLayout()
        slider_row.addWidget(_length_label)
        slider_row.addWidget(self.slider)
        slider_row.addWidget(self.number_of_characters_label)
        slider_row.addWidget(self.entropy_label)

        checkbox_row = QHBoxLayout()
        checkbox_row.addWidget(self.lower_case)
        checkbox_row.addWidget(self.upper_case)
        checkbox_row.addWidget(self.numbers)
        checkbox_row.addWidget(self.special_characters)
        checkbox_row.addWidget(self.remove_ambiguous_characters)

        layout.addLayout(password_row)
        layout.addLayout(slider_row)
        layout.addLayout(checkbox_row)

        self.update_password()

        container = QWidget()
        container.setLayout(layout)
        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def update_password(self):
        self.number_of_characters_label.setText(f"{self.slider.value()} Characters")
        new_password = get_password(
            length=self.slider.value(),
            lower_case=self.lower_case.checkState().value,
            upper_case=self.upper_case.checkState().value,
            numbers=self.numbers.checkState().value,
            special_characters=self.special_characters.checkState().value,
            remove_ambiguous_characters=self.remove_ambiguous_characters.checkState().value,
        )
        self.password_input.setText(new_password["password"])
        self.entropy_label.setText(f"{new_password['entropy']} bits")


def start_gui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


start_gui()
