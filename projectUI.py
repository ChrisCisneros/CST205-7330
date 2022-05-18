#UI for project

from PySide6.QtWidgets import *
from PySide6.QtCore import Slot
from PIL import Image
import urllib.request
from pprint import pprint
from movie_api_data import movie_info
import sys
import requests
from io import BytesIO

movieDict = {}

class ProjectUI(QWidget):
    def __init__(self):
        super().__init__()

        self.searchBoxLineEdit = QLineEdit("Enter Keywords to Search Here")
        #self.searchBoxLineEdit.selectAll()
        self.searchBoxLineEdit.returnPressed.connect(self.onSearchButton)

        self.searchPushButton = QPushButton("Search")
        self.searchPushButton.clicked.connect(self.onSearchButton)

        genre_List = ['Fantasy','Action','Adventure','Comedy', 'Horror', 'Mystery', 'Historical', '-none-']
        self.genre = QComboBox()
        self.genre.addItems(genre_List)
        self.genre.currentIndexChanged.connect(self.onSearchButton)
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
        hbox2.addWidget(self.genre)
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
        movie_dict = {}    
        max_list = []
        max_val = 0

      # def preprocess(movie_info):
#     for i in movie_info:
#         movieDict[i["imdbID"]] = []


        def preprocess(movie_info):

           

            for i in movie_info:
                movie_dict[i["imdbID"]] = []

                for j in i['Title'].split():
                     movie_dict[i['imdbID']].append(j.rstrip(',').lower())
                
                for j in i['Actors'].split():
                    movie_dict[i['imdbID']].append(j.rstrip(',').lower())
                
                for j in i['Genre'].split():
                    movie_dict[i['imdbID']].append(j.rstrip(',').lower())
            
                movie_dict[i['imdbID']].insert(1,i['Year'])
                movie_dict[i['imdbID']].insert(0,0)
         

            return movie_dict

        

        
        preprocess(movie_info)
      

        selection  = self.genre.currentText()


        def get_count(dict,search):
            for key,value in dict.items():
                if selection in value:
                    value[0] += 1
                for count,term in enumerate(value):
                    if count >= 1:
                      
                        if term in search:
                            #                          
                            value[0] += 1
                             
                           
            return dict


        get_count(movie_dict,self.searchBoxLineEdit.text())

        for key,value in movie_dict.items():    
            for count,term in enumerate(value):
                if count == 0:
                    if term >= max_val:
                        if term > max_val and len(max_list) > 0:                 
                            del max_list[:len(max_list)]
                        max_val = term
                        if(max_val > 0):
                            max_list.append(key)
                            

        

        

        for i in movie_info:
            if(i['imdbID']) == max_list[0]:
                posterURL = i["Images"][0]
                urllib.request.urlretrieve(posterURL, "poster.jpg")
                img = Image.open("poster.jpg")
                img.show()
                
               
    
        

    

app = QApplication([])
myScreen = ProjectUI()
myScreen.show()
sys.exit(app.exec())
