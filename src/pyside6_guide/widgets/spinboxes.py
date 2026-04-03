"""
spinboxes.py
by HundredVisionsGuy
A demo of the two main types of spinboxes
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(500, 700)

        layout = QVBoxLayout()
        title_label = QLabel("Title of this App")

        self.instructions = "Make an app that gets two different numbers: "
        self.instructions += "a whole number (integer) and a number with "
        self.instructions += "a decimal point (float). Put them each in "
        self.instructions += "a horizontal layout, and add two buttons: "
        self.instructions += "one that gets then displays the inputs, and "
        self.instructions += "one that resets the inputs and displays these "
        self.instructions += "instructions\n\n"
        self.instructions += "Feel free to modify these instructions once "
        self.instructions += "you are done. Make sure the isntructions are "
        self.instructions += "clear to the user as to what they should do."

        self.instructions_label = QLabel(self.instructions)
        self.instructions_label.setWordWrap(True)

        # TODO: Create An HBox Layout with a QSpinBox that gets a whole number
        age_input_hbox = QHBoxLayout()
        age_label = QLabel("Age: ")
        self.age_spinbox = QSpinBox()
        self.age_spinbox.valueChanged.connect(self.value_changed)
        self.age_spinbox.textChanged.connect(self.value_changed_str)
        age_input_hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # set minimum and maximum possible numbers
        self.age_spinbox.setMinimum(1)
        self.age_spinbox.setMaximum(120)
        self.age_spinbox.setSuffix(" yrs. old")

        # double spinbox
        self.double_spinbox = QDoubleSpinBox()
        self.double_spinbox.setPrefix("$")
        self.double_spinbox.setSingleStep(0.25)
        self.double_spinbox.valueChanged.connect(self.value_changed)
        self.double_spinbox.textChanged.connect(self.value_changed_str)
        double_label = QLabel("Get Number:")
        
        # Add label and button to layout
        age_input_hbox.addWidget(age_label)
        age_input_hbox.addWidget(self.age_spinbox)
        age_input_hbox.addWidget(double_label)
        age_input_hbox.addWidget(self.double_spinbox)

        # TODO: Create another HBox that gets a number with a decimal point

        # TODO: Add 2 buttons in an hbox: one for calculating & a clear button

        # TODO: Create an output label to display the instructions and results

        # TODO: Re-write the instructions to tell the user what to do.

        """
        Challenge: make a simple calculator app that uses 2 inputs.
            * Pick a math or science formula (like area of circle or force).
            * Change the instructions to explain what the user should do.
            * Format the results by rounding the output to 2 decimal places.
            * Format the output using clear language.
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addLayout(age_input_hbox)
        layout.addWidget(self.instructions_label)
        
        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet("font-size: 20pt;")

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def value_changed(self, value):
        print(f"Value Changed: doublespinbox: {value} - spinbox: {self.age_spinbox.value()}")

    def value_changed_str(self, str_value):
        print(f"Value Changed (as string): {str_value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
