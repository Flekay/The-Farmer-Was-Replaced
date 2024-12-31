move(North)
FULL_MOVES = generate_moves_light()
SMALL_MOVES = generate_small_moves()
move_data_x, move_data_y = loadDataList(get_world_size())
power = [[],[],[],[],[],[],[],[],[]]
index = {15: 0, 14: 1, 13: 2, 12: 3, 11: 4, 10: 5, 9: 6, 8: 7, 7: 8}
part1()
part2(5, 0.35, 0.25, 4)
part2(8, 0.35, 0.25, 5)
part2(10, 0.35, 0.25, 6)
