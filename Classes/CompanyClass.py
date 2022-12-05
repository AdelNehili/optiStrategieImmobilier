from matplotlib.pylab import *

class Company:
    # AllExpenses = [180, 40]  # Nourriture/Loisirs

    def __init__(self, name, age, investments, interestRate):
        self.name = name
        self.age = age
        self.save = investments
        self.investments = investments # Pas sûr que ce soit une bonne chose que company ait la liste d'investments
        self.interestRate = interestRate


        self.months = 0
        self.x = []
        self.y = []

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def livingMonths(self, nbrMonths, isDisplayed):
        for i in range(nbrMonths):
            self.livingOneMonth()
            self.x.append(self.months)
            self.y.append(self.investments)
            print("Voila combien a été généré :", self.investments)
        if isDisplayed:
            self.displayGraph()


    def calculateInterest(self):
        newInterest = self.investments*self.interestRate
        self.investments += newInterest

    def livingOneMonth(self):
        self.age += 1/12
        self.months += 1

        self.calculateInterest()





    def displayGraph(self):
        matplotlib.pylab.plot(self.x, self.y, 'r-')

        grid()  # permet d'afficher des grilles pour mieux lire
        matplotlib.pylab.show()
    def getX(self):
        return self.x

    def getY(self):
        return self.y

