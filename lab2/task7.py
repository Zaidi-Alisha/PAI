temperatures = [12, 23, 21, 23, 18, 24, 22, 20, 16, 12, 19,29, 21, 23, 25, 28, 16, 14]

def calculate_average(temperatures):
    return sum(temperatures) / len(temperatures)

def find_extremes(temperatures):
    return max(temperatures), min(temperatures)

def sort_temperatures(temperatures):
    return sorted(temperatures)

def remove_temperature(temperatures, day):
    del temperatures[day - 1]
    return temperatures


average_temperature = calculate_average(temperatures)
print("Average temperature: ", average_temperature)

# Find and print the highest and lowest temperatures
highest, lowest = find_extremes(temperatures)
print("Highest temperature:", highest)
print("Lowest temperature: ", lowest)

# Sort the temperatures in ascending order
sorted_temperatures = sort_temperatures(temperatures)
print("Sorted temperatures:", sorted_temperatures)

# Remove the temperature record for a specific day (e.g. day 10)
temperatures = remove_temperature(temperatures, 2)
print("Temperatures after removing day 2:", temperatures)
