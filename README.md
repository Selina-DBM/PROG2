# Projektvorhaben Onlineshop
## Ausgangslage
Ich wollte einen Onlineshop entwickeln. Für diesen habe ich mich entschieden einen einfachen Aufbau zu wählen. Der Kunde wir mit seinem Namen begrüsst und anschliessend wird er durch die Seite durchgeführt und kann sich seine Kleidungsstücke aussuchen. Er wird nach Adresse etc. gefragt und kann nach Berechnung der Versandkosten seiner Bestellung abschliessen und die Artikel kaufen. 

## Flussdiagram
!(Flussdiagram.png)
## Funktionen
- Name eingeben
- Artikel filtern
- Artikel auswählen
- Artikel zum Warenkorb hinzufügen
- Adresse eintragen
- Gesamtkosten inkl. Länder-abhängigen Versandkosten anschauen

## Begrüssungsseite
(./Begrüssungsseite.png)
Die erste Seite ist sehr simpel gehalten. Der Benutzer wird begrüsst und nach seinem Namen gefragt. 
Diese Seite soll als Einstieg genutzt werden und dafür da sein, dass der Benutzer in den nächsten Schritten immer mit dem Namen angesprochen werden kann.  

## Kleidungsabfrage-Seite
Die zweite Seite in meinem Onlineshop ist die Abfrage, welche Kleidungsstücke für einen interessant sind. Dafür habe ich eine Tabelle erstellt, in der es Checkboxen gibt. Diese Boxen decken immer eine Konstellation zwischen Kleidungsstück und Grösse ab. Die Tabelle ist grundsätzlich die einfachste Möglichkeit eine solche Abfrage zu machen. 
Anschliessend kann der Benutzer weiter gehen mit seiner getroffenen Auswahl. 

## Add_to_cart-Seite
Die nächste Seite startet ganz oben mit einem Text und einem Abbrechen Button. Dieser ist dafür da, falls die gezeigten Kleidungsstücke nicht mit dem gewünschten Ergebnis übereinstimmen, eine Neue Auswahl zu treffen. 

Anschliessend werden die Kleidungsstücke angezeigt, für die vorher das Häckchen angewählt wurde. Zusätzlich zu den Bildern der Kleidungsstücke werden auch Preis und Grösse angezeigt. Dies hilft dem Kunden zur Übersicht und ist natürlich auch relevant für die schlussendliche Kaufentscheidung. 
Jedes Kleidungsstück kann anschliessend einzeln angewählt werden, da der Kunde dann doch vielleicht nur eine Hose möchte, anstatt Hose und Jacke. 

## Warenkorb Seite
Diese Seite ist der Warenkorb. Wie bei vielen Onlineshops werden hier alle ausgewählten Kleidungsstücke erneut angezeigt. Zusätzlich werden die Anzahl Artikel angezeigt und der Gesamtpreis ohne Versandkosten.
Falls diese Auswahl dem entspricht, was man bestellen möchte, kann man nun die Auswahl bestätigen. 

## Adressdaten
Die Seite Adressdaten fragt dann ab welche Adresse man für die Lieferung haben möchte. Zusätzlich wird auch das Land abgefragt, dieses ist dann wiederum relevant für die Berechnung der Versandkosten. Die Länderauswahl ist nicht mit Checkboxen sondern mit einer Art Dropdown Auswahl gespeichert. Dadurch kann der Benutzer nur ein Land auswählen und nicht ausversehen mehrere. 
Auch hier gibt es wieder die Möglichkeit über einen Submit-Input Button dann weiterzugehen oder abzubrechen. 

## Bezahlseite
Auf der Bezahlseite werden die Gesamtkosten inkl. der Länderabhängigen Versandkosten angezeigt. Zusätzlich wird noch einmal die Adresse angezeigt, als Hilfe zur Übersicht. Abschliessend ist auch noch eine Auswahl zwischen Rechnung, Kredit Karte  und PayPal vorhanden, dort kann man auswählen, welche Zahlungsart man möchte. 

## Verabschiedung
Hier wird der Kunde noch einmal verabschiedet. 
 

