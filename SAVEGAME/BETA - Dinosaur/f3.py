def default_path_distance(pos1_idx, pos2_idx, total_positions=100):
	return (pos2_idx - pos1_idx) % total_positions