from Classes.CompanyClass import *

class Invest:
    # AllExpenses = [180, 40]  # Nourriture/Loisirs

    def __init__(self,human, name,invest_Rate, startDate, lifetime,investments, companies):
        self.human = human
        self.name = name

        self.invest_Rate = invest_Rate
        self.startDate = startDate
        self.lifetime = lifetime

        self.age_in_months = 0
        self.companies = []

        self.initalInvest = investments
        self.economies = investments

        self.x = []
        self.y = []


    def linkHumanToCompagny(self):
        for company in self.companies:
            if isinstance(company,Company):
                print("IL FAUT REFLECHIR A COMMENT TOUT RELIER")

    def livingOneMonth(self):
        self.age_in_months += 1

        self.checkLifeTime()

    def checkLifeTime(self):
        if self.age_in_months%12 == 0:

            self.economies += self.economies*self.invest_Rate
            print("Je suis",self.name, " et voici mes economies :", self.economies)

        if self.age_in_months == self.lifetime*12:
            print("Ca y est", self.name, "est de retour, voici ce que j'ai généré :", self.economies-self.initalInvest)
            self.giveBackMoney()

    def giveBackMoney(self):
        from Classes.BizarreClass import Human
        if isinstance(self.human,Human):
            if self.economies > 500:
                print("YES J'AI ATTEINT LES 500!!!")
                self.human.bePayed(self)
                self.economies = 0
                self._die()
            else:
                self.human.reInvest(self)
                self._die()

    def _die(self):
        self.human.delete_Invest(self)
        print("Ce fut un plaisir de travailler avec vous!")
        print()

    def getInvestRate(self):
        return self.invest_Rate
    def getLifeTime(self):
        return self.lifetime
    def getEconomies(self):
        return self.economies
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getName(self):
        return self.name

