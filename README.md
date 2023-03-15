# WonderDoktorandin 

Dieses Spiel entstand im Rahmen des Kurses "getcupcake" der MeccanicaFeminale 2023 und wurde im Nachgang noch vervollständigt.

Das kleine Spiel "WonderDoktorandin" von Diana Barth kann über eine Instanz der DOS-Konsole "cmd" gestartet werden.
geben sie hierzu in der Konsole "cd " und den Pfad zum Oberordner ein. Geben
Geben sie anschließen in der Konsole "python main.py" ein.

Bevor Sie weiterlesen, einfach mal ausprobieren!

Der Code ist wie folgt in mehrere Dateien organisiert:

* main: Hauptinstanz mit der Klasse Spiel sowie dem Aufruf von Spiel.spiele() um das Spiel zu starten.
* WonderWoerter: Hier findet die Definition und Erkennung aller Wörter statt, also der Usereingaben. 
  * Die Wörter sind dabei so strukturiert, dass verschiedene Eingaben zum selben Wort erkannt werden und zu unterschiedlichen Ausgaben führen, damit das Spiel nicht zu eintönig wird.
  * Die Wörter sind in verschiedene WortTypen kategorisiert:  
       die Bewegungstypen sind dabei Flaeche, Ebene, Uebergang, außerdem gibt es noch Inventar,Blumenpflege und SpielBeenden = 6
* WonderPosition: enthält die Grundklasse Position, die für Bewegungstypen relevant ist. Es wird eine dreidimensionale Welt mit x.y.z-Koordinate aufgespannt
* WonderUmgebung: enthält die Klasse Umgebung und die Intanziierung dieser Klasse. Die Welt besteht aus Wiese,Wasser,Wald und Universität in dieser Reihenfolge, wobei jede Umgebung quadratisch aufgebaut ist und an allen Grenzen des Rechtecks die jeweils nächste Umgebung beginnt.
* WonderBewegung: wenn ein Wort eines Bewegungstyps erkannt wird, so beginnt diese Klasse, die Bewegung in der jeweiligen Umgebung auszuführen. An den Grenzen einer Umgebung finden mehrere Bewegungsschritte automatisch statt, sofern das passende Uebergangs-Wort eingegeben wurde.
* WonderBlumen: In jeder Umgebung werden zufällig Blumen gespawnt mit einem zufälligen Aussehen. Blumen können gegossen werden und gepflückt werden.
* WonderInventar:In der Klasse Inventar werden die eingesammelten Blumen verwaltet und gezählt, wie viele hiervon die Größe "rießig" erreicht haben (denn wenn 3 rießige Blumen erreicht sind, wird von main aus aufgefordert, die Doktormutter zu suchen und ihr die Blumen zu bringen. hierdurch wird das Spiel beendet.)
