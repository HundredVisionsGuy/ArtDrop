"""
check_boxes.py
by HundredVisionsGuy
An experiment with check boxes (QCheckBox)
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(400, 600)

        layout = QVBoxLayout()
        title_label = QLabel("Title Label (Make this bigger, please!)")

        # Description Label
        description = "This is an example of working with QCheckBoxes. "
        description += "The first example is just a series of check boxes "
        description += "that are not being grouped.\n\nWhat level course "
        description += "are you in?"
        description_label = QLabel(description)
        description_label.setWordWrap(True)

        # Create a series of check boxes
        self.programming_1_check = QCheckBox("Programming 1")
        self.programming_2_check = QCheckBox("Programming 2")
        self.programming_3_check = QCheckBox("Programming 3")

        # Set programming 3 checkbox to neutral (tri-state)
        self.programming_3_check.setCheckState(Qt.CheckState.PartiallyChecked)
        
        # Create another series of check boxes using a list and for loop
        self.programming_label = QLabel("Choose your Programming Language/s:")
        self.programming_language_vbox = QVBoxLayout()

        languages = ["Python", "Java", "JavaScript", "Rust", "Go", "VBScript"]
        self.languages_selected = []
        for language in languages:
            checkbox = QCheckBox(language)
            checkbox.stateChanged.connect(self.language_checkbox_state_changed)
            self.programming_language_vbox.addWidget(checkbox)

        # Process Form Button
        self.process_button = QPushButton("Display Output")
        self.process_button.clicked.connect(self.process_form)

        # Output Label
        self.output_instructions = "Make your selection, then click the "
        self.output_instructions += "'Display Output' button above."
        self.output_label = QLabel(self.output_instructions)
        self.output_label.setWordWrap(True)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addWidget(self.programming_1_check)
        layout.addWidget(self.programming_2_check)
        layout.addWidget(self.programming_3_check)
        layout.addWidget(self.programming_label)
        layout.addLayout(self.programming_language_vbox)
        layout.addWidget(self.process_button)
        layout.addWidget(self.output_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def process_form(self):
        """Get check box states to determine what we classes_selected"""

        # check classes
        classes_selected = []
        if self.programming_1_check.isChecked():
            classes_selected.append(self.programming_1_check.text())
        if self.programming_2_check.isChecked():
            classes_selected.append(self.programming_2_check.text())
        if self.programming_3_check.isChecked():
            classes_selected.append(self.programming_3_check.text())

        if classes_selected:
            results = "You classes_selected the following classes:"
            for item in classes_selected:
                results += "\n* " + item
        
        # Check programming languages
        for widget in self.programming_language_vbox.children():
            print(widget)

        self.output_label.setText(results)


    def language_checkbox_state_changed(self, state):
        checkbox = self.sender()
        if state == 2:
            item = checkbox.text()
            if item not in self.languages_selected:
                self.languages_selected.append(item)
        elif state == 0:
            item = checkbox.text()
            if item in self.languages_selected:
                self.languages_selected.remove(item)
        else:
            print("Let's take over the entire tri-state checkbox")
        print(self.languages_selected)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()