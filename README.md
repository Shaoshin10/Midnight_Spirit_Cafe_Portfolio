# Midnight Spirit Café

**Midnight Spirit Café** ist ein in Godot entwickelter Idle-Management-Prototyp. Spielende bauen ein kleines nächtliches Café auf, verwalten Zutaten und Rezepte, bedienen Gäste, organisieren Mitarbeitende und verbessern den Betrieb schrittweise.

> **Projektstatus:** Aktiv in Entwicklung  
> **Engine:** Godot 4.7  
> **Programmiersprache:** GDScript  
> **Genre:** Idle Game / Café Management

## Vorschau

### Café und Mitarbeitersystem

| Café-Hauptansicht | Mitarbeitersystem |
|---|---|
| <img src="docs/screenshots/cafe_uebersicht.jpg" alt="Hauptansicht des Cafés" width="450"> | <img src="docs/screenshots/mitarbeiter.jpg" alt="Übersicht der Mitarbeitenden" width="450"> |
| Gäste, Tische, Bestellungen und zentrale Caféverwaltung | Verwaltung des Teams und der Mitarbeitenden |

### Rekrutierung und Schichtplanung

| Mitarbeitende rekrutieren | Schichten planen |
|---|---|
| <img src="docs/screenshots/recruit_system.jpg" alt="Rekrutierung neuer Mitarbeitender" width="450"> | <img src="docs/screenshots/schichtplanung.jpg" alt="Planung der Arbeitsschichten" width="450"> |
| Auswahl und Rekrutierung neuer Teammitglieder | Einteilung der Mitarbeitenden in verschiedene Schichten |

### Rezepte und Upgrades

| Rezeptverwaltung | Café-Upgrades |
|---|---|
| <img src="docs/screenshots/rezepte.jpg" alt="Verwaltung der Rezepte" width="450"> | <img src="docs/screenshots/upgrades.jpg" alt="Übersicht der Café-Upgrades" width="450"> |
| Freischaltung und Verbesserung verschiedener Rezepte | Weiterentwicklung und Ausbau des Cafés |

### Warenlieferung

<p align="center">
  <img
    src="docs/screenshots/lieferung.jpg"
    alt="Verwaltung der Warenlieferung"
    width="700"
  >
</p>

<p align="center">
  Verwaltung eingehender Lieferungen und des verfügbaren Warenbestands.
</p>

## Spielidee

Das Spiel kombiniert automatische Idle-Abläufe mit aktiven Managemententscheidungen. Gäste betreten das Café, warten auf einen Platz, bestellen ein freigeschaltetes Produkt und werden abhängig von Zutatenbestand, Zubereitungszeit und Mitarbeitereinsatz bedient.

Der erzielte Umsatz fließt in neue Rezepte, bessere Ausstattung, zusätzliche Sitzplätze, Mitarbeitende und weitere Ausbauoptionen.

## Bereits umgesetzte Systeme

### Café und Gäste

- Warteschlange, Tresen, Sitzplätze und belegte Tische
- Automatisch erzeugte Gäste mit Wartezeit und Geduld
- Aufnahme, Vorbereitung und Auslieferung von Bestellungen
- Verhalten bei fehlenden Zutaten
- Einnahmen durch erfolgreich bediente Gäste
- Fortschritt über mehrere Café-Stufen

### Rezepte und Inventar

- Zutatenbestände mit begrenzter Lagerkapazität
- Getränke und Speisen mit individuellen Rezepten
- Freischaltung neuer Produkte über Café-, Maschinen- oder Ofenfortschritt
- Rezeptlevel, Verkaufspreise und Zubereitungszeiten
- Unterschiedliche Gewichtungen für die zufällige Produktauswahl
- Prüfung und Verbrauch benötigter Zutaten

### Mitarbeitende

- Rekrutierung mit Tickets oder Diamanten
- Mehrfachziehungen und Verarbeitung doppelter Charaktere
- Aktive Mitarbeiterslots
- Training, Sternstufen und individuelle Werte
- Zufriedenheit, Pausen und Gespräche
- Aktive und passive Fähigkeiten
- Rollen- und Aufgabenboni
- Einfluss auf Bedienzeit, Kundengeduld, Verkaufspreise und Offline-Ertrag

### Schichten und Öffnungszeiten

- Konfigurierbare Öffnungs- und Schließzeiten
- Mehrere Arbeitsschichten und zugeordnete Teams
- Drag-and-drop-Zuweisung von Mitarbeitenden
- Optionaler 24-Stunden-Betrieb
- Berücksichtigung von Schichten bei Offline-Zeiträumen

### Ausbau und Wirtschaft

- Kaffeemaschinen-Upgrades
- Zusätzliche Sitzplätze
- Verbesserter Produktwert
- Café-Stufen mit Voraussetzungen
- Freischaltbare Bäckerei
- Verbesserbarer Bäckerei-Ofen
- Zeitbasierte Warenlieferungen
- Begrenzte kostenlose Notfalllieferungen

### Speicherung und Idle-Fortschritt

