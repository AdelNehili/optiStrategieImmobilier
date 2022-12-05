from matplotlib.pylab import *
from Classes.InvestClass import *
list_name = ["Mensualité", "Nourriture", "Vélo", "gaz", "electricité", "ass. habitation", "eau", "internet", "chaudière",
            "restorant", "Velo"]
list_price = [1300, 400, 30, 10, 50, 25, 60, 50, 7, 120, 30]


class Livings:
    # AllExpenses = [180, 40]  # Nourriture/Loisirs

    def __init__(self, name, age, expenses):

        self.name = name
        self.age = age
        self.expenses = expenses

        self.totalExpens = 0
        self.months = 0
        self.x = []
        self.y = []

        self.house = None
        self.sick_expense = 70
        self.no_sick_period = 1

        self.life_time = 80
    def showERROR(self, error_type):
        print("____________________")
        print("ATTENTION ERREUR DE TYPE", error_type)
        print("____________________")
        quit()

    def check_sickness(self):
        if self.months % (self.no_sick_period * 12) == 0:
            print("JE SUIIIIIS", self.name," et je suis, MALADDEUUUUU!")
            self.being_Sick()
    def being_Sick(self):
        from Classes.MaisonClass import Maison
        if isinstance(self.house,Maison):
            self.house.pay(self.sick_expense)

    def check_age_livings(self):
        if self.age> self.life_time:
            self.die()

    def die(self):
        if isinstance(self,Dog):
            print("WOUAF!! Je suis,", self.name, "et je vais faire pipi là bas!!")
        else:
            print("Je suis,", self.name, "et je me meuuuuurs!")
        from Classes.MaisonClass import Maison
        if isinstance(self.house,Maison):
            self.house.deleteFamilyMember(self)

    def setHouse(self, house):
        import Classes.MaisonClass
        if isinstance(house, Classes.MaisonClass.Maison):
            self.house = house
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getExpenses(self):
        return self.expenses

    def setExpenses(self, value):
        self.expenses[0] = value

    def getExpensesValue(self):
        # Plus logique que tout le monde garde "secret" ses dépenses => seul les Livings connaissent leur propres
        # dépenses
        currentExpense = 0
        for elem in self.expenses:
            currentExpense += elem
        # print("Je suis", self.name, "et je dépense par mois", currentExpense)
        return currentExpense

    def livingOneMonth(self):
        self.age += 1 / 12
        self.months += 1

        self.check_age_livings()
        self.check_sickness()
    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Human(Livings):

    def __init__(self, name, age, expenses, personalExpenses, salary, economies, color, economiesPartition):
        super().__init__(name, age, expenses)
        self.personalExpenses = personalExpenses
        self.salary = salary
        self.economies = economies
        self.color = color
        self.economiesPartition = economiesPartition

        self.promotion = 0
        self.promotionValue = 450
        self.retirement = 65

        self.listInvestissements = []

    def introduceYourself(self):
        print("Salut, mon nom est :", self.name)
        print("J'ai :", self.age, "ans")
        print("Et ça, c'est mon salaire :", self.salary)
        print("Bon c'est genant mais je t'avoue qu'il me reste plus que :", self.economies)
        print("")

    def spendMoney(self, prix):
        # Pour l'instant toutes les dépenses sont gérées par la Maison
        self.economies -= prix

    def bePayed(self,invest):
        if isinstance(invest,Invest):
            self.economies += invest.getEconomies()
            print("YOUHOU!! J'AI RECU",invest.getEconomies(),"DE",invest.getName(),"!!!!")
        else:
            self.showERROR(1)
    def reInvest(self,invest):
        if isinstance(invest,Invest):
            new_name = invest.getName() + "&&"
            self._invest(new_name,invest.getInvestRate(),invest.getLifeTime(),invest.getEconomies())
            print("YOUHOU!! J'AI REINVESTI",invest.getEconomies(),"DE",invest.getName(),"!!!!")

        else:
            self.showERROR(1)

    def spendMoneyForPersonalExpenses(self):
        for elem in self.personalExpenses:
            self.spendMoney(elem)

    def check_age_livings(self):
        super().check_age_livings()
        if self.age > self.retirement:
            if isinstance(self, Human):
                self.salary=0

    def getPromoted(self, gain):

        if self.promotion <= 2:  # On ne peut avoir une infinité de promotions
            if self.salary == 0:
                # Si on n'a pas de salaire, on ne peut pas avoir de promotion! Si on trouve un job,
                # une autre fonction s'occupe de rendre le salaire different de zero
                self.salary += 0

            else:
                self.promotion+=1
                self.salary += gain
                print("YEEEES J'AI EU MA PROMOTIIIIION ET MON SALAIRE DEVIENT: ", self.salary)
    def checkPromotion(self):
        if self.months % (5 * 12) == 0:
            self.getPromoted(self.promotionValue)

    def livingOneMonth(self):
        super().livingOneMonth()
        self.checkPromotion()
        self.spendMoneyForPersonalExpenses()
        for investissements in self.listInvestissements:
            investissements.livingOneMonth()

    def getSalaryPartition(self):
        # Cette fonction incremente l'axe des temps (x), c'est investAndEcoForHouse qui incremente l'axe y

        humanEconomiesPartition = self.economiesPartition
        houseEconomiesPartition = 1 - humanEconomiesPartition

        houseEconomies = self.investAndEcoForHouse(houseEconomiesPartition, humanEconomiesPartition)
        return houseEconomies

    def investAndEcoForHouse(self, houseEconomiesPartition, humanEconomiesPartition):
        # Coucou, je m'occupe d'incrémenter l'axe Y (economies)
        if humanEconomiesPartition + houseEconomiesPartition == 1:
            houseEconomies = houseEconomiesPartition * self.salary
            humanEconomies = humanEconomiesPartition * self.salary
        else:
            houseEconomies = self.salary
            humanEconomies = 0

        self.economies += humanEconomies
        self.y.append(self.economies)
        return houseEconomies

    def delete_Invest(self,invest):
        if isinstance(invest,Invest):
            if invest in self.listInvestissements:
                self.listInvestissements.remove(invest)

    def _invest(self, name, invest_Rate, lifetime, investValue):
        # Fonction permettant de modéliser l'investissement en bourse
        startDate = self.months
        invest = Invest(self, name, invest_Rate, startDate, lifetime, investValue, [])
        self.listInvestissements.append(invest)
        self.economies -= investValue
    def investForCompanies(self,nbr_invest,invest_Rate, lifetime, investValue):
        for i in range(nbr_invest):
            name = "Invest N°"+ str(i)
            self._invest(name,invest_Rate,lifetime,investValue)
    def getSalary(self):
        return self.salary
    def setSalary(self, newSalary):
        self.salary = newSalary
    def getEconomies(self):
        return self.economies
    def setEconomies(self, value):
        self.economies = value
    def setEconomiesPartition(self, newEconomiesPartition):
        self.economiesPartition = newEconomiesPartition
    def setPersonalExpenses(self,newPersonalExpenses):
        self.personalExpenses = newPersonalExpenses
    def getColor(self):
        return self.color

