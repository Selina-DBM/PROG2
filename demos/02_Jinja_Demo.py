from flask import Flask #Kommt aus der Flask Bibliothek: mit dem wird Flask importiert und damit auch direkt Jinja
from flask import render_template #Kommt aus der Flask Bibiliothek um die Funktion: Return render_template auszuführen
from flask import request #Kommt aus der Flask Bibiliothek um die Funktionen: request.. auszuführen
import pandas as pd #Es ermöglicht das einlesen einer CSV Datenbank und direkte Zuordnung der pd Variable

#Import der CSV Datenbank
DATENBANK = pd.read_csv ('Datenbank.csv')

#Definition der gloabeln Variabeln
app = Flask("Onlineshop") 
vorname=""
sum_prices =""
applied_filters =[] 
email = ""

#Index Seite:
#Startseite und erste Begrüssung inkl. Abfrage nach dem Namen
#Definition der gloaben Variable: Name inkl. der Übergabe der Variabeln an die nächste Seite
@app.route("/", methods=['GET', 'POST']) #Zur Benutzung von GET und POST muss als methods beides definiert sein
def hallo():
    if request.method == 'POST':#Durch die POST Method wird der Name nicht in der URL eingeführt
        global vorname
        vorname = request.form['vorname'] #request.form wird verwendet da es nur einen Wert gibt, den man hier einträgt
        return render_template("kleidungsabfrage.html", vorname=vorname) #Übergabe der Variabeln an die nächste Seite
    return render_template('index.html')


#Kleidungsabfrage:
#Abfrage nach den gewünschten Kleidungsstücken mit den gewünschten Grössen
#Wieso hier sehr wenig? und wieso der Name?
@app.route('/kleidungsabfrage/', methods=['GET', 'POST'])#Zur Benutzung von GET und POST muss als methods beides definiert sein
def kleidungsabfrage():
    return render_template("kleidungsabfrage.html", vorname=vorname)#Übergabe der Variabeln an die nächste Seite


#Add_to_cart
#Auswahl der Kleidungsstücke, welche einem wirklich gefallen und möglichkeit neue Auswahl zu machen oder weiterzugehen
#Definition der globaen Variabeln, Zugriff auf die Datenbank über die Variabel "filtered_articles"
@app.route('/add_to_cart/', methods=['GET', 'POST'])#Zur Benutzung von GET und POST muss als methods beides definiert sein
def add_to_cart():
    global applied_filters
    if request.method == 'POST':#Wenn es ein POST request ist, dann kann dem applied_filters ein Wert zugeordnet werden 
        applied_filters = request.form.getlist('artikel_filter')#Getlist wird verwendet, da im Key artikel_filter mehrere Werte entgegen genommen werden
    filtered_articles = DATENBANK[DATENBANK.filter_values.isin(applied_filters)] #Inhalt in [] steht für die Abfrage ob die Zeile true or false ist und dies ist abhängig von dem angewendeten Filter
    return render_template("add_to_cart.html", articles=filtered_articles) #Übergabe der Variabeln an die nächste Seite

#Warenkorb:
#Bestätigung der Kleidungsstücke, Gesamtkosten und Gesamtstückzahl der Artikel werden angezeigt
@app.route('/warenkorb/', methods=['GET', 'POST'])#Zur Benutzung von GET und POST muss als methods beides definiert sein
def warenkorb():
    article_selection = request.form.getlist('warenkorb') #Getlist wird verwendet, da es mehrere Werte im Key warenkorb entgegen genommen werden
    Anzahl =len(article_selection)
    selected_articles = DATENBANK[DATENBANK.artikelnummer.isin(article_selection)]
    global sum_prices
    sum_prices = selected_articles ['preis'].sum() #Berechnung der Gesamtkosten ohne Versandkosten
    return render_template("warenkorb.html", articles=selected_articles, sum=sum_prices, Anzahl_Art=Anzahl) #Übergabe der Variabeln an die nächste Seite

#Adressdaten
#Angabe der Adresse inkl. Land zur Berechnung der Versandkosten
@app.route('/adressdaten', methods=['GET', 'POST'])#Zur Benutzung von GET und POST muss als methods beides definiert sein
def adressdaten():

    return render_template('adressdaten.html') #Übergabe der Variabeln an die nächste Seite

#Bezahlseite
#Berechnung der Gesamtkosten inkl. Länder-abhängigen Versandkosten und Auswahl der gewünschten Bezahlmöglichkeit. 
#Definition der gloaben Variabelen "email", da diese noch weiter auf der letzten Seite gebraucht wird
@app.route('/bezahlseite/', methods=['GET', 'POST'])#Zur Benutzung von GET und POST muss als methods beides definiert sein
def bezahlseite():
    global email 
    email = request.form['email']
    name_vorname = request.form['name_vorname']
    strasse = request.form['adresse']
    wohnort = request.form['wohnort']
    country = request.form['länder']
    #if / else Funktion um zu prüfen, welches Land der Nutzer auswählt, um dann je nach dem die entsprechenden Versandkosten auszugeben
    if country == "Schweiz": 
        Porto = 8
    elif country =="Deutschland":
        Porto = 15
    else: 
        Porto = 20

    Gesamtkosten =  sum_prices + Porto #Preisberechnung: Gesamtkosten = alle Artikel zusammen plus die Länderabhängigen Versandkosten

    return render_template("bezahlseite.html", email=email, name_vorname=name_vorname, strasse=strasse, wohnort=wohnort, Porto=Porto, Gesamtkosten=Gesamtkosten, sum=sum_prices)#Übergabe der Variabeln an die nächste Seite

#Verabschiedung
#Besätitung an E-Mail die aus der Adressseite gezogen wird
@app.route('/verabschiedung/', methods=['GET', 'POST'])#Zur Benutzung von GET und POST muss als methods beides definiert sein
def verabschiedung():
    return render_template("verabschiedung.html", email=email, vorname=vorname)

#Brauch ich das???
if __name__ == "__main__":
    app.run(debug=True, port=5000)