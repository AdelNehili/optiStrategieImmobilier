from Classes.VoitureClass import *
from Classes.MaisonClass import *

"""
Permet de vérifier que les allocations ne soient pas interpretées comme des salaires (pas de promotion) 
=> la promotionvalue des child =0
Permet de vérifier si le salaire des parent augmente bien quand il le faut
"""

def setupFamilyHouse():
    whole_Family = []

    human_Expenses = [100, 60]
    personal_Expenses = [50]

    bizarre_male = Bizarre("ElTortueAdaptor", 30, human_Expenses, personal_Expenses, 2100, 10000, "g-", 0.10, 8)
    bizarre_femelle = Bizarre("MamanDePoupouille", 29, human_Expenses, personal_Expenses, 1200, 10000, "b-", 0.1, 9)

    houseFamily = [bizarre_femelle, bizarre_male]
    houseEconomies = 0
    """
    houseExpenses = [2400, 125]
    housePrice = 725000
    """

    houseExpenses = [1400, 125]
    housePrice = 331000
    maison = Maison("MaisonBizarre", houseExpenses, housePrice, houseFamily, houseEconomies, "r-")

    whole_Family.append(bizarre_male)
    whole_Family.append(bizarre_femelle)
    whole_Family.append(maison)
    return whole_Family
def createCar(house):
    car = Car("BizarreMobile", 0, [25000, 250], 25000)  # 4150 pour une voiture 3000 payé e
    if isinstance(house, Maison):
        house.getFamily().append(car)
def createEnfant(house, name, expenses, allocation, current_months, color):
    child = Child(name, 0, expenses, allocation, color, current_months)
    if isinstance(house, Maison):
        house.getFamily().append(child)
def create_MyBABY_Dog(house, name, age,):
    dog = Livings(name, age, [100, 40])
    if isinstance(house, Maison):
        house.getFamily().append(dog)
        # cout d'un chien à l'achat
        house.pay(2000)
def newStrategy(bizarre_male, bizarre_femelle, salaryPartition):
    if isinstance(bizarre_male, Human) and isinstance(bizarre_femelle, Human):
        bizarre_male.setEconomiesPartition(salaryPartition)
        bizarre_male.setPersonalExpenses([0])

        bizarre_femelle.setSalary(0)
        bizarre_femelle.setEconomiesPartition(salaryPartition)
        bizarre_femelle.setPersonalExpenses([0])

def showAllSalary(house,global_count):
    global_count += 1
    print("NBR appel =", global_count)
    if isinstance(house,Maison):
        for human in house.getFamily():
            if isinstance(human,Human):
                print("ALORS Le salaire de", human.getName(), "vaut :", human.getSalary())
        print("______________________________")

isDisplayed = 0
global_count = 0
test1 = 1
if test1:
    # Chap Zero : INtroDucTioN
    familyHouse = setupFamilyHouse()
    bizarre_male = familyHouse[0]
    bizarre_femelle = familyHouse[1]
    maison = familyHouse[2]
    maison.setHolidaysExpense(0)

    # First Chap : Happy old years
    showAllSalary(maison,global_count)
    maison.livingMonths(3 * 12, 0)
    showAllSalary(maison,global_count)

    # Second Chap : first child
    createEnfant(maison, "enfant1", [500,50], 150, maison.getMonths(), "k-")
    maison.livingMonths(4 * 12, isDisplayed)
    showAllSalary(maison,global_count)

    # Third Chap : second child
    createEnfant(maison, "enfant2", [500,50], 150, maison.getMonths(), "y-")
    createCar(maison)
    newStrategy(bizarre_male, bizarre_femelle,0)
    maison.livingMonths(3 * 12, isDisplayed)
    showAllSalary(maison,global_count)

    # Fourth Chap : Third child
    newStrategy(bizarre_male, bizarre_femelle,0.01)
    maison.livingMonths(3 * 12, isDisplayed)
    showAllSalary(maison,global_count)
    maison.livingMonths(2 * 12, 1)
    showAllSalary(maison,global_count)



    """
    
    """

    maison.livingMonths(15 * 12, 1)
    showAllSalary(maison,global_count)