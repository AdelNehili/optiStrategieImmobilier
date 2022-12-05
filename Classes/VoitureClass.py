from matplotlib.pylab import *
from Classes.BizarreClass import *


class Car(Livings):
    # AllExpenses = [180, 40]  # Food/For Fun

    def __init__(self, name, age, expenses, currentGoldToPay):
        super().__init__(name, age, expenses)

        self.currentGoldToPay = currentGoldToPay

        self.monthlyPayment = self.expenses[0]
        self.introduceYourself()

        self.months = 0
        self.currentPricePayed = 0
        self.x = []
        self.y = []

        self.sick_expense = 300
        self.no_sick_period = 2

        self.life_time = 10

    def introduceYourself(self):
        if self.monthlyPayment != 0:
            print("Vroum Vroum je suis :", self.name, "et je coute :", self.monthlyPayment, " par mois")
        print("")

    def getExpensesValue(self):
        # Plus logique que tout le monde garde "secret" ses dépenses => seul les Livings connaissent leur propres
        # dépenses
        currentExpenses = 0

        for elem in self.expenses:
            currentExpenses += elem
        self.currentGoldToPay -= self.monthlyPayment
        # print("Je suis", self.name, "et je dépense par mois", currentExpenses)
        # print("La partie de la voiture déja payée vaut :", self.currentPricePayed)

        return currentExpenses

    def livingOneMonth(self):
        super().livingOneMonth()
        if self.monthlyPayment != 0:
            if self.currentGoldToPay <= 0:
                print("__________________________________")
                print("CA Y EST, ON A PAYE CETTE VOITURE!!")
                print("__________________________________")
                self.monthlyPayment = 0
                self.expenses[0] = 0

