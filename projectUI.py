#UI for project

from PySide6.QtWidgets import(QPushButton, QWidget, QComboBox, QLineEdit, QGroupBox, QApplication, QLabel, QVBoxLayout, QPushButton)
from PySide6.QtCore import Slot

class ProjectUI(QWidget):
    def __init__(self):
        super().__init__()

        genre_List = ['Comedy', 'Horror', 'Mystery', 'Historical', '-none-']
        genre = QComboBox()
        genre.addItems(genre_List)
        genreLabel = QLabel("Please choose a genre")

        screen = QVBoxLayout()

        screen.addWidget(genreLabel)
        screen.addWidget(genre)

        self.setLayout(screen)
        self.setWindowTitle('Movie Search Tool')

app = QApplication([])
myScreen = ProjectUI()
myScreen.show()
app.exec_()