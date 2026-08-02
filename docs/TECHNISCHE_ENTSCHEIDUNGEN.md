# Technische Entscheidungen

## Spezialisierte Manager statt einer einzigen Spielklasse

Der Prototyp enthält viele Systeme mit unterschiedlichen Regeln. Inventar, Gäste, Mitarbeitende, Schichten und Rekrutierung wurden deshalb in eigene Manager aufgeteilt.

**Vorteile**

- fachliche Regeln lassen sich leichter lokalisieren
- Zustände können getrennt gespeichert werden
- einzelne Systeme sind unabhängig erweiterbar
- Abhängigkeiten werden sichtbar

**Trade-off**

Die Verknüpfung der Manager wurde anfangs stark im zentralen Koordinator gebündelt. Dieser Koordinator wird aktuell weiter aufgeteilt.

## Dictionary-basierte Zustände

Für den Prototyp werden Systemzustände als Dictionaries gespeichert.

**Gründe**

- schnell erweiterbar
- gut mit Godots `store_var()` nutzbar
- geeignet für einen iterativen Prototyp
- Manager können eigene Datenpakete exportieren

**Absicherung**

- Typen beim Laden prüfen
- fehlende Schlüssel über Standardwerte behandeln
- numerische Werte begrenzen
- Arrays und Dictionaries an Grenzen kopieren
- ungültige oder fehlende Spielstände nicht als gültigen Zustand behandeln

## Begrenzter Offline-Fortschritt

Der Offline-Zeitraum wird begrenzt.

**Gründe**

- extreme Zeitsprünge vermeiden
- Balancing kontrollierbar halten
- Manipulation über Systemzeit weniger attraktiv machen
- Berechnungen nachvollziehbar halten

## Schichtberechnung über Minuten des Tages

Öffnungs- und Schichtzeiten werden als Minuten innerhalb eines Tages modelliert. Dadurch lassen sich auch Zeiträume behandeln, die über Mitternacht laufen.

Die Auswertung unterscheidet:

- normalen Zeitraum innerhalb eines Tages
- Zeitraum über Mitternacht
- 24-Stunden-Betrieb
- geschlossenen Betrieb ohne verfügbares Team

## Dynamische UI als Prototyping-Entscheidung

Ein Teil der Oberfläche wurde zunächst zur Laufzeit erzeugt. Das beschleunigte die frühe Entwicklung und machte neue Systeme schnell sichtbar.

Mit wachsendem Umfang entstanden jedoch Nachteile:

- Editor-Szene und Laufzeitansicht unterscheiden sich
- UI-Referenzen werden schwieriger nachvollziehbar
- Listen werden zu häufig neu aufgebaut
- der zentrale Koordinator übernimmt zu viele Darstellungsaufgaben

Daher wird die Oberfläche schrittweise auf stabilere Editor-Nodes, Seitencontroller und ereignisbasierte Aktualisierung umgestellt.

## Kleine Refactoring-Schritte

Größere Strukturänderungen werden nicht gleichzeitig durchgeführt. Nach jedem Schritt folgt ein Funktionscheck.

Diese Strategie reduziert das Risiko, dass Fehler aus Szenenstruktur, Datenfluss und UI-Aktualisierung gleichzeitig auftreten.
