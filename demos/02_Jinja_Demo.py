from flask import Flask
from flask import render_template
from flask import request
import pandas as pd

DATENBANK = pd.read_csv ('Datenbank.csv')

app = Flask("Onlineshop")
vorname=""

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
    return render_template("kleidungsabfrage.html")



@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        applied_filters = request.form.getlist('artikel_filter')
        print (applied_filters)
        filtered_articles = DATENBANK[DATENBANK.filter_values.isin(applied_filters)]
        return render_template("add.html", articles=filtered_articles)


@app.route('/bezahlseite/', methods=['GET', 'POST'])
def bezahlseite():
    return render_template("bezahlseite.html")



@app.route('/warenkorb/', methods=['GET', 'POST'])
def warenkorb():
    return render_template("warenkorb.html")


@app.route('/verabschiedung/', methods=['GET', 'POST'])
def verabschiedung():
    return render_template("verabschiedung.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)