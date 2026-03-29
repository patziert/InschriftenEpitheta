#Webscraper zur Massenextraktion von Inschriften aus der EDCS bis 2025

import re, pandas, shapefile, matplotlib, werkzeug, csv
werkzeug.cached_property = werkzeug.utils.cached_property # ohne diese Zeile Fehler beim Laden von RoboBrowser
from robobrowser import RoboBrowser

global SUCHTABELLE

def initialize():
    global SUCHTABELLE
    #Definition der Suchanfragen an die EDCS
    #Suche tituli sepucrales
    sucheSepulcrales = {"p_gattung1" : "vel;tituli sepulcrales", "p_gattung2" : "inscriptiones christianae", "p_lingua" : "la"}
    #Suche tituli sepulcrales Substraktive späte Inschriften
    sucheSepulcralesMinus = {"p_gattung1" : "vel;tituli sepulcrales", "p_gattung2" : "inscriptiones christianae", "p_lingua" : "la", "p_dat_von" : "301"}
    #Suche Sonstige Inschriften
    sucheVaria = {"p_gattung2" : "vel;tituli sepulcrales;inscriptiones christianae", "p_lingua" : "la", "p_dat_von" : "-27", "p_dat_bis" : "300"}
    #Suche Alt
    sucheAlt ={"p_gattung1" : "vel;carmina;signacula;praenomen et nomen;defixiones;signacula medicorum;liberti/libertae;diplomata militaria;termini;milites;sacerdotes christiani;inscriptiones christianae;tesserae nummulariae;mulieres;sacerdotes pagani;leges;tituli fabricationis;nomen singulare;servi/servae;litterae erasae;tituli honorarii;officium/professio;seviri Augustales;litterae in litura;tituli operum;ordo decurionum;tria nomina;miliaria;tituli possessionis;ordo equester;viri;senatus consulta;tituli sacri;ordo senatorius;sigilla impressa;tituli sepulcrales", "p_gattung2" : "Augusti/Augustae;reges", "p_lingua" : "la", "p_dat_von" : "-27", "p_dat_bis" : "300"}
    #Suche Alt "Dis Manibus"
    sucheAlt ={"p_gattung1" : "vel;carmina;signacula;praenomen et nomen;defixiones;signacula medicorum;liberti/libertae;diplomata militaria;termini;milites;sacerdotes christiani;inscriptiones christianae;tesserae nummulariae;mulieres;sacerdotes pagani;leges;tituli fabricationis;nomen singulare;servi/servae;litterae erasae;tituli honorarii;officium/professio;seviri Augustales;litterae in litura;tituli operum;ordo decurionum;tria nomina;miliaria;tituli possessionis;ordo equester;viri;senatus consulta;tituli sacri;ordo senatorius;sigilla impressa;tituli sepulcrales", "p_gattung2" : "Augusti/Augustae;reges", "p_lingua" : "la"}

    suchIndex = {"searchresultSepulcrales" : sucheSepulcrales, "searchResultSepulcralesMinus" : sucheSepulcralesMinus, "searchResultWeitere" : sucheVaria, "searchresult" : sucheAlt}

    # Liste aller durchzuführenden EDCS-Suchanfragen
    suchliste = [suchIndex[SUCHTABELLE]]
    return suchliste

# Extrahiert Daten aus Markup und gibt diese als Series zurück
def serializeInscription(InscriptionSoup):
    # Inschriftentext
    
    texttemp = re.search(r"(?:Ort\:</b>.*?<br/>\n)(.*?)(:?<br/>)", InscriptionSoup, re.DOTALL)
    if texttemp is not None:
        text = texttemp.group(1)
    else:
        try:
            text = re.search(r"(?:Ort\:</b>.*<br/>\n)(.*?)(:?</p>)", InscriptionSoup, re.DOTALL).group(1)
        except:
            text =""
            print(InscriptionSoup)
   
    # Provinz der Inschrift
    try:
        provinz = re.search(r"(?:Provinz\:</b> )(.*?)(:?\s*<b>)", InscriptionSoup).group(1)
    except:
        provinz =""
        print(InscriptionSoup)
    # Ort der Inschrift, evtl mit Koordinaten
    orttemp = re.search(r"(?:ort=)(.*?)(:?&lat)", InscriptionSoup)
    breite = None
    laenge = None
    if orttemp is not None:
        ort = orttemp.group(1)
        breite = float(re.search(r"(?:&latitude=)(.*?)(:?&long)", InscriptionSoup).group(1))
        laenge = float(re.search(r"(?:&longitude=)(.*?)(:?&prov)", InscriptionSoup).group(1))
    else:
        try:
            ort = re.search(r"(?:Ort\:</b> )(.*?)(:?\s*<br/>)", InscriptionSoup).group(1)
        except:
            ort =""
            print(InscriptionSoup)
    # Datum der Inschrift
    datv = None
    datb = None
    dattemp = None
    dattemp = re.search(r"(?:Datierung\:</b>\s*\<b>a\:\s*</b>)(.*?)(:?\s*<b>)", InscriptionSoup)
    if dattemp:
        datv = dattemp.group(1)
        datb = re.search(r"(?:bis</b> )(.*?)(:?;(\s*<b>)|;)", InscriptionSoup).group(1)
        #print (datv+" bis "+datb)
    else:
        try:
            datv = re.search(r"(?:Datierung\:</b> )(.*?)(:?(\s*<b>)|;)", InscriptionSoup).group(1)
        except:
            datv = ""
        try:
            datb = re.search(r"(?:bis</b> )(.*?)(:?\s)", InscriptionSoup).group(1)
        except:
            datb = ""
    datv = str(datv)
    datb = str(datb)
    # Gattung der Inschrift
    gattung = None
    gattungtemp = re.search(r"(?:Inschriftengattung / Personenstatus\:</b>?\s*)(.*?)(:?(<br>|<p>|<br/>))", InscriptionSoup)
    #print (gattungtemp.group(0))
    try:
        gattung = gattungtemp.group(1)
    except:
        gattung = ""
    #
    #print (gattung)
    if gattung:
        print (gattung)
    # Erstellung und Rückgabe der Pandas-Series
    Inscription = pandas.Series([provinz, ort, breite, laenge, text, datv, datb, gattung],
                                index= ["Provinz", "Ort", "Breite", "Länge", "Text", "Datum von", "Datum bis", "Personenstatus / Inschriftengattung"])
    return Inscription

