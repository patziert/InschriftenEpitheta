#Zentrales Steuerungsinterface für die Einzelskripte

from Kernskripte import EDCSScraper, InschriftenAnalyse, AdjStats, PPAStats, listtotable, adjdependencies
from Hilfsskripte import *
from Evaluationsskripte import evaltabgen, evaltabgen2, evaltabgen3, evaltabgen4, evaltabgen5
from Tabellengenerationsskripte import findlisttabgen, findlisttabgenZ, bezzuschrtabgen, mfnplace, placetables, statprov, statustables, superlative, bezplace, bezstatus, AlterListe, mfnstats, mfnstats2, mfnstats3, mfnstats4, bezzuschrtabgenRom

def question1():
    global KORPUS
    global SUCHTABELLE
    option1 = input("Wählen Sie das zu bearbeitende Korpus aus den Optionen: \n 1: Korpus_Sepulcrales \n 2: Korpus_Varia \n 3: inscraccs_test \nIhre Wahl: ")
    match option1:
        case "1":
            KORPUS = "Korpus_Sepulcrales"
            SUCHTABELLE = "searchresultSepulcralesReduziert"
        case "2":
            KORPUS = "Korpus_Varia"
            SUCHTABELLE = "searchresultWeitere"
        case "3":
            KORPUS = "inscraccs_test"
            SUCHTABELLE = "searchresult"
        case _:
            print("Ungültige Option")
            question1()

def question2():
    global KORPUS
    global SUCHLISTE
    option2 = input("Wählen Sie den gewünschten Prozess: \n 1: ECDS-Suche (ACHTUNG: DERZEIT NICHT FUNKTIONAL!) \n 2: Verarbeitung und Begriffssuche \n 3: Generiere Evaluationstabellen (Korpusübergreifend) \n 4: Generiere Ausgabetabellen \nIhre Wahl: ")
    match option2:
        case "1":
            if SUCHTABELLE == "searchresultSepulcralesReduziert":
                EDCSScraper.SUCHTABELLE = "searchresultSepulcrales"
                EDCSScraper.main()
                SUCHLISTE = "searchresultSepulcralesMinus"
                EDCSScraper.main()
                Hilfsskripte.searchcombine3.main()
            else:
                EDCSScraper.SUCHTABELLE = SUCHTABELLE
                EDCSScraper.main()
        case "2":
            question3()
        case "3":
            print("Generiere Tabelle 1...")
            evaltabgen.main()
            print("Generiere Tabelle 2...")
            evaltabgen2.main()
            print("Generiere Tabelle 3...")
            evaltabgen3.main()
            print("Generiere Tabelle 4...")
            evaltabgen4.main()
            print("Generiere Tabelle 5...")
            evaltabgen5.main()
        case "4":
            bezzuschrtabgen.KORPUS = KORPUS
            bezzuschrtabgen.main()
            bezzuschrtabgenRom.KORPUS = KORPUS
            bezzuschrtabgenRom.SUCHTABELLE = SUCHTABELLE
            bezzuschrtabgenRom.main()
            mfnplace.KORPUS = KORPUS
            mfnplace.SUCHTABELLE = SUCHTABELLE
            mfnplace.main()
            placetables.KORPUS = KORPUS
            placetables.SUCHTABELLE = SUCHTABELLE
            placetables.main()
            statprov.KORPUS = KORPUS
            statprov.SUCHTABELLE = SUCHTABELLE
            statprov.main()
            statustables.KORPUS = KORPUS
            statustables.SUCHTABELLE = SUCHTABELLE
            statustables.main()
            superlative.KORPUS = KORPUS
            superlative.main()
            bezplace.KORPUS = KORPUS
            bezplace.SUCHTABELLE = SUCHTABELLE
            bezplace.main()
            bezstatus.KORPUS = KORPUS
            bezstatus.SUCHTABELLE = SUCHTABELLE
            bezstatus.main()
            AlterListe.KORPUS = KORPUS
            AlterListe.SUCHTABELLE = SUCHTABELLE
            AlterListe.main()
            mfnstats4.KORPUS = KORPUS
            mfnstats4.main()
            mfnstats2.KORPUS = KORPUS
            mfnstats2.main()
            mfnstats.KORPUS = KORPUS
            mfnstats.SUCHTABELLE = SUCHTABELLE
            mfnstats.main()
            mfnstats3.KORPUS = KORPUS
            mfnstats3.main()
        case _:
            print("Ungültige Option")
            question2()

def question3():
    global KORPUS
    global SUCHTABELLE
    option3 = input("Wählen Sie den Prozessumfang: \n 1: Voller Prozess \n 2: Nur LatinCy-Analyse \n 3: Nur Postprozession \nIhre Wahl: ")
    match option3:
        case "1":
            InschriftenAnalyse.KORPUS = KORPUS
            InschriftenAnalyse.SUCHTABELLE = SUCHTABELLE
            InschriftenAnalyse.main()
            AdjStats.KORPUS = KORPUS
            PPAStats.KORPUS = KORPUS
            AdjStats.main()
            PPAStats.main()
            listtotable.KORPUS = KORPUS
            listtotable.SUCHTABELLE = SUCHTABELLE
            listtotable.TYPE = "adj"
            listtotable.main()
            listtotable.TYPE = "participle"
            listtotable.main()
            adjdependencies.KORPUS = KORPUS
            adjdependencies.main()
            findlisttabgen.KORPUS = KORPUS
            findlisttabgen.SUCHTABELLE = SUCHTABELLE
            findlisttabgen.main()
            findlisttabgenZ.KORPUS = KORPUS
            findlisttabgenZ.SUCHTABELLE = SUCHTABELLE
            findlisttabgenZ.main()
        case "2":
            InschriftenAnalyse.KORPUS = KORPUS
            InschriftenAnalyse.SUCHTABELLE = SUCHTABELLE
            InschriftenAnalyse.main()
        case "3":
            AdjStats.KORPUS = KORPUS
            PPAStats.KORPUS = KORPUS
            AdjStats.main()
            PPAStats.main()
            listtotable.KORPUS = KORPUS
            listtotable.SUCHTABELLE = SUCHTABELLE
            listtotable.TYPE = "adj"
            listtotable.main()
            listtotable.TYPE = "participle"
            listtotable.main()
            adjdependencies.KORPUS = KORPUS
            adjdependencies.main()
            findlisttabgen.KORPUS = KORPUS
            findlisttabgen.SUCHTABELLE = SUCHTABELLE
            findlisttabgen.main()
            findlisttabgenZ.KORPUS = KORPUS
            findlisttabgenZ.SUCHTABELLE = SUCHTABELLE
            findlisttabgenZ.main()
        case _:
            print("Ungültige Option")
            question3()


global KORPUS
global SUCHTABELLE

def main():
    question1()
    question2()

if __name__ == "__main__":
    main()