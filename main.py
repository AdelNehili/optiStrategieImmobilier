from Classes.MaisonClass import *
from Classes.InvestClass import *
from Classes.CompanyClass import *


def setupFamilyHouse():
    whole_Family = []

    human_Expenses = [100, 60]
    personal_Expenses = [50]

    bizarre_male = Bizarre("ElTortueAdaptor", 30, human_Expenses, personal_Expenses, 2100, 10000, "g-", 0.10, 8)
    bizarre_femelle = Bizarre("MamanDePoupouille", 30, human_Expenses, personal_Expenses, 1500, 10000, "b-", 0.1, 9)

    houseFamily = [bizarre_femelle, bizarre_male]
    houseEconomies = 0
    """
    houseExpenses = [2400, 125]
    housePrice = 725000
    """

    houseExpenses = [1000, 125]
    housePrice = 347000
    maison = Maison("MaisonBizarre", houseExpenses, housePrice, houseFamily, houseEconomies, "r-")

    whole_Family.append(bizarre_male)
    whole_Family.append(bizarre_femelle)
    whole_Family.append(maison)
    return whole_Family
def createCar(house):
    car = Car("BizarreMobile", 0, [25000, 350], 25000)  # 4150 pour une voiture 3000 payé e
    if isinstance(house, Maison):
        house.addFamilyMember(car)
def createEnfant(house, name, expenses, allocation, current_months, color):
    #Pour rappel, expenses[0] = dépense moyenne d'un enfant et expenses[1]= 50euro d'eco par mois
    child = Child(name, 0, expenses, allocation, color, current_months)
    if isinstance(house, Maison):
        house.addFamilyMember(child)
def create_MyBABY_Dog(house, name, age):
    dog = Dog(name, age, [100, 40])
    if isinstance(house, Maison):
        house.addFamilyMember(dog)

def newStrategy(bizarre_male, bizarre_femelle, salaryPartition, house):
    if isinstance(bizarre_male, Human) and isinstance(bizarre_femelle, Human):
        bizarre_male.setEconomiesPartition(salaryPartition)
#        bizarre_male.setSalary(bizarre_male.getSalary())
        bizarre_male.setPersonalExpenses([0])

        bizarre_femelle.setSalary(0)
        bizarre_femelle.setEconomiesPartition(salaryPartition)
        bizarre_femelle.setPersonalExpenses([0])

    #Les allocations augmentent s'il n'y a qu'une personne qui travaille
    if isinstance(house,Maison):
        for child in house.getFamily():
            if isinstance(child,Child):
                child.setSalary(240)

holidays_expenses = 0
isDisplayed = 0

test1 = 0
if test1:
    # Chap Zero : INtroDucTioN
    familyHouse = setupFamilyHouse()
    bizarre_male = familyHouse[0]
    bizarre_femelle = familyHouse[1]
    maison = familyHouse[2]

    # First Chap : Happy old years
    maison.livingMonths(2 * 12, 0)
    create_MyBABY_Dog(maison, "Happa", 0)
    create_MyBABY_Dog(maison, "Grotas",0)
    maison.livingMonths(1 * 12, isDisplayed)
    maison.setHolidaysExpense(1500)


    # Second Chap : first child
    createEnfant(maison, "enfant1", [500,50], 150, maison.getMonths(), "k-")
    maison.livingMonths(4 * 12, isDisplayed)


    # Third Chap : second child
    createEnfant(maison, "enfant2", [500,50], 150, maison.getMonths(), "y-")
    createCar(maison)
    newStrategy(bizarre_male, bizarre_femelle,0,maison)
    maison.livingMonths(3 * 12, isDisplayed)


    # Fourth Chap : Third child
    maison.livingMonths(3 * 12, isDisplayed)

    maison.livingMonths(4 * 12, 1)

    maison.livingMonths(15 * 12, 1)

test2 = 1
if test2:
    # Test d'un appart à louer
    expenses = [80, 0]
    salary = 600 + 250 + 50
    #salary = 1200

    economies = 2000
    personal_Expenses = [0]
    bizarre_femelle = Bizarre("MamanDePoupouille", 29, expenses, personal_Expenses, salary, economies, "b-", 0, 9)

    houseFamily = [bizarre_femelle]
    houseEconomies = 0
    houseExpenses = [750, 0]
    housePrice = 99999999999999
    maison = Maison("MaisonBizarre", houseExpenses, housePrice, houseFamily, houseEconomies, "r-")
    maison.setHolidaysExpense(0)
    maison.livingMonths(3 * 12, 1)

testInvestissement = 0
if testInvestissement:
    # Chap Zero : INtroDucTioN
    familyHouse = setupFamilyHouse()
    bizarre_male = familyHouse[0]
    bizarre_femelle = familyHouse[1]
    maison = familyHouse[2]
    maison.setHolidaysExpense(0)

    maison.livingMonths(1 * 12, 0)

    nbrYears = 5
    nbr_invest = 3

    for i in range(10):
        bizarre_male.investForCompanies(nbr_invest,0.1,nbrYears,0.01*bizarre_male.getEconomies())
        maison.livingMonths(1 * 12, 0)


    maison.livingMonths(30 * 12, 1)

testMama = 0
if testMama:
    mensuality = 733
    value = 65000-4*12*mensuality
    print("La valeur vaut =", value)