# M226a

Im Modul M226a geht es um Objekt basiertes Programmieren.

***Was ist Objektorientiertes Programmieren ?***

Beim Objektorientes programmieren werden Programme in Gruppen unterteilt, diese werden Objekte gennent. Jedes Objekt in einer Klasse wird gleich aufgebaut, sie haben alle verschiedene Eigenschaften, aber die gleichen Attributen. Jedes Objekt hat ihre Aufgaben/Funktionen, die man Methoden nennt. Mit diesen Methoden kann man Daten verändern und zu seinen Zweck nutzen.

***Beispiel***

Zum verdeutlichen, werden wir ein Pferd als beispiel nehmen:

Das erste Pferd nennen wir Hans.

Klasse: Pferd

Objekt: Hans

Seine Attribute:
- Hans ist Braun.
- Hans höchst Geschwindigkeit ist 20Km/h.
- Hans ist ein Arravani.

Methoden:
- Hans kann springen.
- Hans kann essen.
- Hans kann laufen.

``` python

Hans = Pferd()

#Attribute
Hans.Farbe = "Braun"
Hans.Geschwindigkeit = 20
Hans.Rasse = "Arravani"

#Methoden
class Pferd:
  def springen(self):
    self.springen
    
  def essen(self):
     self.essen
     
  def laufen(self):
    self.laufen
```

![image](https://user-images.githubusercontent.com/89509863/140812688-b3e5d820-24c7-4b88-b378-049b10f879e2.png)



### Projekt Beschreibung

Unser Programm sollte ein OnlineShop werden, für Kleidung. Es sollte eine Artikelliste geben mit den jeweiligen Prdukten. Es sollte möglich sein diese Sortieren nach Obergriffe oder spezifische Produkte zu suchen. Zusätzlich wollten wir einen Warenkorb implementieren, in dem man Produkte die man Bestellen möchte anzeigen lassen kann. Auch wird die gesamte Summe der Produkten Berechnet und die Summe anzeigen. Auch wollten wir ein anmeldesystem hinzufüge, damit kann sich der User einloggen und die Produkte bestellen.

Im Hintergrund nicht für den Kunden Sichtbar aber für einen Mitarbeiter, den Lagerbestand. Der Mitarbeiter kann eingeliefte Waren in den Lagerbestand aufnehmen und entfernen. Dies ermöglicht den einkäufer einen überblick zu erschaffen. Bei einem Einkauf sollten auch die Waren im Lager minimiert werden.


### Diagramme

![image](https://user-images.githubusercontent.com/89509863/140818165-b86323bc-b000-4d56-a057-87326df3759e.png)

![image](https://user-images.githubusercontent.com/89509863/141175385-06446604-8bfe-4834-bce2-0791d5fb209d.png)


### Unser Programm


### OO-Konzepte

***Delegation***

Delegation ist die weitergabe von Befehlen von höheren Klassen.

![image](https://user-images.githubusercontent.com/89509863/141179737-12ab1e2c-b69d-4105-ae5d-d9c0bc02d408.png)

In diesem Beispiel gibt man dem Haus das Befehl, dass alle blaue Türen geschlossen werden sollen. Dieses Haus, gibt dem Raum den Befehl alle blauen Türen schlissen.

***Encapsulation***

Man versteck die Variabeln von einer Klasse, somit können die anderen Kapseln nicht in die anderen Klassen einsehen.

***Exceptions***
Bei Ausnahmen ensteht eine Fehlermelung und diese stoppt das Programm. Die Exceptions verhindert dies und tut Ausnamehn ignorieren, damit das Programm weiter fahren kann.

***Static***

Auf statische Methoden kann zugegriffen werden, ohne dass ein Objekt erstellt werden muss.

***Final***

Die Variabeln bleiben konstant und können sich nicht verändern.

### Reflextion
Mit dem Ergebnis der Gruppenarbeit sind wir zufrieden. Wir haben beide viel Zeit in unser Programm gesteckt und unser Bestes gegeben(auch wenn unser Programm nur teilweise funktioniert). Leider haben wir weder in der Schule noch im Betrieb gross mit Python, Java oder C# gearbeitet, deshalb fällt es uns etwas schwer das ganze umzusetzen. 
Von dem Theorieteil konnten wir jedoch sehr viel mitnehmen. Wir haben gelernt was Objektorientierte Programmierung ist und wie man das ganze Planen kann anhand eines Klassendiagramms. Ausserdem wissen wir den Unterschied zwischen Klassen und Objekten. 
Bei unserem Programm sind wir viel mit der Hilfe von Herr Nussle vorangekommen. YouTube und Google waren auch noch eine Hilfe. Wir haben 7 verschieden Klassen eingebunden und versucht Produkte zu erstellen. Wir haben das Skript und auch andere Beispiele versucht zu analysieren, um alles nachvollziehen zu können.
Die aufgaben haben wir uns nicht aufgeteilt, sondern wir haben alles gemeinsam erarbeitet
 

