#KOMMENTAR ZU DEM
from flask import Flask
from flask import render_template
from flask import request
import pandas as pd

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
@app.route("/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        global vorname
        vorname = request.form['vorname']
        return render_template("kleidungsabfrage.html", vorname=vorname)
    return render_template('index.html')


#Kleidungsabfrage:
#Abfrage nach den gewünschten Kleidungsstücken mit den gewünschten Grössen
#Wieso hier sehr wenig? und wieso der Name?
@app.route('/kleidungsabfrage/', methods=['GET', 'POST'])
def kleidungsabfrage():
    return render_template("kleidungsabfrage.html", vorname=vorname)


#Add_to_cart
#Auswahl der Kleidungsstücke, welche einem wirklich gefallen und möglichkeit neue Auswahl zu machen oder weiterzugehen
#Definition der globaen Variabeln, Zugriff auf die Datenbank über die Variabel "filtered_articles"
@app.route('/add_to_cart/', methods=['GET', 'POST'])
def add_to_cart():
    global applied_filters
    if request.method == 'POST':
        applied_filters = request.form.getlist('artikel_filter')
    filtered_articles = DATENBANK[DATENBANK.filter_values.isin(applied_filters)]
    return render_template("add_to_cart.html", articles=filtered_articles,)

#Warenkorb:
#Besätitung der Kleidungsstücke, Gesamtkosten und Gesamtstückzahl der Artikel werden angezeigt
@app.route('/warenkorb/', methods=['GET', 'POST'])
def warenkorb():
    article_selection = request.form.getlist('warenkorb')
    Anzahl =len(article_selection)
    selected_articles = DATENBANK[DATENBANK.artikelnummer.isin(article_selection)]
    global sum_prices
    sum_prices = selected_articles ['preis'].sum() #Berechnung der Gesamtkosten ohne Versandkosten
    return render_template("warenkorb.html", articles=selected_articles, sum=sum_prices, Anzahl_Art=Anzahl)

#Adressdaten
#Angabe der Adresse inkl. Land zur Berechnung der Versandkosten
@app.route('/adressdaten', methods=['GET', 'POST'])
def adressdaten():

    return render_template('adressdaten.html')

#Bezahlseite
#Berechnung der Gesamtkosten inkl. Länder-abhängigen Versandkosten und Auswahl der gewünschten Bezahlmöglichkeit. 
#Definition der gloaben Variabelen "email", da diese noch weiter auf der letzten Seite gebraucht wird
@app.route('/bezahlseite/', methods=['GET', 'POST'])
def bezahlseite():
    global email 
    email = request.form['email']
    name_vorname = request.form['name_vorname']
    strasse = request.form['adresse']
    wohnort = request.form['wohnort']
    country = request.form['länder']
    #Funktion um zu prüfen, welches Land der Nutzer auswählt, um dann je nach dem die entsprechenden Versandkosten auszugeben
    if country == "Schweiz": 
        Porto = 8
    elif country =="Deutschland":
        Porto = 15
    else: 
        Porto = 20

    Gesamtkosten =  sum_prices + Porto #Preisberechnung: Gesamtkosten = alle Artikel zusammen plus die Länderabhängigen Versandkosten

    return render_template("bezahlseite.html", email=email, name_vorname=name_vorname, strasse=strasse, wohnort=wohnort, Porto=Porto, Gesamtkosten=Gesamtkosten, sum=sum_prices)

#Verabschiedung
#Besätitung an E-Mail die aus der Adressseite gezogen wird
@app.route('/verabschiedung/', methods=['GET', 'POST'])
def verabschiedung():
    return render_template("verabschiedung.html", email=email, vorname=vorname)

#Brauch ich das
if __name__ == "__main__":
    app.run(debug=True, port=5000)