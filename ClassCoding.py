class Animal:
    def __init__(self, genus, species):
        self._species = species
        self._genus = genus

    def move(self):
        print('f.{self.__species} is moving')

    def think(self):
        print('f.{self.__species} is thinking')
    
    def vocalize(self):
        print('f.{self.__species} is vocalizing')

class Book:
    def __init__(self, title, author):
        self._author = author
        self._title = title


class Vehicle:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
    
    def start(self):
        print('targvashooooom')

    def move(self):
        print('Vrooom')

    def turn(self):
        print('errrrrrt')
