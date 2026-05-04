"""
main_window.py
by HundredVisionsGuy
The main ArtDrop layout window.
"""
from utils import controller
from PySide6.QtCore import QEvent, Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
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
        self.resize(320, 240)

        layout = QVBoxLayout()

        # Header Layout
        header_layout = QHBoxLayout()
        title_label = QLabel("Art Drop")
        surprise_button = QPushButton("surprise me")
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(surprise_button)
        header_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)

        # Search Layout
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Monet")
        self.search_button = QPushButton("Submit")
        self.search_button.clicked.connect(self.search_term)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_edit)
        search_layout.addWidget(self.search_button)

        # Output Label (Proof of concept for now)
        self.output_label = QLabel("Add a term and click search.")
        self.output_label.setWordWrap(True)


        # add widgets & layouts to main layout
        layout.addLayout(header_layout)
        layout.addLayout(search_layout)
        layout.addWidget(self.output_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def search_term(self):
        # Get text
        search_text = self.search_edit.text()

        # Make API call
        api_results = controller.artist_search(search_text)

        # Display results
        self.output_label.setText(api_results)

if __name__ == "__main__":
    print("To be determined...")