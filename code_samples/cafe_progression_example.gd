extends Node
class_name CafeProgressionPortfolioExample

## Generalisierter Portfolio-Auszug.
## Produktionswerte und projektspezifische Abhängigkeiten wurden entfernt.

signal level_changed(new_level: int)

var current_level: int = 1
var sold_products: int = 0


func register_sale(amount: int = 1) -> void:
	if amount <= 0:
		return

	sold_products += amount


func can_advance(
	requirements: Dictionary,
	machine_level: int,
	seat_level: int
) -> bool:
	if requirements.is_empty():
		return false

	return (
		sold_products >= int(requirements.get("required_sales", 0))
		and machine_level >= int(requirements.get("required_machine_level", 0))
		and seat_level >= int(requirements.get("required_seat_level", 0))
	)


func try_advance(
	requirements: Dictionary,
	machine_level: int,
	seat_level: int,
	max_level: int
) -> bool:
	if current_level >= max_level:
		return false

	if not can_advance(requirements, machine_level, seat_level):
		return false

	current_level += 1
	level_changed.emit(current_level)
	return true


func export_state() -> Dictionary:
	return {
		"current_level": current_level,
		"sold_products": sold_products,
	}


func import_state(data: Dictionary, max_level: int) -> void:
	current_level = clampi(
		int(data.get("current_level", 1)),
		1,
		max_level
	)
	sold_products = maxi(
		0,
		int(data.get("sold_products", 0))
	)
