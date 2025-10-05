from move_to import move_to

# Test point sets
SMALL_POINTS = {(1, 2), (3, 4), (7, 1), (2, 8), (9, 5)}
MEDIUM_POINTS = {
	(1,3),(1,4),(1,1),(3,0),(3,1),(4,2),(4,3),(4,7),(5,2),(6,0),
	(6,6),(7,6),(7,1),(8,8),(8,2),(9,4),(9,0),(9,1),(9,3),(0,3),
}
LARGE_POINTS = {
	(2,6),(2,9),(2,0),(2,2),(2,4),(2,5),(3,6),(3,7),(3,1),(3,3),
	(3,4),(4,4),(4,6),(4,8),(4,9),(4,2),(5,3),(5,4),(5,5),(5,6),
	(5,7),(5,8),(5,9),(5,0),(5,2),(6,4),(6,6),(6,7),(6,8),(6,9),
	(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,8),(7,9),(8,1),(8,2),
	(8,4),(8,8),(8,9),(9,9),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),
	(0,8),(0,9),(0,3),(0,5),(0,6),(0,7),(1,9),(1,1),(1,2),(1,3),
}

test_sets = [
	("Small (5 points)", SMALL_POINTS),
	("Medium (20 points)", MEDIUM_POINTS),
	("Large (60 points)", LARGE_POINTS)
]

# Baseline function - no pathfinding optimization
def no_pathfinding(points, start_pos=None):
	return points

# Import algorithms
import nearest_neighbor
import greedy_insertion
import farthest_insertion
import two_opt
import christofides_approx

algorithms = [
	(no_pathfinding, "no_pathfinding (baseline)"),
	(nearest_neighbor.nearest_neighbor, "nearest_neighbor"),
	(greedy_insertion.greedy_insertion, "greedy_insertion"),
	(farthest_insertion.farthest_insertion, "farthest_insertion"),
	(two_opt.two_opt, "two_opt"),
	(christofides_approx.christofides_approx, "christofides_approx")
]

quick_print("=== Pathfinding Algorithm Benchmark ===")
quick_print("")

for test_name, points in test_sets:
	quick_print(test_name)
	quick_print("------------------------------------------------")

	for algorithm, name in algorithms:
		# Reset position and points
		clear()
		start_pos = (get_pos_x(), get_pos_y())
		test_points = set(points)
		# Test path generation
		path_start = get_tick_count()
		path = algorithm(test_points, start_pos)
		path_ticks = get_tick_count() - path_start

		# Test movement execution
		move_start = get_tick_count()
		for x,y in path:
			move_to(x, y)
		move_ticks = get_tick_count() - move_start

		total_ticks = path_ticks + move_ticks

		quick_print(name,
				   "| Gen:", path_ticks,
				   "| Move:", move_ticks,
				   "| Total:", total_ticks)

	quick_print("")

quick_print("=== Benchmark Complete ===")
