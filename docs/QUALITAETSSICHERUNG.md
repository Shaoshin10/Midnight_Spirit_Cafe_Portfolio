# Qualitätssicherung

## Aktueller Ansatz

Der Prototyp befindet sich in aktiver Entwicklung. Die Qualitätssicherung besteht derzeit aus:

- statischer Prüfung von Szenen- und Ressourcenpfaden
- kontrollierten Refactoring-Schritten
- wiederholbaren manuellen Smoke-Tests
- Fehlerbehandlung beim Laden und Speichern
- Debug-Werkzeugen für Währungen, Inventar und Fortschritt
- Versionsverwaltung über Git

Automatisierte Gameplay-Tests sind geplant, aber noch nicht vollständig umgesetzt.

## Manueller Smoke-Test

Nach größeren Änderungen werden mindestens folgende Punkte geprüft:

| Prüfung | Erwartetes Ergebnis |
|---|---|
| Projektstart | keine Parser- oder Szenenfehler |
| Startseite | Café-Seite sichtbar |
| Navigation | alle Seiten erreichbar |
| HUD | TopBar und BottomBar bleiben sichtbar |
| Rekrutierung | Einzel- und Mehrfachrekrutierung funktionieren |
| Währungen | korrekte Kosten und Debug-Zugaben |
| Upgrades | Wirkung und Ressourcenabzug korrekt |
| Rezepte | Freischaltung und Darstellung korrekt |
| Lieferung | Timer, Wareneingang und Lagergrenzen korrekt |
| Schichten | Öffnungszeiten und Teamzuweisung korrekt |
| Café-Ablauf | Warteschlange, Bestellung und Bezahlung laufen |
| Speichern | Zustand wird geschrieben |
| Laden | Zustand wird nach Neustart wiederhergestellt |
| Offline-Zeit | Zeitraum wird begrenzt und plausibel ausgewertet |

## Schutz des öffentlichen Repositorys

Dieses Portfolio-Repository ist absichtlich nicht ausführbar. Ein Python-Prüfskript kontrolliert, dass keine typischen privaten Projektbestandteile eingecheckt wurden.

Geprüft werden unter anderem:

- `project.godot`
- Godot-Szenen und Ressourcen
- Produktionsordner wie `scripts/`, `scenes/` und `data/`
- GDScript-Dateien außerhalb des ausdrücklich freigegebenen Beispielordners
- Godot-Cache und temporäre Dateien

Der Check läuft auch als GitHub-Actions-Workflow bei Pushes und Pull Requests.

Lokal:

```bash
python tools/verify_public_repo.py
```

## Geplante Erweiterungen

- Unit-Tests für reine Berechnungsfunktionen
- Tests für Speichern und defensive Deserialisierung
- Tests für Zeiträume über Mitternacht
- deterministische Tests der Rekrutierungsverarbeitung
- klarere Trennung zwischen Simulation und Darstellung
