
# AU values for each set
AU_values = {
    1: 1.00,
    2: 1.39,
    3: 1.61,
    4: 1.77,
    5: 1.90,
    6: 2.00,
    7: 2.09,
    8: 2.16,
    9: 2.23
}

# Function to calculate the total AU for the given number of sets
def calculate_total_AU(sets):
    return AU_values[sets]  # Return AU value only for the number of sets

# Weekly net stimulus calculation remains the same
def calculate_weekly_net_stimulus(sets, frequency):
    total_AU = calculate_total_AU(sets)
    weekly_net_stimulus = total_AU * frequency
    return weekly_net_stimulus


# Get user inputs (converted to integers)
sets_per_exercise = int(input('Enter the number of sets per exercise: '))
frequency_per_week = int(input('Enter the number of workout sessions per week: '))

# Calculate and print the weekly net stimulus
weekly_stimulus = calculate_weekly_net_stimulus(sets_per_exercise, frequency_per_week)
print(f'Your weekly net stimulus is: {weekly_stimulus:.2f} AU')


