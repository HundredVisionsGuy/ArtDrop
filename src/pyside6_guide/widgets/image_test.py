"""
basic_app.py
by HundredVisionsGuy
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys

# from Pyside6 import QtGuiQPixMap
from PySide6.QtGui import QPixmap

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic App: a simple greeting app.")

        # TODO: add a label for an image
        self.image_label = QLabel()
        self.image_pixmap = QPixmap("resources/images/puppy.jpg")
        self.image_label.setPixmap(self.image_pixmap)

        # TODO: add a file dialog to open a file (image) and load an image
        file_browse_layout = QHBoxLayout()
        file_label = QLabel("File:")
        self.file_browse = QPushButton("Choose Image")
        self.file_browse.clicked.connect(self.open_file_dialog)
        file_browse_layout.addWidget(file_label)
        file_browse_layout.addWidget(self.file_browse)

        # TODO: add a push button to 

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.image_label)
        layout.addLayout(file_browse_layout)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select an Image File",
            "",
            "Images (*.png *.jpg *.gif)"
        )
        if filename:
            path = Path(filename)
            self.image_pixmap = QPixmap(path)
            self.image_label.setPixmap(self.image_pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()