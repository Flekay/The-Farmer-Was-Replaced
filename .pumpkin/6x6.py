MOVES = (
	North, North, North, North, North, East,
	South, South, South, South, East,
	North, North, North, North, East,
	South, South, South, South, East,
	North, North, North, North, East,
	South, South, South, South, South,
	West,  West,  West,  West,  West,
)

for direction in MOVES:
	till()
	use_item(Items.Water)
	move(direction)
