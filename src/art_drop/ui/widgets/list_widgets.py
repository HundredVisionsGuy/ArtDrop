"""
list_widgets.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QListWidget,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(380, 340)
        self.setStyleSheet(
            """background: #336699;
            color: #ffffff;"""
        )
        self.set_fonts()

        layout = QVBoxLayout()
        title_label = QLabel("ListView Widget")
        title_label.setFont(QFont("Syne Mono", 28))

        # TODO: create your list widget
        self.music_selection = QListWidget()
        self.music_selection.setFont(QFont("Titillium Web", 12, 400))

        # TODO: add items to your list widget
        self.music_selection.addItems(["Classical", "Rock", "Rap", "R&B", "Jazz"])
        self.music_selection.addItem("Ska")

        # Add signals to list widget
        self.music_selection.currentItemChanged.connect(self.index_changed)
        self.music_selection.currentTextChanged.connect(self.text_changed)

        # TODO: add a button to test getting input from the list widget
        select_button = QPushButton("Choose")
        select_button.setCheckable(False)
        select_button.clicked.connect(self.choose_genre)
        select_button.setFont(QFont("Titillium Web", 14, 400))

        """
        Advanced TODO
        1. check out the docs at https://doc.qt.io/qt-6/qlistwidget.html
        2. explore the public methods
        3. check out the slots and signals
        4. customize your QListWidget
        5. style your QListWidget
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.music_selection)
        layout.addWidget(select_button)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setStyleSheet(
            """background: #336699;
            color: #ffffff;"""
        )
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    # Process Selection
    def choose_genre(self):
        """gets selection and displays information"""
        genre = self.music_selection.currentItem().text()
        print("Do something with the selection")


    # List Widget Signals - in case you want to perform an action when the
    # user interacts with the list widget.
    def index_changed(self, index):  # Not an index, index is a QListWidgetItem
        print(index.text())

    def text_changed(self, text):  # text is a str
        test = self.music_selection.currentItem().text()
        print(text)

    def set_fonts(self):
        """Set the font using QFontDatabase"""
        # import fonts
        font_dir = "resources/fonts/"
        heading_font_name = "SyneMono-Regular.ttf"
        heading_font_path = font_dir + heading_font_name

        normal_font_name = "TitilliumWeb-Regular.ttf"
        normal_font_path = font_dir + normal_font_name

        # Try and add fonts
        success = QFontDatabase.addApplicationFont(heading_font_path)
        if success == -1:
            print(f"{heading_font_name} not loaded")
        success = QFontDatabase.addApplicationFont(normal_font_path)
        if success == -1:
            print(f"{normal_font_path} not loaded")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
