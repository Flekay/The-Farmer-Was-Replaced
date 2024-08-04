def time_series(list, width=60, height=10):
    # Find min and max values
    min_val = min(list)
    max_val = max(list)
    range_val = max_val - min_val

    # Create normalized points
    normalized = []
    for value in list:
        if range_val != 0:
            normalized.append((value - min_val) / range_val * (height - 1))
        else:
            normalized.append(0)

    # Print the chart
    for y in range(height - 1, -1, -1):
        line = ''
        for x in range(len(list)):
            if y == 0:
                line += '-'
            elif x < width and normalized[x] >= y:
                line += '*'
            else:
                line += ' '
        quick_print(line)

    # Print x-axis labels
    min_index = 0
    max_index = len(list) - 1
    min_time = list[min_index]
    max_time = list[max_index]
    min_label = "0:" + str(min_time)
    max_label = str(max_index) + ":" + str(max_time)
    spacing = width - len(min_label) - len(max_label) - 2
    whitespace = ''
    for i in range(spacing):
        whitespace += ' '
    quick_print(min_label + whitespace + max_label)

    # Print min and max information
    min_index = list.index(min_val)
    max_index = list.index(max_val)
    quick_print("Min: index=" + str(min_index) + ", time=" + str(min_val))
    quick_print("Max: index=" + str(max_index) + ", time=" + str(max_val))

# Example usage
example_list = [10.28,9.31,8.28,7.31,6.21,6.33,5.33,5.21,4.29,4.26,4.23,4.17,3.26,3.27,3.32,3.25]
time_series(example_list)
