import pandas as pd

# --- 1. DATASET ---
# I'm using a simple dictionary to hold the study hours and scores
my_data = {
    'hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'scores': [52, 57, 63, 68, 72, 78, 82, 88, 93, 97]
}

# Convert to a dataframe to keep it organized
df = pd.DataFrame(my_data)
print("Checking my data table:")
print(df)

# --- 2. CALCULATING THE GROWTH ---
# I want to find out how many points a student gains for every hour.
# I will loop through the scores to find the average 'jump'.

points_total = 0
count = 0

for i in range(len(df['scores']) - 1):
    # Subtracting current score from the next one to find the increase
    jump = df['scores'][i+1] - df['scores'][i]
    points_total = points_total + jump
    count = count + 1

# This is the average points gained per hour
average_jump = points_total / count

# --- 3. PREDICTION FUNCTION ---
# This function calculates the final score. 
# It assumes a base score of 50 even if someone studies 0 hours.
def get_prediction(user_hours):
    starting_points = 50 
    
    # Simple math: starting score + (hours * value of each hour)
    answer = starting_points + (user_hours * average_jump)
    return answer

# --- 4. USER INTERFACE ---
print("\n--- Predict Your Result ---")

# Getting input from the user
input_val = input("How many hours did you study? ")

# Turning the text input into a number (float)
user_h = float(input_val)

# Calling the function to get the final answer
final_score = get_prediction(user_h)

print("---------------------------------")
print("Your Predicted Score is:", round(final_score, 2))
print("---------------------------------")