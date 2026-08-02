# Midnight Spirit Café — Portfolio Summary

**Midnight Spirit Café** is a playable idle-management prototype developed with Godot 4.7 and GDScript.

Players operate a small night café and manage:

- customers, queues, orders and seating
- ingredients, recipes and deliveries
- employees, skills, satisfaction and shifts
- recruitment, upgrades and progression
- local save data and capped offline progress

<p align="center">
  <img src="docs/screenshots/cafe_uebersicht.jpg" alt="Midnight Spirit Café main prototype view" width="100%">
</p>

## My contribution

I am responsible for the concept, software architecture, GDScript implementation, UI prototyping, debugging and technical documentation.

The prototype focuses on the interaction of multiple stateful and time-based systems rather than on final visual assets.

## Technical approach

The application is coordinated by a central gameplay controller and several specialised managers for customers, inventory, employees, shifts, recruitment, upgrades, deliveries and persistence.

Key engineering topics include:

- defensive state loading and local persistence
- time-based and offline calculations
- cross-system dependencies
- dynamic UI synchronisation
- iterative refactoring of a growing prototype

The current refactoring roadmap separates page presentation from gameplay logic and replaces broad per-frame UI rebuilds with more targeted updates.

## Public repository scope

This repository is intentionally documentation-only. It does **not** contain the runnable Godot project, production scenes, core managers, save implementation, balancing data or internal debug tools.

A small generalised GDScript sample is available in [code_samples/cafe_progression_example.gd](code_samples/cafe_progression_example.gd).

A guided walkthrough of the private source code can be offered during a hiring process.

## Author

**Justin Plath**

For further details, see the [German project documentation](README.md).

## Rights

No open-source licence is granted. See [NOTICE.md](NOTICE.md).
