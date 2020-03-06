from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello World")

@app.route("/index/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        vorname = request.form['vorname']
        return render_template("seite1.html")
    return render_template('index.html')




@app.route('/seiteeins')
def seiteeins():
    return render_template("seite1.html")



@app.route('/seitezwei')
def seitezwei():
    return render_template("seite2.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)