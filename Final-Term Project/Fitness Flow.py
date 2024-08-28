"""
Made By:

Name: Burhan Ul Haq
Roll No.: 08
Email: burhanrgrg8@gmail.com

Name: Abdullah Ahmed
Roll No.: 24
Email: abdullah.official@gmail.com
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

                # If Input is Less than Equal to Zero
                if weight <= 0:
                    print("\nNumber can't be Less than or Equal to Zero")
                    continue

                sets= int(input(f"Tell How Many Sets Have you Taken for {exercise_name}: "))

                # If Input is Less than Equal to Zero
                if sets <= 0:
                    print("\nNumber can't be Less than or Equal to Zero")
                    continue

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
            print(f"\nNo High Score Recorded for {exercise_name} yet.\n")
    
    # If any Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while checking high scores: {e}")

def set_goals(exercise_name):

    try:
        
        # Looping If there is a Error
        while True:
            try:

                # Input for Goal Weight and Sets For Particular Exercise
                Goal_Weight= int(input("\nTell your Weight Goal: "))

                # If Input is Less than or Equal to Zero
                if Goal_Weight <= 0:
                    print("\nNumber can't be Less than or Equal to Zero")
                    continue

                Goal_Set= int(input("Tell your Sets Goal: "))

                # If Input is Less than or Equal to Zero
                if Goal_Set <= 0:
                    print("\nNumber can't be Less than Equal to Zero")
                    continue

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

# Function to set diet plan
def set_diet_plan(exercise_name):

    # Making Diet File and Joining it in the Particular Exercise Folder
    Exercise_folder= os.path.join(Exercises_folder, exercise_name)
    Exercise_diet= os.path.join(Exercise_folder, "Diet Plan.txt")

    # Dictionary of Diet Plan
    diet_plan= {}

    # Looping If Any Error Occurs
    while True:

        try:

            # Input of Number of Items
            num_items = int(input(f"\nHow many items do you want to include in your {exercise_name} diet plan: "))

            # If Input is Less than or Equal to Zero
            if num_items <= 0:
                print("\nNumber Of Items Should be Greater than Zero")
                continue

            for i in range(1, num_items + 1):
                
                # Looping If Any Error Occurs
                while True:

                    # Input of Items 
                    item = input(f"\nEnter the name of food item {i}: ").strip()

                    # Validating If the Input is not the Directory
                    if item.isalpha():
                        break
                    else:
                        print("\nInvalid input. Please enter a Valid Food Item name.")

                # Looping if Any Error Occurs
                while True:

                    try:

                        # Input of Item Calories
                        calories = int(input(f"Enter the number of Calories for {item}: "))

                        # If Input is Less than or Equal to Zero
                        if calories <= 0:
                            print("\nCalories Must be a Positive Number, Please Enter a Valid Number\n")
                        else:
                            break

                    # If Value Error Occurs
                    except ValueError:
                        print("\nPlease Enter a Valid Integer for Calories\n")

                # Appending Items and their Calories to Dictionary
                diet_plan[item] = calories

            # Calculating Toal Calories
            total_calories= sum(diet_plan.values())

            # Writing Diet Plan to Particular Exercise
            with open(Exercise_diet, 'w') as b:
                b.write(f"Your Diet Plan for {exercise_name} is:\n\n")
                b.write(f"Total Calories: {total_calories}\n")
                for item, calories in diet_plan.items():
                    b.write(f"{item}: {calories}\n")

            # Prompt of Compeleting the Task
            print("\nYour diet plan has been set!\n")
            break

        # If Value Error Occurs
        except ValueError:
            print("\nPlease Enter a Valid Integer for Number of Items")

# Function to Check Diet
def check_diet(exercise_name):
        
    # Making Diet File and Joining it in the Particular Exercise Folder
    Exercise_folder= os.path.join(Exercises_folder, exercise_name)
    Exercise_diet= os.path.join(Exercise_folder, "Diet Plan.txt")

    # Looping If any Error Occurs
    while True:
    
        try:

            # Checking Exercise Diet Plan (If Exists)
            if not os.path.exists(Exercise_diet):
                print(f"\nNo Diet Plan Recorded for {exercise_name}. Please Set Diet Plan First\n")

                break

            else:
                # Input for Daily Diet Limit
                daily_calorie_limit = int(input(f"\nEnter your Daily Calorie limit for {exercise_name}: "))

            # If Input is Less than or Equal to Zero
            if daily_calorie_limit <= 0:
                print("\nCalorie can't be Equal to or Less than Zero")
                continue

            # Reading the Diet Plan
            with open(Exercise_diet, 'r') as a:
                lines= a.readlines()
                total_calories= int(lines[2].strip().split(":")[1])

                # Comparision Of Total Calories Set with Daily Calories
                if total_calories <= daily_calorie_limit:
                    print(f"\nGood job! Your diet is within the limit of {daily_calorie_limit} calories.\n")

                # If Daily Calories are less than Total Calories
                else:
                    print(f"\nWarning! Your diet exceeds the limit by {total_calories - daily_calorie_limit} calories.\n")

                # Displaying Diet Plan of Particular Exercise
                for line in lines:
                    print(f"{line.strip()}")
                break
        
        # If File Not Found Error Occurs
        except FileNotFoundError:
            print("\nError: The Diet plan file does not exist. Please Set a Diet Plan first.")
    
        # If Value Error Occurs
        except ValueError:
            print("\nError: Please write a Valid Integer for Daily Calorie Limit")

        # If Any Other Error Occurs
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

# Function to display the diet plan
def display_diet_plan(exercise_name):
        
    # Making Diet File and Joining it in the Particular Exercise Folder
    Exercise_folder= os.path.join(Exercises_folder, exercise_name)
    Exercise_diet= os.path.join(Exercise_folder, "Diet Plan.txt")

    # Reading Diet Plan for Particular Exercise (If Exists)
    if os.path.exists(Exercise_diet):
        with open(Exercise_diet, 'r') as c:
            lines= c.read()
            print(f"\n{lines}")

    # If Diet Plan Doesn't Exists
    else:
        print(f"\nNo Diet Plan Recorded for {exercise_name}\n")

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
                exercise_name= input("\nEnter the Name of the New Exercise: ").strip()

                # Making sure exercise_name is valid
                if exercise_name.isalpha() and exercise_name:
                    # Making a Folder for the New Exercise
                    Exercise_folder = os.path.join(Exercises_folder, exercise_name)
                    os.makedirs(Exercise_folder, exist_ok=True)
                    return exercise_name
                else:
                    print("\nInvalid Exercise name. Please enter a Valid Name.")
                    continue

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

                    # Looping if any Error Occurs
                    while True:
                        exercise_name= input("\nEnter the Name of the New Exercise: ").strip()

                        # Validating New Exercise Name
                        if exercise_name.isalpha() and exercise_name:
                            Exercise_folder = os.path.join(Exercises_folder, exercise_name)
                            os.makedirs(Exercise_folder, exist_ok=True)
                            return exercise_name
                        

                        else:
                            print("\nInvalid Exercise Name. Please enter a Valid Name.")
        
                # If User Inputs a Value Longer than what is available
                else:
                    print("\nInvalid Choice.")

            # If Value Error Occurs
            except ValueError:
                print("\nError: Please enter a valid number.")

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
            print("2. Display Log Data")
            print("3. Display High Score")
            print("4. Set Goal")
            print("5. Display Goal")
            print("6. Set Diet")
            print("7. Check Diet")
            print("8. Display Diet")

            # Input of Action that User want to Perform
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
            elif action_choice == 6:
                set_diet_plan(exercise_name)
            elif action_choice == 7:
                check_diet(exercise_name)
            elif action_choice == 8:
                display_diet_plan(exercise_name)
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
                print("1. Track Workout")
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