from matplotlib.pylab import *
from Classes.VoitureClass import *

class TimeManager:

    def __init__(self, name, expenses, currentGoldToPay, family, economies, color):
        self.name = name

        self.expenses = expenses
        self.currentGoldToPay = currentGoldToPay

        self.total_expens = 0
        self.family = family
        self.setAllFamilyHouse()
        self.economies = economies
        self.color = color

        self.x = []
        self.y = []
        self.months = 0

        self.holidaysExpense = 3000

    def setAllFamilyHouse(self):
        #Cette fonction sert au premiers Human qui arrivent dans la maison
        #Une fois la maison crée, ajouter un membre revient à appeler addFamilyMember
        for elem in self.family:
            if isinstance(elem,Livings):
                elem.setHouse(self)
    def addFamilyMember(self, living):
        if isinstance(living,Livings):
            self.family.append(living)
            living.setHouse(self)

        else:
            self.showError(1)

    def deleteFamilyMember(self,current_member):
        if isinstance(current_member,Livings):
            self.family.remove(current_member)

    def introduceWholeHuman(self):
        print("Salut, moi c'est :", self.name, "et il me reste :", self.economies, "et j'ai :", self.months/12)
        for human in self.family:
            if isinstance(human, Human):
                print("Salut, moi c'est :", human.getName(), "et il me reste :", human.getEconomies(), "et j'ai :", human.getAge(), "ans!")
        print(" ")

    def introduceWholeFamily(self):
        print("Salut, moi c'est :", self.name, "et j'ai :", self.months / 12, "ans!")
        for livings in self.family:
            print("Salut, moi c'est :", livings.getName(), "et j'ai :", livings.getAge(), "ans!")
    def showError(self, value):
        print("BRUH ERREUR DE TYPE:", value)
        if value == 1:
            print("Attention, tu fais entrer dans la famille un truc non-livings!")
            quit()

    def getName(self):
        return self.name
    def getExpenses(self):
        return self.expenses

    def getFamily(self):
        return self.family

    def getEconomies(self):
        return self.economies

    def getMonths(self):
        return self.months

    def setHolidaysExpense(self, value):
        self.holidaysExpense = value

    def _goToHolidays(self, expense):
        if self.months % 12 == 0:
            self.economies -= expense

    def displayGraph(self):
        matplotlib.pylab.plot(self.x, self.y, 'r.')

        grid()  # permet d'afficher des grilles pour mieux lire
        matplotlib.pylab.show()

    def displayAllGraph(self):

        matplotlib.pylab.plot(self.x, self.y, self.color)

        for human in self.family:
            if isinstance(human,Human):
                # print("Je suis l'human de displayAllGraph", human.getName())
                matplotlib.pylab.plot(self.x, human.getY(), human.getColor())

        grid()
        matplotlib.pylab.show()

class Maison(TimeManager):
    # Expenses = [1400, 125]  # Rent/Charges
    AllFurniture = [200, 600, 500]  # Carpet/Full Bed/Wardrobe

    # AllFurniture = [0]  # Carpet/Full Bed/Wardrobe

    def __init__(self, name, expenses, currentGoldToPay, family, economies, color):
        super(Maison, self).__init__(name, expenses, currentGoldToPay, family, economies, color)
        self.liveFirstMonth()

    def receiveSalary(self, salary):
        print("L'entrée du mois vaut pour la maison:", salary)
        self.economies += salary

    def payExpenses(self, expenses, salaryPart):
        print("Il a fallut payé:", expenses)
        if expenses > salaryPart:
            print("Juste pour dire, ON EST A PEEEEEEEERTE!!!")
            print("On dépense :", expenses - salaryPart, "en TROP!")
        else:
            print("Ce qu'il reste du mois c'est :", salaryPart - expenses)
        self.economies -= expenses

    def liveFirstMonth(self):
        # Attention, cette fonction n'est appelée QUE par le constructeur! Elle sert de setup pour le 1er mois
        self.months += 1
        print("Le NBR DE MOIS :", self.months)

        for human in self.family:
            if isinstance(human, Human):
                humanEconomies = human.getEconomies()
                self.economies += humanEconomies
                human.setEconomies(0)
        for furniture in self.AllFurniture:
            self.economies -= furniture
        print("On a vécu le premier mois!!")
        print("Les economies de la maisons valent :", self.economies)
        print("")

    def _checkInflation(self):
        if self.months != 0 and self.months%12 == 0:
            inflation_value = 2/100
            self.economies = self.economies*(1-inflation_value)
            for human in self.family:
                if isinstance(human,Human):
                    new_salary = human.getSalary()*(1-inflation_value)
                    human.setSalary(new_salary)
                    new_economy = human.getEconomies()*(1-inflation_value)
                    human.setEconomies(new_economy)
            print("OUCH ON EST AU MOIS: ",self.months," ET L'INFLATION FAIT MAL!")

    def _checkHousePayment(self):
        monthlyPayment = self.expenses[0]
        self.currentGoldToPay -= monthlyPayment
        if self.currentGoldToPay <= 0 and monthlyPayment != 0:
            print("__________________________________")
            print("CA Y EST, ON A PAYE CETTE MAISON!!")
            print("__________________________________")

            self.introduceWholeFamily()

            self.expenses[0] = 0

    def livingOneMonth(self):
        self.months += 1
        print("Le NBR DE MOIS :", self.months)

        self._goldManagement()
        self._checkHousePayment()
        self._checkInflation()
        self._goToHolidays(self.holidaysExpense)

        print("Donc il reste à la maison :", self.economies)

    def livingMonths(self, nbrMonths, isDisplayed):
        for i in range(nbrMonths):
            self.livingOneMonth()
            self.x.append(self.months)
            self.y.append(self.economies)

            print("")
        self.introduceWholeHuman()
        if isDisplayed:
            self.displayAllGraph()

    def _goldManagement(self):
        currentExpenses = 0
        currentSalaryPart = 0
        for human in self.family:
            if isinstance(human, Human):
                currentSalaryPart += human.getSalaryPartition()
        self.receiveSalary(currentSalaryPart)

        print("Moi c'est,", self.name, "et mes depenses sont :", self.expenses)
        for exepense in self.expenses:  # Expense House
            currentExpenses += exepense
        self.total_expens += currentExpenses
        for livings in self.family:  # Expense Family
            if isinstance(livings, Livings):
                print("Moi c'est,", livings.getName(), "et mes depenses sont :", livings.getExpenses(), "et j'ai", livings.getAge(), "ans!")
                currentExpenses += livings.getExpensesValue()
                livings.livingOneMonth()
        self.payExpenses(currentExpenses, currentSalaryPart)

    def pay(self, value):
        self.economies -= value