# Ausführung der Suchanfragen und Sammlung sämtlicher Inschriften in einem Dictionary
def getInscriptions(suchliste):
    br = RoboBrowser(parser="lxml") #Browser-Objekt br wird erstellt
    inscriptionset = {}
    # Iteration über Liste der Suchanfragen
    for q in suchliste:
        #Ausführung der Suche
        br.open("https://web.archive.org/web/20260126032101/https://db.edcs.eu/epigr/epi.php?s_sprache=de")
        form = br.get_form()
        for i in q:
            form[i].options = [q[i]]
            form[i].value = q[i]
        br.submit_form(form)
        # Vorbereitung der Serialiserung
        result = br.find_all("p")
        del result[0]
        del result[-1]
        # Serialiserung und Sammlung aller zurückgegeben Inschriften
        for r in result:
            try:
                inscription = serializeInscription(str(r))
                id = re.search("EDCS-\d+", str(r)).group()
                inscriptionset[id] = inscription
            except:
                continue
    return inscriptionset

# Erstellung der Shapefiles
def writeShapefile(Inscriptions):
    # Definition des Shapefiles
    shape = shapefile.Writer("vetinscr")
    shape.field("EDCS_ID", "C")
    shape.field("Provinz", "C")
    shape.field("Ort", "C", size=128)
    shape.field("Text", "C", size=255)
    shape.field("Datum von", "C")
    shape.field("Datum bis", "C")
    #Erstellen der Einträge
    for i in Inscriptions:
        if Inscriptions[i].at["Breite"] is not None:
            shape.point(Inscriptions[i].at["Länge"], Inscriptions[i].at["Breite"])
            shape.record(i, Inscriptions[i].at["Provinz"], Inscriptions[i].at["Ort"], Inscriptions[i].at["Text"], Inscriptions[i].at["Datum von"], Inscriptions[i].at["Datum bis"])
    # Abschließendes Speichen
    shape.close()

# Statistik der Fundortprovinzen
def printProvinceStats(Inscriptions):
    # Erstellen eine Dataframes aus den Series-Objekten
    frame = pandas.DataFrame(columns=["ID", "Provinz", "Ort", "Breite", "Länge", "Text"])
    for i in Inscriptions:
        frame = pandas.concat([frame, Inscriptions[i].to_frame(i).T], ignore_index=True)
    # Erstellen und Ausgabe von Tabelle 
    result = frame.groupby("Provinz").size()
    pandas.set_option('display.max_rows', 100)
    print (result)
    # Erstellen und Ausgabe von Graph
    result.plot(kind="barh")
    matplotlib.pyplot.show()
    
# Ausgabe der Inschriften als Tabelle
def writeTable(Inscriptions):
    global SUCHTABELLE
    frame = pandas.DataFrame(Inscriptions).T
    outcsv = frame.to_csv(quoting=csv.QUOTE_NONNUMERIC)
    file = open("./EDCS-Tabellen/"+SUCHTABELLE+".csv", "w", encoding="utf-8", newline='')
    file.write(outcsv)
    file.close()

# Main-Methode mit Statusmeldungen
def main():
    suchliste = initialize()
    print("Sammle Daten...")
    Inscriptions = getInscriptions(suchliste)
    print("Erstelle Shapefiles...")
    writeShapefile(Inscriptions)
    #print("Erstelle Statistik...")
    #printProvinceStats(Inscriptions)
    print("Erstelle Tabelle...")
    writeTable(Inscriptions)
    print(Inscriptions)
    
if __name__ == "__main__":
    SUCHTABELLE = "searchresult"
    main()