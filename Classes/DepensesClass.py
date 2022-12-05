#import matplotlib.pylab as nc
from matplotlib.pylab import *

listeNom = ["Mensualité", "Nourriture", "Vélo", "gaz", "electricité", "ass. habitation", "eau", "internet", "chaudière", "restorant", "Velo"]
listePrix = [1300, 400, 30, 10, 50, 25, 60, 50, 7, 120, 30]


class Depense():

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def printEverything(self):
        print("Je suis dans la class et mon nom est :", self.name)
        print("Je suis dans la class et mon cout est :", self.value)
        print("")

    def printSpeedAndMarq(self):
        x = matplotlib.pylab.linspace(-3,3,100)
        y = x**2
        z = 1-x**2

        matplotlib.pylab.plot(x,y,'r-')
        matplotlib.pylab.plot(x,z,'y.')

        grid() #permet d'afficher des grilles pour mieux lire
        matplotlib.pylab.show()


    def createAllDepenses(self):
        listeAllDepenses = []
        for i in range(len(listeNom)):
            currentName = listeNom[i]
            currentValue = listePrix[i]

            currentDepense = Depense(currentName,currentValue)
            listeAllDepenses.append(currentDepense)
        return listeAllDepenses

    def printAllDepenses(self):
        listeAllDepenses = self.createAllDepenses()
        for elem in listeAllDepenses:
            elem.printEverything()
