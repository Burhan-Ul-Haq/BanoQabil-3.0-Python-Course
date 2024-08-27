"""
Made By:

Name: Burhan Ul Haq
Roll No.: 08
Email: burhanrgrg8@gmail.com

Name: Abdullah Ahmed
Roll No.: 
Email: 
"""

# Library
import os
from datetime import datetime

# Base Directory Location set to Desktop
base_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Fitness Flow")

# Making of Program File Folder
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Making of Exercises Folder
Exercises_folder= os.path.join(base_dir, "Exercises")

if not os.path.exists(Exercises_folder):
    os.makedirs(Exercises_folder)

# Preset List of Exercises
Exercises_List= ["Bench Press", "Hammer Curl", "Knee Touch", "Pull Up", "Push Up", "Squat"]

# Making of Exercises in Exercises Folder
for Exercise in Exercises_List:
    Exercises= os.path.join(Exercises_folder, Exercise)

    if not os.path.exists(Exercises):
        os.makedirs(Exercises)

# Function of Exercises
def log_data(exercise_name):
    
    try:
        
        # Making of Particular Exercise Folder
        Exercise_folder= os.path.join(Exercises_folder, exercise_name)
        if not os.path.exists(Exercise_folder):
            os.makedirs(Exercise_folder)

        # HighScore File Path
        high_score_file = os.path.join(Exercise_folder, "High Score.txt")

        High_Score_Weight= 0
        High_Score_Sets= 0

        # Reading of High Score file for changing High Score (If Achieved)
        if os.path.exists(high_score_file):
            with open(high_score_file, 'r') as g:
                lines = g.readlines()
                if len(lines) > 2:
                    try:
                        High_Score_Sets= int(lines[1].strip().split(":")[1])
                        High_Score_Weight= int(lines[2].strip().split(":")[1])
                    except ValueError:
                        print("\nError: Invalid data format in high score file.")

        # Making of Exercise Log file
        log_file = os.path.join(Exercise_folder, f"{exercise_name}_log.txt")

        # Looping If there is a Error
        while True:
            # Input of Weight and Sets of Particular Exercise
            try:
                weight= int(input(f"\nTell How Much Weight Have you Pulled for {exercise_name} (KGs): "))
                sets= int(input(f"Tell How Many Sets Have you Taken for {exercise_name}: "))
                break
            # If Value Error Occurs
            except ValueError:
                print("\nError: Please enter a valid integer for Weight and Sets.")

        # Current Date and Time
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

            # Writing Log Data of Particular Exercise
        with open(log_file, 'a') as f:
            f.write(f"\nDate: {current_time}\nWeight: {weight} KGs\nSets: {sets}\n")

        # Comparison of old High Score Weight and Sets with New
        new_high_score_weight = weight > High_Score_Weight
        new_high_score_sets = sets > High_Score_Sets

        # Update high scores if new ones are achieved
        if new_high_score_weight:
            High_Score_Weight = weight

        if new_high_score_sets:
            High_Score_Sets = sets

        # Writing Data of Particular Exercise High Score
        with open(high_score_file, 'w') as g:
            g.write(f"Date: {current_time}\n")
            g.write(f"High Score Sets: {High_Score_Sets}\n")
            g.write(f"High Score Weight: {High_Score_Weight}\n")

        print(f"\n{exercise_name}:\nDate: {current_time}\nWeight: {weight} KGs\nSets: {sets}")

        # Prompt the User if New High Score is Achieved
        if new_high_score_weight or new_high_score_sets:
            print("\nNew High Score Achieved!")
            
        print(f"\nHigh Score:\nHigh Score Weight: {High_Score_Weight} KGs\nHigh Score Sets: {High_Score_Sets}\n")

    # If any Error Other than Value Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while logging data: {e}\n")

# Function for Checking Log Data
def check_log_data(exercise_name):

    try:

        # Joining Log File in Exercise Folder
        Exercise_folder= os.path.join(Exercises_folder, exercise_name)
        log_file = os.path.join(Exercise_folder, f"{exercise_name}_log.txt")

        # Reading Log Data of Particular Exercise (If Exists)
        if os.path.exists(log_file):
            with open(log_file,'r') as e:
                log_data= e.read()
            print(f"\nThe Log Data for {exercise_name} is:\n\n{log_data}")

        # If Log Data doesn't Exists
        else:
            print(f"\nNo Log Recorded for {exercise_name} yet.\n")

    # If any Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while setting goals: {e}\n")

