# Roadmap und Refactoring

## Erledigter Bereinigungsschritt

Der Projektstand wurde vor dem nächsten größeren Feature-Umbau technisch bereinigt:

- Projektname vereinheitlicht
- Godot-Cache aus dem Versionsstand entfernt
- temporäre Szenendateien entfernt
- alte Backup-Szene aus dem aktiven Projekt ausgelagert
- `.gitignore` erweitert
- bestehender Stand anschließend manuell getestet

## Nächste strukturelle Schritte

### Phase 2 – Eindeutige Szenenstruktur

- doppelte Node-Namen beseitigen
- alten leeren Seitencontainer entfernen
- Overlay-Hintergrund vereinheitlichen
- feste Node-Pfade statt rekursiver Fallback-Suche verwenden

### Phase 3 – Zentralen Koordinator aufteilen

- Navigation von Spiellogik trennen
- seitenspezifische UI-Funktionen auslagern
- Node-Referenzen bündeln
- tote und doppelte Pfade entfernen

### Phase 4 – UI-Aktualisierung optimieren

- nur sichtbare oder geänderte Bereiche aktualisieren
- Dirty-Flags und Signale einsetzen
- Listen nicht pro Frame vollständig neu erzeugen
- UI-Elemente wiederverwenden

### Phase 5 – Zusammenhängende Café-Ansicht

Die aktuelle Drei-Spalten-Ansicht ist ein funktionaler Prototyp. Das geplante räumliche Layout umfasst:

- Kasse und Theke als Zentrum
- Warteschlange direkt an der Kasse
- Küche und Ofen hinter oder neben der Theke
- frei im Raum angeordnete Tische
- sichtbare Bewegungs- und Zustandspositionen der Gäste

Die Simulation bleibt dabei von der Darstellung getrennt. Ein Gastzustand bestimmt, an welchem visuellen Ankerpunkt sich die Darstellung befindet.

## Weitere Produktentwicklung

- eigene visuelle Assets
- Audio und Feedback-Effekte
- Tutorial und besserer Einstieg
- zusätzliche Rezepte und Mitarbeitende
- Balancing-Werkzeuge
- automatisierte Tests
- spielbarer Demo-Build
