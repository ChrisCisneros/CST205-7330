#UI for project

from PySide6.QtWidgets import(QPushButton, QStackedLayout, QHBoxLayout, QCheckBox, QWidget, QComboBox, QLineEdit, QGroupBox, QApplication, QLabel, QVBoxLayout, QPushButton)
from PySide6.QtCore import Slot
import sys

class ProjectUI(QWidget):
    def __init__(self):
        super().__init__()

        genre_List = ['Comedy', 'Horror', 'Mystery', 'Historical', '-none-']
        genre = QComboBox()
        genre.addItems(genre_List)
        genreLabel = QLabel("Please choose a genre:")

        playingLabel = QLabel("Is Playing")
        playingBox = QCheckBox()

        popularLabel = QLabel("Most Popular")
        popularBox = QCheckBox()

        ratingsLabel = QLabel("Ratings")
        ratingsBox = QCheckBox()
        
        hbox1 = QHBoxLayout()
        hbox2 = QVBoxLayout()

        hbox1.addWidget(playingLabel)
        hbox1.addWidget(playingBox)
        hbox1.addWidget(popularLabel)
        hbox1.addWidget(popularBox)
        hbox1.addWidget(ratingsLabel)
        hbox1.addWidget(ratingsBox)

        hbox2.addWidget(genreLabel)
        hbox2.addWidget(genre)

        gbox1 = QGroupBox()
        gbox1.setLayout(hbox1)

        gbox2 = QGroupBox()
        gbox2.setLayout(hbox2)

        screen = QVBoxLayout()
        screen.addWidget(gbox1)
        screen.addWidget(gbox2)

        self.setLayout(screen)
        self.setWindowTitle('Movie Search Tool')
        self.setGeometry(100, 100, 500, 500)

app = QApplication([])
myScreen = ProjectUI()
myScreen.show()
app.exec_()