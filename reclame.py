#Opdracht 12
from algemene_functies import mijn_functie_2

#Opdracht 5
def aanbieding_1(smaak = "aardbei", prijs = "4", korting = "3,60"):
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.") 

aanbieding_1()


#Opdracht 6 en 7
inkomsten = [220, 430, 125, 160, 205, 90, 345]
def inkomsten_totaal():
    totaal = sum(inkomsten)
    btw = 0.09 * totaal
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden.")

inkomsten_totaal()


#Opdracht 8
def laag_en_hoog(mijn_lijst = [220, 430, 125, 160, 205, 90, 345] ):
    return_waarde = [min(mijn_lijst), max(mijn_lijst)]
    print(return_waarde)

laag_en_hoog()

#Opdracht 9 + 10
import statistics

def gemiddelde(mijn_lijst = [220, 430, 125, 160, 205, 90, 345]):
    gemiddelde_week = statistics.mean(mijn_lijst)
    print(f"De gemiddelde inkomsten deze week zijn {gemiddelde_week} euro.")

gemiddelde()

#Opdracht 11
def meervoudig(invoer_lijst = [10,5,3,2,1,2,9]): 
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer
    print(uitvoer)

meervoudig()

#Opdracht 12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer