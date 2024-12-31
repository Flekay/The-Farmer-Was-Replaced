import statistics
import os

def process_file(file_path):
    data = {}

    # Read the file and process each line
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            key = int(parts[0])
            value = float(parts[1])

            if key not in data:
                data[key] = []
            data[key].append(value)

    # Calculate average and median for each key
    for key, values in data.items():
        average = sum(values) / len(values)
        median = statistics.median(values)
        print(f"Key: {key}, Average: {average:.2f}, Median: {median:.2f}")

process_file( os.path.join(os.path.dirname(__file__), 'output.txt') )


# Key: 20, Average: 28.57, Median: 28.40
# Key: 21, Average: 28.40, Median: 28.50
# Key: 22, Average: 28.38, Median: 28.18
# Key: 30, Average: 26.88, Median: 26.88
# Key: 31, Average: 26.96, Median: 27.00
# Key: 32, Average: 26.68, Median: 26.61
# Key: 33, Average: 26.73, Median: 26.78
# Key: 34, Average: 26.12, Median: 26.12
# Key: 35, Average: 26.46, Median: 26.52
# Key: 36, Average: 26.13, Median: 26.28
# Key: 37, Average: 26.03, Median: 25.95
# Key: 38, Average: 26.11, Median: 26.09
# Key: 39, Average: 25.82, Median: 25.70
# Key: 40, Average: 25.70, Median: 25.73
# Key: 41, Average: 25.54, Median: 25.48
# Key: 42, Average: 25.30, Median: 25.12
# Key: 43, Average: 25.27, Median: 25.36
# Key: 44, Average: 25.27, Median: 25.24
# Key: 46, Average: 25.06, Median: 25.04
# Key: 47, Average: 25.19, Median: 25.34
# Key: 48, Average: 25.05, Median: 25.25
# Key: 56, Average: 24.64, Median: 24.70
# Key: 57, Average: 24.65, Median: 24.64
# Key: 65, Average: 25.02, Median: 25.10
# Key: 67, Average: 25.44, Median: 25.33
# Key: 68, Average: 25.58, Median: 25.68
# Key: 69, Average: 25.67, Median: 25.58
# Key: 70, Average: 26.31, Median: 26.48
# Key: 71, Average: 26.07, Median: 26.02
# Key: 72, Average: 26.62, Median: 26.47
# Key: 73, Average: 26.73, Median: 26.61
# Key: 74, Average: 27.44, Median: 27.37
# Key: 75, Average: 27.43, Median: 27.48
# Key: 76, Average: 27.87, Median: 28.02
# Key: 77, Average: 28.03, Median: 27.93



# Key: 10, Average: 31.84, Median: 31.55
# Key: 11, Average: 31.71, Median: 31.95
# Key: 12, Average: 31.49, Median: 31.29
# Key: 13, Average: 30.38, Median: 29.94
# Key: 14, Average: 29.90, Median: 30.32
# Key: 15, Average: 29.44, Median: 29.68
# Key: 16, Average: 29.95, Median: 29.77
# Key: 17, Average: 28.86, Median: 29.51
# Key: 18, Average: 28.23, Median: 28.33
# Key: 19, Average: 28.46, Median: 28.93
# Key: 20, Average: 27.15, Median: 26.99
# Key: 21, Average: 27.40, Median: 27.27
# Key: 22, Average: 27.62, Median: 27.29
# Key: 23, Average: 25.59, Median: 25.98
# Key: 24, Average: 26.86, Median: 26.84
# Key: 25, Average: 26.28, Median: 26.49
# Key: 26, Average: 25.21, Median: 24.54
# Key: 27, Average: 25.06, Median: 25.09
# Key: 28, Average: 26.09, Median: 25.74
# Key: 29, Average: 25.30, Median: 25.21
# Key: 30, Average: 24.70, Median: 24.36
# Key: 31, Average: 25.41, Median: 25.21
# Key: 32, Average: 25.00, Median: 24.80
# Key: 33, Average: 23.84, Median: 23.94
# Key: 34, Average: 24.75, Median: 24.67
# Key: 35, Average: 23.61, Median: 23.62
# Key: 36, Average: 23.96, Median: 24.55
# Key: 37, Average: 24.68, Median: 24.62
# Key: 38, Average: 25.05, Median: 25.35
# Key: 39, Average: 24.55, Median: 24.50
# Key: 40, Average: 24.85, Median: 25.42
# Key: 41, Average: 24.28, Median: 24.48
# Key: 42, Average: 24.15, Median: 24.59
# Key: 43, Average: 24.02, Median: 23.94
# Key: 44, Average: 23.48, Median: 23.40
# Key: 45, Average: 23.61, Median: 24.13
# Key: 46, Average: 24.59, Median: 24.95
# Key: 47, Average: 24.38, Median: 24.45
# Key: 48, Average: 25.06, Median: 25.15
# Key: 49, Average: 24.58, Median: 24.27
# Key: 50, Average: 25.37, Median: 25.55
# Key: 51, Average: 24.42, Median: 24.27
# Key: 52, Average: 25.17, Median: 25.12
# Key: 53, Average: 25.07, Median: 24.95
# Key: 54, Average: 25.06, Median: 25.31
# Key: 55, Average: 24.19, Median: 23.94
# Key: 56, Average: 25.48, Median: 25.66
# Key: 57, Average: 25.94, Median: 25.59
# Key: 58, Average: 24.63, Median: 24.55
# Key: 59, Average: 25.17, Median: 25.55
# Key: 60, Average: 25.95, Median: 25.64
# Key: 61, Average: 25.45, Median: 25.71
# Key: 62, Average: 25.97, Median: 25.45
# Key: 63, Average: 25.39, Median: 25.02
# Key: 64, Average: 26.31, Median: 25.34
# Key: 65, Average: 26.46, Median: 26.21
# Key: 66, Average: 27.67, Median: 27.80
# Key: 67, Average: 26.47, Median: 25.48
# Key: 68, Average: 27.11, Median: 26.80
# Key: 69, Average: 26.33, Median: 26.04
# Key: 70, Average: 27.08, Median: 26.64
# Key: 71, Average: 26.41, Median: 26.39
# Key: 72, Average: 26.68, Median: 26.39
# Key: 73, Average: 27.19, Median: 26.70
# Key: 74, Average: 27.40, Median: 27.23
# Key: 75, Average: 27.60, Median: 27.25
# Key: 76, Average: 27.52, Median: 27.58
# Key: 77, Average: 27.78, Median: 27.84
# Key: 78, Average: 28.09, Median: 28.54
# Key: 79, Average: 27.85, Median: 27.93
# Key: 80, Average: 28.56, Median: 28.90
# Key: 81, Average: 28.07, Median: 28.07
# Key: 82, Average: 28.05, Median: 27.96


# Key: 20, Average: 27.85, Median: 28.36
# Key: 21, Average: 27.26, Median: 27.11
# Key: 22, Average: 26.49, Median: 26.05
# Key: 23, Average: 27.52, Median: 27.14
# Key: 24, Average: 26.01, Median: 26.37
# Key: 25, Average: 25.28, Median: 24.93
# Key: 26, Average: 25.74, Median: 26.11
# Key: 27, Average: 25.38, Median: 25.20
# Key: 28, Average: 24.82, Median: 24.84
# Key: 29, Average: 25.27, Median: 25.45
# Key: 30, Average: 24.43, Median: 24.66
# Key: 31, Average: 25.04, Median: 25.06
# Key: 32, Average: 24.74, Median: 24.66
# Key: 33, Average: 24.40, Median: 24.55
# Key: 34, Average: 25.00, Median: 25.07
# Key: 35, Average: 24.60, Median: 24.90
# Key: 36, Average: 24.42, Median: 24.30
# Key: 37, Average: 24.58, Median: 24.26
# Key: 38, Average: 24.12, Median: 24.20
# Key: 39, Average: 24.25, Median: 24.55
# Key: 40, Average: 23.94, Median: 23.78
# Key: 41, Average: 24.14, Median: 24.25
# Key: 42, Average: 24.25, Median: 24.11
# Key: 43, Average: 24.16, Median: 23.96
# Key: 44, Average: 23.97, Median: 23.86
# Key: 47, Average: 23.79, Median: 23.84
# Key: 48, Average: 23.93, Median: 23.59
# Key: 49, Average: 24.35, Median: 24.30
# Key: 50, Average: 24.38, Median: 24.22
# Key: 51, Average: 24.78, Median: 24.74
# Key: 52, Average: 24.86, Median: 24.59
# Key: 53, Average: 25.17, Median: 24.92
# Key: 54, Average: 24.75, Median: 25.09
# Key: 55, Average: 24.85, Median: 25.31
# Key: 56, Average: 25.30, Median: 25.24
# Key: 57, Average: 25.22, Median: 25.64
# Key: 58, Average: 25.83, Median: 25.96
# Key: 59, Average: 24.94, Median: 24.75
# Key: 60, Average: 26.26, Median: 26.75
# Key: 61, Average: 25.67, Median: 25.28
# Key: 62, Average: 26.15, Median: 26.29
# Key: 63, Average: 25.97, Median: 25.74
# Key: 64, Average: 25.84, Median: 25.73
# Key: 65, Average: 26.56, Median: 26.94
# Key: 66, Average: 25.80, Median: 25.91
# Key: 67, Average: 26.77, Median: 26.89
# Key: 68, Average: 27.13, Median: 27.31
# Key: 69, Average: 27.01, Median: 27.20
# Key: 70, Average: 26.86, Median: 26.47
# Key: 71, Average: 27.21, Median: 27.55
# Key: 72, Average: 25.38, Median: 25.38



# Key: 40, Average: 24.02, Median: 23.95
# Key: 41, Average: 24.10, Median: 24.04
# Key: 42, Average: 24.51, Median: 24.64
# Key: 43, Average: 24.10, Median: 24.06
# Key: 44, Average: 24.29, Median: 24.23
# Key: 45, Average: 24.34, Median: 24.38
# Key: 46, Average: 24.28, Median: 24.18
# Key: 47, Average: 24.29, Median: 24.14
# Key: 48, Average: 24.47, Median: 24.44
# Key: 49, Average: 24.74, Median: 24.75
# Key: 35, Average: 24.23, Median: 24.11
# Key: 36, Average: 24.09, Median: 24.10
# Key: 37, Average: 24.02, Median: 24.09
# Key: 38, Average: 23.88, Median: 24.11
# Key: 39, Average: 24.08, Median: 23.98



# Key: 1, Average: 40.72, Median: 40.19
# Key: 2, Average: 40.09, Median: 39.25
# Key: 3, Average: 39.70, Median: 39.45
# Key: 4, Average: 37.63, Median: 37.92
# Key: 5, Average: 36.32, Median: 36.23
# Key: 6, Average: 35.78, Median: 35.78
# Key: 7, Average: 37.17, Median: 37.33
# Key: 8, Average: 35.65, Median: 35.57
# Key: 9, Average: 34.09, Median: 34.19
# Key: 10, Average: 34.00, Median: 33.89
# Key: 11, Average: 32.91, Median: 33.29
# Key: 12, Average: 31.22, Median: 30.96
# Key: 13, Average: 32.95, Median: 32.62
# Key: 14, Average: 32.84, Median: 32.36
# Key: 15, Average: 31.40, Median: 31.34
# Key: 16, Average: 31.00, Median: 30.41
# Key: 17, Average: 29.87, Median: 30.13
# Key: 18, Average: 30.18, Median: 29.86
# Key: 19, Average: 31.28, Median: 31.25
# Key: 20, Average: 31.87, Median: 32.61
# Key: 21, Average: 29.23, Median: 29.81
# Key: 22, Average: 30.49, Median: 30.20
# Key: 23, Average: 29.43, Median: 30.63
# Key: 24, Average: 28.31, Median: 28.45
# Key: 25, Average: 30.76, Median: 30.80
# Key: 26, Average: 29.96, Median: 30.05
# Key: 27, Average: 29.43, Median: 29.16
# Key: 28, Average: 28.15, Median: 28.51
# Key: 29, Average: 28.49, Median: 29.05
# Key: 30, Average: 29.52, Median: 29.30
# Key: 31, Average: 30.34, Median: 30.23
# Key: 32, Average: 28.89, Median: 29.16
# Key: 33, Average: 28.42, Median: 28.26
# Key: 34, Average: 27.85, Median: 27.92
# Key: 35, Average: 29.15, Median: 28.46
# Key: 36, Average: 28.34, Median: 27.90
# Key: 37, Average: 29.84, Median: 29.34
# Key: 38, Average: 29.14, Median: 27.92
# Key: 39, Average: 28.65, Median: 29.21
# Key: 40, Average: 28.71, Median: 28.39
# Key: 41, Average: 29.96, Median: 29.36
# Key: 42, Average: 30.25, Median: 30.84
# Key: 43, Average: 31.21, Median: 31.48
# Key: 44, Average: 27.80, Median: 27.35
# Key: 45, Average: 30.10, Median: 30.19
# Key: 46, Average: 29.27, Median: 29.85
# Key: 47, Average: 30.75, Median: 31.49
# Key: 48, Average: 30.92, Median: 31.29
# Key: 49, Average: 29.18, Median: 29.12
# Key: 50, Average: 30.25, Median: 31.27
# Key: 51, Average: 31.38, Median: 30.58
# Key: 52, Average: 30.77, Median: 30.88
# Key: 53, Average: 30.08, Median: 29.84
# Key: 54, Average: 32.21, Median: 31.86
# Key: 55, Average: 32.61, Median: 32.34
# Key: 56, Average: 31.31, Median: 31.52
# Key: 57, Average: 31.18, Median: 30.64
# Key: 58, Average: 31.50, Median: 31.55
# Key: 59, Average: 31.06, Median: 30.69
# Key: 60, Average: 32.33, Median: 31.67
# Key: 61, Average: 32.10, Median: 31.68
# Key: 62, Average: 32.38, Median: 32.25
# Key: 63, Average: 32.07, Median: 32.34
# Key: 64, Average: 33.48, Median: 33.23
# Key: 65, Average: 33.27, Median: 32.55
# Key: 66, Average: 34.31, Median: 35.86
