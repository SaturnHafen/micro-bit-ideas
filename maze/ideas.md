# Ideen zum herangehen:

## Anzeigen des Irrgartens:
 - Welche Datenstruktur(en) ist/sind zum Speichern des Irrgartens sinnvoll?
   - Am Besten geeignet sind Datenstrukturen, in denen wir mehr als nur einen Datensatz speichern können (wir wollen ja für jede Zelle ihren zugehörigen Zustand, also ob es zB eine Wand oder das Ziel ist, speichern). Geeignet sind hierfür zum Beispiel Listen oder Zeichenketten. Da wir auch noch 2 Dimensionen haben, können wir uns überlegen, ob wir eine 2 dimensionale Liste (eine Liste, deren Elemente auch Listen sind) verwenden, oder später ein wenig Positionen umrechnen müssen.
   
 - Wie merken wir uns die Spielerposition (entspricht dem Mittelpunkt des sichtbaren Bereichs)?
   - Hierfür können wir uns einfach zwei Variablen nehmen, oder wir speichern sie auch in einer Liste

 - Wie können wir nur einen Teil des Irrgartens anzeigen (5 * 5)?
   - Hierfür müssen wir die richtigen 25 Symbole aus unserer Liste von oben holen. Da diese Abfragen prinzipiell alle sehr ähnlich zueinander sind, können wir hierfür eine Schleife verwenden.

 - Wie stellt man die verschiedenen Elemente des Irrgartens (Spieler, Weg, Wand, ...) dar?
   - Da wir leider nur eine Farbe pro Pixel haben, bleibt uns nichts anderes übrig, als mithilfe der Helligkeit unterschiedliche Bedeutungen zu vermitteln (zB Spieler = hell, Weg = aus, Wand = leicht leuchtend, usw.)

## Richtung
  - Wie können wir bestimmen in welche Richtung der Spieler sich bewegen soll?
    - Der Micro:Bit hat einen Kompass eingebaut, den wir dafür zB verwenden könnten (wir können aber auch Mithilfe der beiden Knöpfe navigieren (zB A = nach links, B = nach rechts))
    
  - Wann soll der Spieler sich bewegen?
    - Zeitbasiert (zB alle 1 sek), wenn ihr den Micro:Bit schüttelt, bei einem Knopfdruck, oder andere verrückte Möglichkeiten
  
  - Wann gewinnt man?
    - Es könnte eine Zielzone geben, oder es geht darum, eine bestimmte Schrittzahl zu schaffen, oder man muss alle versteckten Kisten finden, ...
    
  - Wie verhindern wir, das der Spieler durch Wände laufen kann?
    - Wir haben ja eine Liste mit allen Wänden (haben wir uns ganz am Anfang überlegt). Jetzt können wir vor jedem Schritt prüfen, ob wir gerade auf eine Wand laufen, und falls ja, den Zug abbrechen (also stehenbleiben)

## weiterführendes
  - Gegner?
    - Es könnten Gegner im Irrgarten versteckt sein, die man bekämpfen / umgehen / ... muss (zB wie bei Pacman)
    
  - Schatzkisten?
    - Eine Bedingung, das Level zu beenden, könnte sein, alle Schatzkisten zu finden.
    
  - Dynamische Irrgartengenerierung?
    - zB aus vorgefertigten Teilen oder mehrere Level, die man erkunden kann, ...

  -  ...