- Lokaler Spielstand über Godots `user://`-Verzeichnis
- Speichern und Laden zentraler Spielsysteme
- Zeitstempel zur Berechnung vergangener Zeit
- Offline-Einnahmen mit einer Begrenzung auf maximal 24 Stunden
- Berücksichtigung aktiver Mitarbeitender und Schichten im Offline-Fortschritt

### Weitere Funktionen

- Deutsche und englische UI-Texte
- Debug-Werkzeuge zum Testen von Währungen, Zutaten, Rezepten und Spielständen
- Dynamisch erzeugte und aktualisierte UI-Komponenten
- Robuste Suche und Wiederherstellung wichtiger UI-Referenzen

## Technologie-Stack

| Bereich | Technologie |
|---|---|
| Game Engine | Godot 4.7 |
| Programmiersprache | GDScript |
| Rendering | GL Compatibility |
| Speicherung | Godot `FileAccess` / lokaler Spielstand |
| Benutzeroberfläche | Godot-Control-Nodes und dynamisch erzeugte UI |
| Architektur | Zentraler Spielkoordinator mit spezialisierten Managerklassen |

## Architektur

Die Spiellogik ist in mehrere fachlich getrennte Manager aufgeteilt. Dadurch können einzelne Systeme unabhängig weiterentwickelt und gespeichert werden.

| Komponente | Verantwortung |
|---|---|
| `CafeManager` | Café-Stufe, Fortschritt und Freischaltungen |
| `KundenManager` | Gäste, Warteschlange, Bestellungen und Bezahlung |
| `InventarManager` | Zutaten, Rezepte, Freischaltungen und Herstellung |
| `MitarbeiterSystem` | Mitarbeitende, Fähigkeiten, Zufriedenheit und Aufgaben |
| `SchichtManager` | Öffnungszeiten, Teams und Schichtzuweisungen |
| `RecruitManager` | Rekrutierung und Duplikatverarbeitung |
| `UpgradeManager` | Kaffeemaschine, Sitzplätze und Produktwert |
| `LieferungManager` | Lieferoptionen, Timer und Warenzugang |
| `BaeckereiManager` | Bäckereifreischaltung und Ofen-Upgrades |
| `SpeicherManager` | Lokales Speichern, Laden und Zeitstempel |
| `TexteManager` | Deutsche und englische UI-Texte |
| `DebugManager` | Entwicklungs- und Testaktionen |

## Projekt lokal starten

### Voraussetzungen

- Godot 4.7 oder eine kompatible Godot-4-Version
- Git für das Klonen des Repositorys

### Start

```bash
git clone <REPOSITORY-URL>
cd <REPOSITORY-ORDNER>
```

Anschließend:

1. `project.godot` im Godot Project Manager importieren.
2. Das Projekt mit Godot 4.7 öffnen.
3. Die Hauptszene `res://scenes/main/main.tscn` starten.

## Projektstruktur

```text
.
├── project.godot
├── scenes/
│   ├── main/
│   └── ui/
└── scripts/
    ├── ui/
    ├── main.gd
    ├── cafe_manager.gd
    ├── kunden_manager.gd
    ├── inventar_manager.gd
    ├── mitarbeiter_system.gd
    ├── schicht_manager.gd
    ├── recruit_manager.gd
    ├── upgrade_manager.gd
    └── weitere Manager
```

## Technische Herausforderungen

- Synchronisierung mehrerer voneinander abhängiger Spielsysteme
- Berechnung zeitbasierter Abläufe während und außerhalb der aktiven Spielsitzung
- Sichere Migration und Wiederherstellung gespeicherter Dictionaries
- Dynamische UI-Aktualisierung bei Änderungen an Inventar, Gästen und Mitarbeitenden
- Trennung von Spiellogik, UI-Darstellung und Speicherlogik
- Balancing von Preisen, Wartezeiten, Freischaltungen und Upgrades

## Aktueller Entwicklungsstand

Das Projekt ist ein spielbarer Prototyp und wird fortlaufend strukturell sowie spielmechanisch weiterentwickelt. Die Kernsysteme sind bereits miteinander verbunden; Grafik, Balancing, automatisierte Tests, Audio und finaler Spielfluss befinden sich noch in Arbeit.

## Geplante Weiterentwicklung

- Weitere Mitarbeitende mit individuellen Fähigkeiten und Dialogen
- Zusätzliche Rezepte, Zutaten und Café-Stufen
- Überarbeitung des visuellen Designs und eigene Art Assets
- Audio, Musik und Feedback-Effekte
- Tutorial und verständlicherer Einstieg
- Balancing-Werkzeuge und externe Konfigurationsdaten
- Automatisierte Tests für Berechnungs- und Speichersysteme
- Weitere Aufteilung des zentralen Spielkoordinators
- Export eines spielbaren Demo-Builds

## Motivation und Lernziele

Mit diesem Projekt entwickle ich ein vollständiges, systemorientiertes Spiel statt nur einzelner Mechaniken. Der Schwerpunkt liegt auf modularer Spiellogik, Zustandsverwaltung, persistenter Speicherung, dynamischen Benutzeroberflächen und dem Zusammenspiel vieler voneinander abhängiger Systeme.

## Lizenz

Dieses Projekt dient derzeit als persönliches Portfolio- und Lernprojekt. Eine Open-Source-Lizenz wurde noch nicht festgelegt.
