from flask import Flask
from flask import render_template
from flask import request
import pandas as pd

DATENBANK = pd.read_csv ('Datenbank.csv')

app = Flask("Onlineshop")
vorname=""
sum_prices =""
applied_filters =[]

@app.route("/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        global vorname
        vorname = request.form['vorname']
        print(vorname)
        return render_template("kleidungsabfrage.html", vorname=vorname)
        print (applied_filters)
    return render_template('index.html')



@app.route('/kleidungsabfrage/', methods=['GET', 'POST'])
def kleidungsabfrage():
    return render_template("kleidungsabfrage.html", vorname=vorname)



@app.route('/add_to_cart/', methods=['GET', 'POST'])
def add_to_cart():
    global applied_filters
    if request.method == 'POST':
        applied_filters = request.form.getlist('artikel_filter')
    filtered_articles = DATENBANK[DATENBANK.filter_values.isin(applied_filters)]
    return render_template("add_to_cart.html", articles=filtered_articles,)

@app.route('/warenkorb/', methods=['GET', 'POST'])
def warenkorb():
    article_selection = request.form.getlist('warenkorb')
    Anzahl =len(article_selection)
    selected_articles = DATENBANK[DATENBANK.artikelnummer.isin(article_selection)]
    global sum_prices
    sum_prices = selected_articles ['preis'].sum()
    return render_template("warenkorb.html", articles=selected_articles, sum=sum_prices, Anzahl_Art=Anzahl)

@app.route('/adressdaten', methods=['GET', 'POST'])
def adressdaten():
    return render_template('adressdaten.html')


@app.route('/bezahlseite/', methods=['GET', 'POST'])
def bezahlseite():
    return render_template("bezahlseite.html")


@app.route('/verabschiedung/', methods=['GET', 'POST'])
def verabschiedung():
    return render_template("verabschiedung.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)