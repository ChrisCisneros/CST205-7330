#UI for project

from PySide6.QtWidgets import *
from PySide6.QtCore import Slot
from PIL import Image
import urllib.request
from pprint import pprint
from movie_api_data import movie_info
import sys

movieDict = {}

class ProjectUI(QWidget):
    def __init__(self):
        super().__init__()

        self.searchBoxLineEdit = QLineEdit("Enter Keywords to Search Here")
        self.searchBoxLineEdit.selectAll()
        self.searchBoxLineEdit.returnPressed.connect(self.onSearchButton)

        self.searchPushButton = QPushButton("Search")
        self.searchPushButton.clicked.connect(self.onSearchButton)

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
        hbox2.addWidget(self.searchBoxLineEdit)
        hbox2.addWidget(self.searchPushButton)

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

    @Slot()
    def onSearchButton(self):
        keywords = self.searchBoxLineEdit.text().lower()
        # print(keywords)

        preprocess(movie_info)
        # pprint(movieDict)

        getCount(movieDict, keywords)

        max_list = []
        max_val = 0
        for key, value in movieDict.items():
            for counter, term in enumerate(value):
                if counter == 0:
                    if term >= max_val:
                        if term > max_val and len(max_list) > 0:
                            del max_list[:len(max_list)]
                        max_val = term
                        if max_val > 0:
                            max_list.append((value[1], key))
        
        max_list.sort()
        # pprint(max_list)

        for i in max_list:
            # pprint("=" * 25 + i[1] + "\n" + "=" * 25)
            for k in movie_info:
                if i[1] == k["imdbID"]:
                    posterURL = k["Poster"]
                    posterURL = "https:" + posterURL.split(":", 1)[1]
                    pprint("Poster URL: " + posterURL)

                    urllib.request.urlretrieve(posterURL, "poster.jpg")
                    img = Image.open("poster.jpg")
                    img.show()



def preprocess(movie_info):
    for i in movie_info:
        movieDict[i["imdbID"]] = []

        for k in i["Title"].split():
            movieDict[i["imdbID"]].append(k.rstrip(",").lower())

        for k in i["Actors"].split():
            movieDict[i["imdbID"]].append(k.rstrip(",").lower())
        
        movieDict[i['imdbID']].insert(0, 0)
        movieDict[i["imdbID"]].insert(1, i["Title"][0].lower())
    
    return movieDict

def getCount(currDict, keywords):
    for key, value in currDict.items():
        for counter, term in enumerate(value):
            if counter > 1:
                if term in keywords:
                    value[0] += 1
    
    return currDict

app = QApplication([])
myScreen = ProjectUI()
myScreen.show()
sys.exit(app.exec())