def set_goals(exercise_name):

    try:
        
        # Looping If there is a Error
        while True:
            try:

                # Input for Goal Weight and Sets For Particular Exercise
                Goal_Weight= int(input("\nTell your Weight Goal: "))
                Goal_Set= int(input("Tell your Sets Goal: "))
                break

            # If Value Error Occurs
            except ValueError:
                print("\nError: Please Enter a valid Integer for Goal Weight and Sets.")

        # Looping If there is a Error
        while True:

            # Taking input of Date
            raw_date = input(f"Tell the Date (DD-MM-YYYY): ")

            # Checking if the input contains only digits and hyphens
            if all(char.isdigit() or char == '-' for char in raw_date):

                try:

                    # Splitting the Input into day, month, and year
                    day, month, year = raw_date.split('-')
    
                    # Check If all variables have their desired length
                    if len(day) == 2 and len(month) == 2 and len(year) == 4:
                        break
                    else:
                        print("\nError: The date must be in the format DD-MM-YYYY. Please try again.\n")
        
            # If Value Error Occurs
                except ValueError:
                    print("\nError: The date must be in the format DD-MM-YYYY. Please try again.\n")
    
            # If the input contains characters other than digits or hyphens
            else:
                print("\nError: The date must be in the format DD-MM-YYYY. Please try again.\n")
        
        # Assign Value to Other Variable
        Goal_Time= raw_date

        # Making Goal File and Joining it in the Particular Exercise Folder
        Exercise_folder= os.path.join(Exercises_folder, exercise_name)
        goal_file= os.path.join(Exercise_folder, "Goals.txt")

        # Writing Goal in the File
        with open(goal_file, 'w') as g:
            g.write(f"Date: {Goal_Time}\n")
            g.write(f"Goal Weight: {Goal_Weight} KGs\n")
            g.write(f"Goal Sets: {Goal_Set}\n")

        print(f"\nGoal set for {exercise_name}: \nDate: {Goal_Time}\nWeight = {Goal_Weight} KGs\nSets = {Goal_Set}\n")

    # If Value Error Occurs
    except ValueError:
        print("\nError: Please enter a valid Integer for weight and sets.")
    
    # If any Error Other than Value Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while setting goals: {e}")

# Function for Checking Goals
def check_goals(exercise_name):
    
    try:

        # Joining Goals File in the Exercise Folder
        Exercise_folder= os.path.join(Exercises_folder, exercise_name)
        goal_file= os.path.join(Exercise_folder, "Goals.txt")

        # Reading Goal Data of Particular Exercise (If Exists)
        if os.path.exists(goal_file):
            with open(goal_file, 'r') as b:
                goal_data= b.read()
            print(f"\nGoal for {exercise_name}:\n{goal_data}")
    
        # If Goal Doessn't Exists
        else:
            print(f"\nNo Goal recorded for {exercise_name} yet.\n")

    # If any Error Occurs
    except Exception as e:
        print(f"\nAn Error occured while checking Goals: {e}\n")

# Function for Checking High Score:
def check_high_score(exercise_name):

    try:

        # Joining High Score File in the Exercise Folder
        Exercise_folder= os.path.join(Exercises_folder, exercise_name)
        high_score_file= os.path.join(Exercise_folder, "High Score.txt")

        # Reading High Score Of Particular Exercise (If Exists)
        if os.path.exists(high_score_file):
            with open(high_score_file, 'r') as g:
                high_score_data = g.read()
            print(f"\nHigh Score for {exercise_name}:\n{high_score_data}")
        
        # If High Score Doesn't Exists
        else:
            print(f"\nNo high score recorded for {exercise_name} yet.\n")
    
    # If any Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while checking high scores: {e}")

