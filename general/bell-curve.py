def bell_curve(list, width=60, height=10):
    # Create histogram
    histogram = []
    for i in range(width):
        histogram.append(0)
    min_val, max_val = min(list), max(list)
    range_val = max_val - min_val
    for value in list:
        bucket = ((value - min_val) / range_val * (width - 1))//1
        histogram[bucket] += 1

    # Normalize histogram
    max_count = max(histogram)
    normalized = []
    for i in range(width):
        normalized.append(0)
    for i in range(width):
        normalized[i] = histogram[i] / max_count * height

    # Print the chart
    for y in range(height - 1, -1, -1):
        line = ''
        for x in range(width):
            if normalized[x] >= y:
                line += '*'
            else:
                line += ' '
        quick_print(line)

    # Print x-axis labels
    min_label = str(min_val)
    max_label = str(max_val)
    spacing = width - len(min_label) - len(max_label) - 2
    whitespace = ''
    for i in range(spacing):
        whitespace += ' '
    quick_print(min_label, whitespace, max_label)