class Bizarre(Human):

    def __init__(self, name, age, expenses, personalExpenses, salary, economies, color, economiesPartition, lvlBizarre):
        super().__init__(name, age, expenses, personalExpenses, salary, economies, color, economiesPartition)
        self.lvlBizarre = lvlBizarre
        super().introduceYourself()

class Child(Human):

    def __init__(self, name, age, expenses, allocation, color, months):
        super().__init__(name, age, expenses, [0], allocation, 0, color, 0)
        self.introduceYourself()
        self.months = months
        self.adapt_Y_axe()
        self.promotionValue = 0
        print("OUIIIIIIN JE SUIS NEEEE")

    def adapt_Y_axe(self):
        # Allow to show the economies axe (y) with at the current month
        for i in range(self.months - 1):
            self.y.append(0)

    def check_age_livings(self):
        super(Child, self).check_age_livings()
        if self.age > 25:
            print("Yo je suis le djeunes :", self.name)
            print("NAAAAAN PAPAAAA, MAMAAAAAN JE PEUX CHANGEEEEER! LAISSEZ MOI ENTRER!!!")
            self.die()

    def check_age_child(self):
        if self.age <= 3:
            self.setExpenses(500)
        if 3 < self.age <= 6:
            self.setExpenses(500)
        if 6 < self.age < 12:
            self.setExpenses(450)
        if 6 < self.age < 12:
            self.setExpenses(450)
        if 12 < self.age < 18:
            self.setExpenses(560)
        if 25 < self.age:
            self.salary=0

    def livingOneMonth(self):
        super(Child, self).livingOneMonth()
        self.check_age_child()
        self.economies+=self.expenses[1]

    def getExpensesValue(self):
        this_Expense = 0
        for elem in self.expenses:
            this_Expense += elem

        return this_Expense

class Dog(Livings):

    def __init__(self, name, age, expenses):
        super().__init__(name, age, expenses)
        self.life_time = 11
        self.start_expenses = [2000,5*100] # 2000 à l'achat et 5 vaccins

    def get_Start_Expenses_Value(self):
        value = 0
        for expense in self.start_expenses:
            value+=expense
        return value

    def livingFirstMonth(self):

        if self.house is not None:
            print("CETTE MAISON (",self.house.getName(),")A DU CHIEN!!")
            from Classes.MaisonClass import Maison
            if self.months <= 1 and isinstance(self.house,Maison):
                print("JE SUIS TROOOOP MIGNON, ET C'EST MON PREMIER MOIS!")
                value = self.get_Start_Expenses_Value()
                self.house.pay(value)
                print("OUCH je suis,", self.name," et j'aime PAS les vaccins >_< !!")
    def livingOneMonth(self):
        if self.months < 1:
            self.livingFirstMonth()
        super(Dog, self).livingOneMonth()