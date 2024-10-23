import streamlit as st

# Title and Introduction
st.title('Weekly Net Stimulus and Muscle Growth Calculator with Recovery Times')
st.write("""
This app calculates your weekly net stimulus for resistance training based on the number of sets per exercise and workout frequency.
It also checks if the volume of sets and frequency is too high for proper recovery.
""")

# Inputs
sets_per_exercise = st.number_input('Enter the number of sets per exercise', min_value=1, max_value=12, value=3)
frequency_per_week = st.number_input('Enter the number of workout sessions per week', min_value=1, value=3)

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
    9: 2.23,
    10: 2.31,
    11: 2.38,
    12: 2.46
}

recovery_times = {
    1: 1,
    2: 1,  # Less than 2 days
    3: 2,
    4: 3,  # More than 2 days
    5: 3,
    6: 4,  # More than 3 days
    7: 4,
    8: 5,  # More than 4 days
    9: 5,
    10: 6,  # For 8-10 sets, recovery is more than 4 days
    11: 6,
    12: 7
}

# Function to calculate total AU for the given number of sets
def calculate_total_AU(sets):
    return AU_values[sets]  # Return AU value for the specific number of sets

# Function to calculate hypertrophy stimulus accounting for recovery times
def calculate_hypertrophy_with_recovery(sets, frequency):
    total_AU = calculate_total_AU(sets)
    weekly_stimulus = 0
    recovery_days = recovery_times.get(sets, 2)  # Get recovery days based on sets

    # If the frequency does not allow enough recovery time
    if 7 / frequency < recovery_days:
        return None  # Return None if not enough time to recover

    for i in range(frequency):
        weekly_stimulus += total_AU  # Full effect if recovered
    
    return weekly_stimulus

# Function to determine muscle state based on weekly net stimulus
def muscle_recovery_state(weekly_stimulus):
    maintenance_AU = 1.61  # 3 sets once per week is maintenance
    if weekly_stimulus > maintenance_AU:
        return "Growth: Your muscle is likely to grow!"
    elif weekly_stimulus == maintenance_AU:
        return "Maintenance: Your muscle size will remain the same."
    else:
        return "Atrophy: Your muscle may decrease in size."

# Calculate weekly net stimulus
if st.button('Calculate'):
    weekly_net_stimulus = calculate_hypertrophy_with_recovery(sets_per_exercise, frequency_per_week)
    
    if weekly_net_stimulus is None:
        st.write("The volume of sets and frequency is too high to allow for recovery.")
    else:
        recovery_state = muscle_recovery_state(weekly_net_stimulus)
        st.write(f'Your weekly net stimulus is: {weekly_net_stimulus:.2f} AU')
        st.write(recovery_state)