# Function for List of Exercises
def exercise_menu():

    # Looping If there is a Error
    while True:
        try:

            # Making List of Exercises Available in Exercise Folder
            exercises= [f for f in os.listdir(Exercises_folder) if os.path.isdir(os.path.join(Exercises_folder, f))]

            # Checking if there is Exercises Available in Exercise folder (Won't Occur in Normal Scenario)
            if not exercises:
                print("\nNo Exercises found.")
                exercise_name= input("\nEnter the Name of the New Exercise: ")
        
                # Making of Particular Exercise Folder
                Exercise_folder= os.path.join(Exercises_folder, exercise_name)
                if not os.path.exists(Exercise_folder):
                    os.makedirs(Exercise_folder)
        
                return exercise_name

            # Listing the Exercises
            print("\nExisting Exercises:")
            for i, exercise_name in enumerate(exercises, 1):
                print(f"{i}. {exercise_name}")

            # Option for Adding New Exercises
            print(f"{len(exercises) + 1}. Add a New Exercise\n")

            try:
                # Taking Input for Exercises
                choice= int(input("Select an Exercise by Number: "))

                # Checking which Number user Entered corresponding to the Exercise
                if 1 <= choice <= len(exercises):
                    return exercises[choice - 1]
                elif choice == len(exercises) + 1:
                    exercise_name= input("\nEnter the Name of the New Exercise: ")
        
                    # Making of Particular Exercise Folder
                    Exercise_folder= os.path.join(Exercises_folder, exercise_name)
                    if not os.path.exists(Exercise_folder):
                        os.makedirs(Exercise_folder)
        
                    return exercise_name
        
                # If User Inputs a Value Longer than what is available
                else:
                    print("\nInvalid Choice.")

            # If Value Error Occurs
            except ValueError:
                print("\nError: Please enter a valid number.\n")

        # If Any Error Other than Value Error Occurs
        except Exception as e:
            print(f"\nAn Error occurred while selecting an exercise: {e}")

# Function for List of Action that can be Performed
def perform_action(exercise_name):

    # Looping If there is an Error
    while True:

        try:
        
            # Printing Actions that can be performed
            print(f"\nWhat would you like to do with {exercise_name}?")
            print("1. Log Data")
            print("2. Check Log Data")
            print("3. Check High Score")
            print("4. Set Goal")
            print("5. Check Goal")

            # Input of Action that User want to perform
            action_choice= int(input("\nEnter Number what you want to do: "))

            # Checking Input and running Functions according to it
            if action_choice == 1:
                log_data(exercise_name)
            elif action_choice == 2:
                check_log_data(exercise_name)
            elif action_choice == 3:
                check_high_score(exercise_name)
            elif action_choice == 4:
                set_goals(exercise_name)
            elif action_choice == 5:
                check_goals(exercise_name)
            else:
                print("\nInvalid choice\n")
                continue

            # Looping If there is an Error
            while True:

                print("Do you want to Exit or Continue?")
                print("Enter 1 to Continue")
                print("Enter 2 to Exit\n")

                try:
                    cont = int(input("Select a Number: "))
                    if cont == 2:
                        print("\nExiting the program. Goodbye!")
                        return
                    elif cont == 1:
                        return
                    else:
                        print("\nError: Please Enter 1 to Continue or 2 to Exit.\n")

                # If Value Error Occurs
                except ValueError:
                    print("\nError: Please Enter a Valid Number.\n")
    
        # If Any Error Other than Value Error Occurs
        except Exception as e:
            print(f"\nAn Error occurred while performing the action: {e}")

# Function for Main Menu
def main_menu():

    try:
        print("\nRunning Program...")

        # Looping if any Errors Occurs
        while True:

            try:
                # Printing actions that can be performed
                print("\nWhat would you like to do?")
                print("1. Workout Tracker")
                print("2. Prioritize Exercise")
                print("3. Fitness Challenge")

                # Input of Action that User wants to perform
                main_choice = int(input("\nEnter the number of what you want to do: "))

                # Running and calling functions based on user choice
                if main_choice == 1:
                    exercise_name = exercise_menu()
                    if exercise_name:
                        perform_action(exercise_name)
                elif main_choice == 2:
                    Prioritize(exercise_menu())
                elif main_choice == 3:
                    Fitness(exercise_menu())
                else:
                    print("\nInvalid Choice")
                    continue

            # If Value Error Occurs
            except ValueError:
                print("\nError: Please Enter a Valid Number")
                continue

    # If any Error Other than Value Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while performing the action: {e}")

# Looping Program
first_run = True
while first_run or main_menu():
    first_run = False

"""
Made By: Burhan Ul Haq
"""
