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
from datetime import datetime, timedelta
import random
import shutil

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

# # Making of Exercises in Exercises Folder
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

                    # If Value Error Occurs
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
            
            # If User Keyboard Interrupts
            except KeyboardInterrupt:

                print("\n\nDo you want to Quit?")
                print("1. Yes")
                print("2. No")

                # Input if User want to Quit
                quitting= int(input("\nEnter the Number: "))

                if quitting == 1:
                    exit()

                elif quitting == 2:
                    continue

                else:
                    print("\nInvalid Choice")

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
            
        print(f"\nHigh Score:\nHigh Score Weight: {High_Score_Weight} KGs\nHigh Score Sets: {High_Score_Sets}")

        # Goal File Path
        goal_file= os.path.join(base_dir, Exercises_folder, exercise_name, "Goals.txt")

        # If Goal File Exists
        if os.path.exists(goal_file):

            # Reading Goal File
            with open(goal_file, 'r') as w:
                goal_data= w.read()
            
            # Extracting Data from Goal File
            goal_exercise= goal_data.split("Exercise: ")[1].split("\n")[0].strip()
            goal_weight= int(goal_data.split("Goal Weight: ")[1].split("KGs")[0].strip())
            goal_sets= int(goal_data.split("Goal Sets: ")[1].split("\n")[0].strip())

            # Checking if Exercise name and Goal Name match
            if exercise_name== goal_exercise:

                # Comparing Weight and Sets with Goal Weight and Sets
                if weight >= goal_weight and sets >= goal_sets:
                    print("\nCongrats, You have Reached you Goals")
                
                # Reading Goal Fole
                with open(goal_file, 'r') as t:
                    goal_status= t.read()
                
                # Updating Goal File
                goal_updated_status = goal_status.replace("Status: Incomplete", "Status: Complete")

                # Writing Updated Data in Goal File
                with open(goal_file, 'w') as o:
                    o.write(goal_updated_status)

        # Check Fitness Challenge
        Fitness_Challenge_file = os.path.join(base_dir, "Fitness Challenge", "Fitness Challenge.txt")

        # Checking if Challenge File Exists
        if os.path.exists(Fitness_Challenge_file):

            # Reading Fitness Challenge File
            with open(Fitness_Challenge_file, 'r') as f:
                challenge_data = f.read()

            # Extracting Challenge Details
            challenge_exercise = challenge_data.split("Challenge Exercise: ")[1].split("\n")[0].strip()
            challenge_weight = int(challenge_data.split("Weight: ")[1].split(" KGs")[0].strip())
            challenge_sets = int(challenge_data.split("Sets: ")[1].split("\n")[0].strip())

            # Checking if Log Exercise and Challenge Exercise Name match
            if challenge_exercise == exercise_name:

                # Compare Challenge data with Log data
                if weight >= challenge_weight and sets >= challenge_sets:
                    print("\nCongrats, on Completing the Challenge, Treat yourself with a Cheat Day.")
                    
                    # Reading Challenge File
                    with open(Fitness_Challenge_file, 'r') as c:
                        content = c.read()

                    # Updating Challenge file
                    updated_content = content.replace('Challenge Status: Incomplete', 'Challenge Status: Completed')

                    # Writing Updated Data
                    with open(Fitness_Challenge_file, 'w') as c:
                        c.write(updated_content)

                    # Running More Challenge Function
                    More_Challenge()

        # Path of Limit File
        Limit_file= os.path.join(base_dir, "Fitness Challenge", "Limit.txt")

        if os.path.exists(Limit_file):

            # Reading Limit Challenge File
            with open(Limit_file, 'r') as e:
                Limit_data= e.read()

            # Extracting Limit Challenge Details
            limit_exercise= Limit_data.split("Exercise: ")[1].split("\n")[0].strip()
            limit_sets= int(Limit_data.split("Highest Sets: ")[1].split("\n")[0].strip())
            limit_weight= int(Limit_data.split("Highest Weight: ")[1].split("KGs")[0].strip())

            # Checking If Log Data Exercise Name and Limit Data Exercise Name Match
            if limit_exercise== exercise_name:

                # Comparing Log Data with Limit Challenge Data
                if weight >= limit_weight and sets>= limit_sets:
                    print("\nCongrats, on Pushing your Highest Limit, Treat yourself with a Cheat Day.")

                    # Reading Limit Challenge File
                    with open(Limit_file, 'r') as q:
                        status= q.read()

                    # Updating Limit Challenge File
                    updated_status= status.replace("Status: Incomplete", "Status: Complete")

                    # Writing Updated Data
                    with open(Limit_file, 'w') as e:
                        e.write(updated_status)

                    # Running More Push Limit Function
                    More_Push_limit()

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
            print(f"\nNo Log Recorded for {exercise_name} yet.")

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
            print(f"\nNo High Score Recorded for {exercise_name} yet.")
    
    # If any Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while checking high scores: {e}")

def set_goals(exercise_name):

    # Goal File Path
    goal_file= os.path.join(base_dir, Exercises_folder, exercise_name, "Goals.txt")

    # Current Time
    current_time= datetime.now()

    # If Goal File Exists
    if os.path.exists(goal_file):

        # Reading Goal File
        with open(goal_file, 'r') as v:
            goal_content= v.read()

        # Checking If Status is Incomplete
        if "Status: Incomplete" in goal_content:

            # Looping if there is an Error
            while True:
                    
                    try:

                        print("\nDid you Compelete the Goal?")
                        print("1. Yes")
                        print("2. No\n")

                        # Input If User Completed Goal
                        ask= int(input("Enter the Number: "))

                        if ask== 1:
                            print("\nCongrats, on Completing the Goal, Treat Yourself with a Cheat Day\n")
                            
                            # Reading Goal File
                            with open (goal_file, 'r') as m:
                                goal_status= m.read()
                            
                            # Updating Goal File
                            updated_goal_status= goal_status.replace("Status: Incomplete", "Status: Complete")

                            # Writing Updated Data
                            with open(goal_file, 'w') as i:
                                i.write(updated_goal_status)
                            
                            # Running More Goals Function
                            More_Goals

                            break

                        elif ask== 2:
                            
                            # If there is an Error
                            while True:

                                try:
                                    
                                    # Reading Challenge File to check Challenge Time
                                    with open(goal_file, 'r') as t:
                                        check_goal= t.read().strip()
                                        
                                    lines = check_goal.splitlines()

                                    goal_date_str= None

                                    for line in lines:

                                        # Finding Challenge Time in Challenge File
                                        if 'Date' in line:

                                            # Split the Challenge Time
                                            goal_date_str = line.split(': ', 1)[1].strip()
                                            break
                                        
                                    if goal_date_str:

                                        # Converting Goal Time in to Date and Time Format
                                        goal_time = datetime.strptime(goal_date_str, '%d-%m-%Y')

                                        # Comparision of Goal Time and Current Time
                                        if goal_time > current_time:

                                            print("\nThere is still time left for you to complete the challenge. Do you still want to change the Goal?")
                                            print("1. Yes")
                                            print("2. No\n")

                                            # Input of User to Change the Goal or Not
                                            Goal_change= int(input("Enter the Number: "))

                                            if Goal_change == 1:

                                                # Running Generate Goals Function
                                                Generate_Goals()

                                            elif Goal_change == 2:

                                                # Running Loop Program Function
                                                Loop_Program()

                                            else:
                                                ("\nInvalid Choice") 
                    
                                        else:

                                            # Running More Goals Function
                                            More_Goals()
                                            break
                                    
                                    else:
                                        print("\nGoal Time not found in this File")

                                # If Value Error Occurs
                                except ValueError:
                                    print("\nPlease Enter a Valid Integer")

                                # If User Keyboard Interrupts
                                except KeyboardInterrupt:
                
                                    print("\n\nDo you want to Quit?")
                                    print("1. Yes")
                                    print("2. No")

                                    # Input if User wants to Quit
                                    quitting= int(input("\nEnter the Number: "))

                                    if quitting == 1:
                                        exit()

                                    elif quitting == 2:
                                        continue

                                    else:
                                        print("\nInvalid Choice")

                                # If Any other Error Occurs
                                except Exception as e:
                                    print(f"\nAn Error Occured while performing the action: {e}")

                        else:
                            print("\nInvalid Choice")
                            continue

                    # If Value Error Occurs
                    except ValueError:
                        print("Error: Please write a Valid Integer")

                    # If User Keyboard Interrupts
                    except KeyboardInterrupt:
                        
                        print("\n\nDo you want to Quit?")
                        print("1. Yes")
                        print("2. No")

                        # Input of User to Quit or not
                        quitting= int(input("\nEnter the Number: "))

                        if quitting == 1:
                            exit()

                        elif quitting == 2:
                            continue

                        else:
                            print("\nInvalid Choice")
                        
                    # If any Other Error Occurs
                    except Exception as e:
                        print(f"\nAn Error occured while performing the action: {e}")
        
        else:

            # Running Generate Goals Function
            Generate_Goals()

    else:

        # Running Generate Goals Function
        Generate_Goals()

# Function for Generating Goals
def Generate_Goals():

    # Invoking Exercise Menu Function and giving the Value to Exercise Name
    exercise_name= exercise_menu()

    # Joining High Score File in the Exercise Folder
    Exercise_folder= os.path.join(Exercises_folder, exercise_name)
    high_score_file= os.path.join(Exercise_folder, "High Score.txt")
    
    # Current Time
    current_time= datetime.now()
    
    try:
        
        if exercise_name:

            # Looping If there is a Error
            while True:
                try:

                    # Input for Goal Weight and Sets For Particular Exercise
                    Goal_Weight= int(input("\nTell your Weight Goal: "))

                    # If Input is Less than or Equal to Zero
                    if Goal_Weight <= 0:
                        print("\nNumber can't be Less than or Equal to Zero")
                        continue

                    # Reading High Score FIle
                    with open (high_score_file, 'r') as u:
                        highscore_data= u.readlines()

                    if len(highscore_data) > 2:

                        # Extracting Data from High Score File
                        High_Score_Weight= int(highscore_data[2].strip().split(": ")[1])

                    # Comparision of High Score Weight and Goal Weight
                    if High_Score_Weight > Goal_Weight:
                        print("\nYou have already reached the weight")
                        continue

                    Goal_Set= int(input("Tell your Sets Goal: "))

                    # If Input is Less than or Equal to Zero
                    if Goal_Set <= 0:
                        print("\nNumber can't be Less than Equal to Zero")
                        continue

                    # Reading High Score File
                    with open (high_score_file, 'r') as u:
                        highscore_data= u.readlines()

                    if len(highscore_data) > 2:

                        # Extracting Data from High Score
                        High_Score_Sets= int(highscore_data[1].strip().split(": ")[1])

                    # Comparision of High Score Sets with Goal Sets
                    if High_Score_Sets > Goal_Set:
                        print("\nYou have already reached the Sets")
                        continue

                    break

                # If Value Error Occurs
                except ValueError:
                    print("\nError: Please Enter a valid Integer for Goal Weight and Sets.")
                
                # If User Keyboard Interrupts
                except KeyboardInterrupt:
                    
                    print("\n\nDo you want to Quit?")
                    print("1. Yes")
                    print("2. No")

                    # Input of User to Quit or not
                    quitting= int(input("\nEnter the Number: "))

                    if quitting == 1:
                        exit()

                    elif quitting == 2:
                        continue

                    else:
                        print("\nInvalid Choice")
                
                # If Any other Error Occurs
                except Exception as e:
                    print(f"\nAn Error Occured while performing the action: {e}")

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
                            goal_date= datetime(int(year), int(month), int(day))

                            if goal_date < current_time:
                                print("\nDate can't be Lower than Current Time\n")
                                continue
                            break
                        
                        else:
                            print("\nError: The date must be in the format DD-MM-YYYY. Please try again.\n")
            
                    # If Value Error Occurs
                    except ValueError:
                        print("\nError: The date must be in the format DD-MM-YYYY. Please try again.\n")

                    # If User Keyboard Interrupts
                    except KeyboardInterrupt:
                    
                        print("\n\nnDo you want to Quit?")
                        print("1. Yes")
                        print("2. No")

                        # Input if User wants to Quit
                        quitting= int(input("\nEnter the Number: "))

                        if quitting == 1:
                            exit()

                        elif quitting == 2:
                            continue

                        else:
                            print("\nInvalid Choice")

                    # If Any other Error Occurs
                    except Exception as e:
                        print(f"\nAn Error Occured while performing the action: {e}")

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
                g.write(f"Exercise: {exercise_name}\n")
                g.write(f"Date: {Goal_Time}\n")
                g.write(f"Goal Weight: {Goal_Weight} KGs\n")
                g.write(f"Goal Sets: {Goal_Set}\n")
                g.write("Status: Incomplete")

            print(f"\nExercise: {exercise_name}\nDate: {Goal_Time}\nWeight = {Goal_Weight} KGs\nSets = {Goal_Set}\nStatus: Incomplete")

    # If Value Error Occurs
    except ValueError:
        print("\nError: Please enter a valid Integer for weight and sets.")

    # If User Keyboard Interrupts
    except KeyboardInterrupt:
    
        print("\n\nnDo you want to Quit?")
        print("1. Yes")
        print("2. No")

        # Input if User wants to Quit
        quitting= int(input("\nEnter the Number: "))

        if quitting == 1:
            exit()

        elif quitting == 2:
            Generate_Goals()

        else:
            print("\nInvalid Choice")

    # If any Error Other than Value Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while setting goals: {e}")

# Function for More Challenge
def More_Goals():

    # If there is an Error
    while True:

        try:

            print("\nDo you want to Set Goal?")
            print("1. Yes")
            print("2. No")

            # Input of User to Quit
            ask= int(input("\nEnter the Number: "))           

            if ask== 1:

                # Running Generate Push Limit Function
                Generate_Goals()
                break

            elif ask== 2: 

                # Running Loop Program Function
                Loop_Program()
                break
            
            else:
                ("\nInvalid Choice")

        # If Value Error Occurs
        except ValueError:
            print("\nError: Please Enter a Valid Integer")

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
        
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")

        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")


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

            print(f"{goal_data}")
    
        # If Goal Doessn't Exists
        else:
            print(f"\nNo Goal recorded for {exercise_name} yet.")

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

                    # If User Keyboard Interrupts
                    except KeyboardInterrupt:
                        
                        print("\n\nDo you want to Quit?")
                        print("1. Yes")
                        print("2. No")

                        # Input if User wants to Quit
                        quitting= int(input("\nEnter the Number: "))

                        if quitting == 1:
                            exit()

                        elif quitting == 2:
                            continue

                        else:
                            print("\nInvalid Choice")

                    # If Any other Error Occurs
                    except Exception as e:
                        print(f"\nAn Error Occured while performing the action: {e}")

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
            print("\nYour diet plan has been set!")
            break

        # If Value Error Occurs
        except ValueError:
            print("\nPlease Enter a Valid Integer for Number of Items")
        
        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")
        
        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

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
                print(f"\nNo Diet Plan Recorded for {exercise_name}. Please Set Diet Plan First.")
                break
            
            # If Exercise Diet Plan Exists
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

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")

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
        print(f"\nNo Diet Plan Recorded for {exercise_name}")

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
            
            # If User Keyboard Interrupts
            except KeyboardInterrupt:
                
                print("\n\nDo you want to Quit?")
                print("1. Yes")
                print("2. No")

                # Input if User wants to Quit
                quitting= int(input("\nEnter the Number: "))

                if quitting == 1:
                    exit()

                elif quitting == 2:
                    continue

                else:
                    print("\nInvalid Choice")
            
            # If Any other Error Occurs
            except Exception as e:
                print(f"\nAn Error Occured while performing the action: {e}")

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
                
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")

        # If Any Error Other than Value Error Occurs
        except Exception as e:
            print(f"\nAn Error occurred while selecting an exercise: {e}")

# Function for Fitness Challenge
def Fitness_Challenge():

    # Looping If there is an Error
    while True:
        try:

            # Printing Options
            print("\nWhat you want to do?")
            print("1. Generate Challenge")
            print("2. Display Fitness Challenge")
            print("3. Push your Limits")
            print("4. Display Limit Challenge\n")
    
            # Input What User want to do
            action = int(input("Tell the Number: "))

            if action == 1:

                # Running Generate Challenge Function
                generate_challenge()
                pass
            
            elif action == 2:

                # Running Display Challenge Function
                display_fitness_challenge()

            elif action == 3:

                # Running Push Limit Function
                Push_limit()

            elif action == 4:
                
                # Running Display Limit Challenge Function
                display_limit()

            else:
                print("\nInvalid Choice")
                continue

        # If Value Error Occurs
        except ValueError:
            print("\nError: Please write a Valid Integer")
        
        # If User Keyboard Interrupts
        except KeyboardInterrupt:
                
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")

        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

# Function for Displaying Challenge
def display_fitness_challenge():

    # Making of Fitness Challenge File
    Fitness_Folder= os.path.join(base_dir, "Fitness Challenge")

    if not os.path.exists(Fitness_Folder):
        os.makedirs(Fitness_Folder)
        
    Fitness_Challenge_file= os.path.join(Fitness_Folder, "Fitness Challenge.txt")

    try:

        # Reading Fitness Challenge File to Display the Challenge
        with open(Fitness_Challenge_file, 'r') as b:
            lines= b.read()

            print(lines.strip())
            Loop_Program()
                
    # If File Not Found Error Occurs
    except FileNotFoundError:
        print("\nPlease Generate a Challenge First.")
    
    # If Any other Error Occurs
    except Exception as e:
        print(f"\nAn Error Occured while performing the action: {e}")

# Function for Generating Challenge
def generate_challenge():

    # Making of Fitness Challenge File
    Fitness_Folder= os.path.join(base_dir, "Fitness Challenge")

    if not os.path.exists(Fitness_Folder):
        os.makedirs(Fitness_Folder)
        
    Fitness_Challenge_file= os.path.join(Fitness_Folder, "Fitness Challenge.txt")

    # Current Time
    current_time= datetime.now()
                
    # Checking If Fitness Challenge File is Already There
    if os.path.exists(Fitness_Challenge_file):
                        
        # Reading Challenge File
        with open(Fitness_Challenge_file, 'r') as c:
            content = c.read()
                    
        # Checking Challenge Status
        if 'Challenge Status: Incomplete' in content:

            # Looping If There is an Error
            while True:
                try:

                    # Checking If User Compeleted the Given Challenge
                    print("\nDid you Complete the Challenge")
                    print("1. Yes")
                    print("2. No")

                    # Taking Input whether User compelted the Challenge or not
                    compeletion_challenege= int(input("\nEnter the Number: "))

                    if compeletion_challenege == 1:
                        print("\nCongrats, Treat Yourself with a Cheat Day")

                        # Reading Challenge File
                        with open(Fitness_Challenge_file, 'r') as c:
                            content = c.read()

                        # Updating Challenge file
                        updated_content = content.replace('Challenge Status: Incomplete', 'Challenge Status: Completed')

                        # Writing Updated Data
                        with open(Fitness_Challenge_file, 'w') as c:
                            c.write(updated_content)

                        More_Challenge()

                    elif compeletion_challenege == 2:

                        # Looping If there is an Error
                        while True:
                                try:

                                     # Reading Challenge File to check Challenge Time
                                    with open(Fitness_Challenge_file, 'r') as t:
                                        check_challenge= t.read().strip()
                                        
                                    lines = check_challenge.splitlines()

                                    challenge_time_str= None

                                    for line in lines:

                                        # Finding Challenge Time in Challenge File
                                        if 'Challenge Time' in line:

                                            # Split the Challenge Time
                                            challenge_time_str = line.split(': ', 1)[1].strip()
                                            break
                                        
                                    if challenge_time_str:

                                        # Converting Challenge Time in to Date and Time Format
                                        challenge_time = datetime.strptime(challenge_time_str, '%m-%d-%Y %H:%M')

                                        # Comparision of Challenge Time and Current Time
                                        if challenge_time > current_time:

                                            print("\nThere is still time left for you to complete the challenge. Do you still want to change the Challenge?")
                                            print("1. Yes")
                                            print("2. No\n")

                                            # Input of User to Change the Challenge or Not
                                            Challenge_change= int(input("Enter the Number: "))

                                            if Challenge_change == 1:

                                                # Running Challenge Function
                                                Challenge()

                                            elif Challenge_change == 2:

                                                # Running Loop Program Function
                                                Loop_Program()

                                            else:
                                                ("\nInvalid Choice") 
                    
                                        else:
                                            print("\nNo Worries, Better Luck Next Time")

                                            # Running More Challenge Function
                                            More_Challenge()
                                            break
                                    
                                    else:
                                        print("\nChallenge Time not found in this File")

                                # If Value Error Occurs
                                except ValueError:
                                    print("\nPlease Enter a Valid Integer")

                                # If User Keyboard Interrupts
                                except KeyboardInterrupt:
                
                                    print("\n\nDo you want to Quit?")
                                    print("1. Yes")
                                    print("2. No")

                                    # Input if User wants to Quit
                                    quitting= int(input("\nEnter the Number: "))

                                    if quitting == 1:
                                        exit()

                                    elif quitting == 2:
                                        continue

                                    else:
                                        print("\nInvalid Choice")

                                # If Any other Error Occurs
                                except Exception as e:
                                    print(f"\nAn Error Occured while performing the action: {e}")

                    else:
                        print("\nInvalid Choice")
                        continue

                # If Value Error Occurs
                except ValueError:
                    print("\nPlease Write a Valid Integer")

                # If User Keyboard Interrupts
                except KeyboardInterrupt:
                
                    print("\n\nDo you want to Quit?")
                    print("1. Yes")
                    print("2. No")

                    # Input if User wants to Quit
                    quitting= int(input("\nEnter the Number: "))

                    if quitting == 1:
                        exit()

                    elif quitting == 2:
                        continue

                    else:
                        print("\nInvalid Choice")
                
                # If Any other Error Occurs
                except Exception as e:
                    print(f"\nAn Error Occured while performing the action: {e}")

        else:
            # Running the function Challenge
            Challenge()

    else:
        # Running the function Challenge    
        Challenge()

def Push_limit():
        
    # Making of Fitness Challenge File
    Fitness_Folder= os.path.join(base_dir, "Fitness Challenge")

    if not os.path.exists(Fitness_Folder):
        os.makedirs(Fitness_Folder)

    # Making of Limit File
    Limit= os.path.join(Fitness_Folder, "Limit.txt")

    # Checking If Limit File Exists
    if os.path.exists(Limit):

        # Reading Limit File
        with open(Limit, 'r') as r:
            push=r.read()

        # Checking if Status is Incompelete
        if "Status: Incomplete" in push:

            # If there is an Error
            while True:
                try:

                    print("\nDid you Reached the Push Limit?")
                    print("1. Yes")
                    print("2. No")

                    # Input of Asking that if the User Reached the Limit or not
                    limit_choice= int(input("\nEnter the Number: "))

                    if limit_choice== 1:
                        print("\nCongrats on Reaching the Limit")

                        # Running More Push Limit function
                        More_Push_limit()

                        # Reading Limit File
                        with open(Limit, 'r') as v:
                            push= v.read()
                        
                        # Updating the Value in Limit File
                        updated_state= push.replace("Status: Incomplete", "Status: Complete")

                        # Writing Updated Value in Limit File
                        with open(Limit, 'w') as z:
                            z.write(updated_state)
                        break

                    elif limit_choice == 2:
                        print("\nNo Worries!, Keep Trying You can make it happen.")

                        # Running Loop Program Function
                        Loop_Program()
                        break
                    
                    else:
                        ("\nInvalid Choice")
                        continue

                # If Value Error Occurs
                except ValueError:
                    print("Error: Please Enter a Valid Integer")

                # If User Keyboard Interrupts
                except KeyboardInterrupt:
                
                    print("\n\nDo you want to Quit?")
                    print("1. Yes")
                    print("2. No")

                    # Input if User wants to Quit
                    quitting= int(input("\nEnter the Number: "))

                    if quitting == 1:
                        exit()

                    elif quitting == 2:
                        continue

                    else:
                        print("\nInvalid Choice")

                # If Any other Error Occurs
                except Exception as e:
                    print(f"\nAn Error Occured while performing the action: {e}")

        else:

            # Running Generate Push Limit Function
            Generate_Push_Limit()
    else:

        # Running Generate Push Limit Function
        Generate_Push_Limit()


# Function for Displaying Limit Challenge
def display_limit():

    # Making of Fitness Challenge File
    Fitness_Folder= os.path.join(base_dir, "Fitness Challenge")

    # Making of Limit File
    Limit= os.path.join(Fitness_Folder, "Limit.txt")

    try:

        with open(Limit, 'r') as e:
            display= e.read()

        print(display.strip())

    # If File Not Found Error Occurs
    except FileNotFoundError:
        print("\nNo Such File Exists Please Generate a Limit Challenge First")
    
    # If any other Error Occurs
    except Exception as e:
        print(f"\nAn Error Occured while performing the action: {e}")

# Function for More Challenge
def More_Push_limit():

    # If there is an Error
    while True:

        try:

            print("\nDo you want to further Push Your Limit?")
            print("1. Yes")
            print("2. No")

            # Input of User to Quit
            ask= int(input("\nEnter the Number: "))           

            if ask== 1:

                # Running Generate Push Limit Function
                Generate_Push_Limit()
                break

            elif ask== 2: 

                # Running Loop Program Function
                Loop_Program()
                break
            
            else:
                ("\nInvalid Choice")

        # If Value Error Occurs
        except ValueError:
            print("\nError: Please Enter a Valid Integer")

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
        
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")

        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

# Function for Genrating Push Limit
def Generate_Push_Limit():
        
    # Invoking Exercise Menu Function annd giving Data to Exercise Name
    exercise_name= exercise_menu()

    # Making of Fitness Challenge File
    Fitness_Folder= os.path.join(base_dir, "Fitness Challenge")

    if not os.path.exists(Fitness_Folder):
        os.makedirs(Fitness_Folder)
    
    # Making of Particular Exercise Folder
    Exercise_folder= os.path.join(Exercises_folder, exercise_name)

    # HighScore File Path
    high_score_file = os.path.join(Exercise_folder, "High Score.txt")

    # Making of Limit File
    Limit= os.path.join(Fitness_Folder, "Limit.txt")

    # Current Time
    current_time= datetime.now().replace(second=0, microsecond=0)

    if exercise_name:        

        High_Score_Weight= 0
        High_Score_Sets= 0

        if os.path.exists(high_score_file):

            try:

                # Reading High Score File
                with open(high_score_file, 'r') as t:
                    limit= t.readlines()
                    
                    if len(limit) > 2:
                        try:

                            High_Score_Sets= limit[1].strip().split(": ")[1]

                            if High_Score_Sets.isnumeric():
                                High_Score_Sets = int(High_Score_Sets)
                            
                            else:
                                print("\nA Problem occured while performing the action\n")

                            High_Score_Weight= limit[2].strip().split(": ")[1]

                            if High_Score_Weight.isnumeric():
                                High_Score_Weight = int(High_Score_Weight)
                            
                            else:
                                print("\nA Problem occured while performing the action\n")

                        # If Value Error Occcurs
                        except ValueError:
                            print("\nInvalid Data format for High Score file.")

            # If File not Found Error Occurs
            except FileNotFoundError:
                print("\nPlease Create a High Score First.\n")
        
        else:
            print(f"\nPlease Create a High Score for: {exercise_name}, Making High Score Weight and Sets Zero\n")

    # Assigning the Value of High Score file to Local Variables
    max_weight_value= High_Score_Weight
    max_set_value= High_Score_Sets

    max_weight_value += 10
    max_set_value += 5

    # Randomly Choosing the Values
    Weight_Value= random.randint(High_Score_Weight, max_weight_value)
    Set_Value= random.randint(High_Score_Sets, max_set_value)

    # Writing Data in the Limit File
    with open(Limit, 'w+') as e:
        e.write(f"Exercise: {exercise_name}\n")
        e.write(f"Date: {current_time}\n")
        e.write(f"Highest Sets: {Set_Value}\n")
        e.write(f"Highest Weight: {Weight_Value} KGs\n")
        e.write(f"Status: Incomplete")
        
    print(f"Exercise: {exercise_name}\n")
    print(f"Date: {current_time}\n")
    print(f"Highest Sets: {Set_Value}\n")
    print(f"Highest Weight: {Weight_Value} KGs\n")
    print(f"Status: Incomplete")

    # Looping If There is an Error
    while True:

        try:
            print("\nDo you Want to Change the Challenge?")
            print("1. Yes")
            print("2. No")
                
            # Input If User want to Change the Challenge
            change_limit= int(input("\nEnter the Number: "))

            if change_limit == 1:

                # Running More Push Limit Function
                Generate_Push_Limit()
                break

            elif change_limit == 2:

                # Running Loop Program Fuction
                Loop_Program()
                break

            else:
                print("\nInvalid Choice")
                continue

        # If Value Error Occurs
        except ValueError:
            print("\nPlease Enter a Valid Integer")

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")
        
        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

# Function for More Challenges
def More_Challenge():

    # Looping If There is an Error
    while True:

        try:
                        
            # Asking User If he wants more Challenges
            print("\nDo you want more Challenges?")
            print("1. Yes")
            print("2. No")
            
            # Input for More Challenge
            more_challenege= int(input("\nEnter the Number: "))

            if more_challenege == 1:
                Challenge()
                break

            elif more_challenege == 2:
                Loop_Program()
                break

            else:
                print("\nInvalid Choice")
                continue

        # If Value Error Occurs
        except ValueError:
            print("\nPlease Write a Valid Integer")

            # Running More Challenge Function
            More_Challenge()
            break

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")
        
        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}\n")

# Function for Giving Challenges
def Challenge():
    
    # Making of Fitness Challenge File
    Fitness_Folder= os.path.join(base_dir, "Fitness Challenge")
    Fitness_Challenge_file= os.path.join(Fitness_Folder, "Fitness Challenge.txt")
        
    # If There is an Error
    while True:

        # Fetching Exercises In Exercise Folder
        exercise_list = os.listdir(os.path.join(base_dir, "Exercises"))

        # Checking If there are Exercise Available
        if exercise_list:
            exercise_selection = random.choice(exercise_list)
            break

        else:
            
            # If there is an Error
            while True:

                try:
                        
                    print("\nNo Exercises Found. Please Add an Exercise first.")
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

                # If User Keyboard Interrupts
                except KeyboardInterrupt:
                    
                    print("\n\nDo you want to Quit?")
                    print("1. Yes")
                    print("2. No")

                    # Input if User wants to Quit
                    quitting= int(input("\nEnter the Number: "))

                    if quitting == 1:
                        exit()

                    elif quitting == 2:
                        continue

                    else:
                        print("\nInvalid Choice")

    # High Score file Path
    high_score_file= os.path.join(base_dir, Exercises_folder, exercise_selection, "High Score.txt")

    # Current time
    current_time = datetime.now().replace(second=0, microsecond=0)
        
    # Generate Challenge Time within a Week
    max_days = 10
    challenge_time = current_time + timedelta(days=random.randint(1, max_days))

    # Checking If High Score File Exists
    if os.path.exists(high_score_file):

            # Reading High Score Files
            with open(high_score_file, 'r') as h:
                challenge_highscore= h.readlines()

            # Checking Length of Challenge High Score
            if len(challenge_highscore) > 2:

                try:
                    High_Score_Sets= int(challenge_highscore[1].strip().split(": ")[1])
                    High_Score_Weight= int(challenge_highscore[2].strip().split(": ")[1])

                # If Value Error Occurs
                except ValueError:
                    print("\nInvalid Data format for High Score")

    else:
        High_Score_Weight= 200
        High_Score_Sets= 15
        
    # Generate Weight
    weight = random.randint(20, High_Score_Weight)
        
    # Generate Sets
    sets = random.randint(1, High_Score_Sets)

    # Writing Data into Fitness Challenge
    with open(Fitness_Challenge_file, 'w') as d:
        d.write("Fitness Challenge Details:\n\n")
        d.write(f"Challenge Exercise: {exercise_selection}\n")
        d.write(f"Challenge Time: {challenge_time.strftime('%m-%d-%Y %H:%M')}\n")
        d.write(f"Weight: {weight} KGs\n")
        d.write(f"Sets: {sets}\n")
        d.write(f"Challenge Status: Incomplete")

    # Print Challenge Details
    print("\nFitness Challenge Details:")
    print(f"Challenge Exercise: {exercise_selection}")
    print(f"Challenge Time: {challenge_time.strftime('%m-%d-%Y %H:%M')}")
    print(f"Weight: {weight} KGs")
    print(f"Sets: {sets}")
    print("Challenge Status: Incomplete")

    # Looping If There is an Error
    while True:

        try:
            print("\nDo you Want to Change the Challenge?")
            print("1. Yes")
            print("2. No")
                
            # Input If User want to Change the Challenge
            change_challenge= int(input("\nEnter the Number: "))

            if change_challenge == 1:
                Challenge()
                break
            elif change_challenge == 2:
                Loop_Program()
                break
            else:
                print("\nInvalid Choice")
                continue

        # If Value Error Occurs
        except ValueError:
            print("\nPlease Enter a Valid Integer")

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")
        
        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

# Prioritize Exercise Function
def Prioritize():

    # Making of Priority Exercise file
    Priority_Folder= os.path.join(base_dir, "Prioritized Exercise")

    if not os.path.exists(Priority_Folder):
        os.makedirs(Priority_Folder)

    Priority_file= os.path.join(Priority_Folder, "Priority Exercise.txt")

    # Looping if there is an Error
    while True:
        try:

            print("\nWhat you want to do?")
            print("1. Set Priority Exercise")
            print("2. Display Priority Exercise\n")

            # Input of What User want to Do
            priority_choice= int(input("Tell the Number: "))

            if priority_choice== 1:

                exercise_name= exercise_menu()
                
                # Making of Particular Exercise Folder
                Exercise_folder= os.path.join(Exercises_folder, exercise_name)

                # HighScore File Path
                high_score_file = os.path.join(Exercise_folder, "High Score.txt")

                # Exercise Diet File
                Exercise_diet= os.path.join(Exercise_folder, "Diet Plan.txt")

                # Exercise Goal File
                goal_file= os.path.join(Exercise_folder, "Goals.txt")
            
                if exercise_name:

                    try:    
                        with open(high_score_file, 'r') as t:
                            high_score_data= t.read()
    
                        with open(Exercise_diet, 'r') as r:
                            Diet_data= r.read()

                        with open(goal_file, 'r') as e:
                            goal_data= e.read()

                    # If File Not Found Error Occurs
                    except FileNotFoundError:
                        print(f"\nPLease Set Data for each of the components: 'Goal, High_Score, Diet Plan'")

                    # If any other Error Occurs
                    except Exception as e:
                        print("\nPlease set the Data for: ")

                try:
                    with open(Priority_file,'w') as q:
                        q.write(f"Priority Exercise: {exercise_name}\n\n")
                        q.write(f"High Score Data: {high_score_data}\n")
                        q.write(f"Diet Data: {Diet_data}\n")
                        q.write(f"Goal Data: {goal_data}\n")

                        print(f"\nPriority Exercise: {exercise_name}\n\n")
                        print(f"High Score Data:\n{high_score_data}")
                        print(f"Diet Data:\n{Diet_data}")
                        print(f"Goal Data:\n{goal_data}\n")
                        print(f"{exercise_name} is set as Priority Exercise")
                        break

                # If any other Error Occurs
                except Exception as e:
                    ("\nPlease Set Data First")

            elif priority_choice== 2:

                try:
                    with open(Priority_file, 'r') as r:
                        priority_data= r.read()

                    print(priority_data.strip())
                    break

                except FileNotFoundError:
                    print("\nNo Such File Exists")

            else:
                print("\nInvalid Choice")
                continue

        # If Value Error Occurs
        except ValueError:
            print("\nError: Please Enter a Valid Integer")

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")
        
        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

# Function for Adding Exercises
def Add_New_exercise():

    # Looping if ther is an Error
    while True:
        try:

            # Takim Input of Exercise Name
            exercise_name= input("\nEnter the Name of the New Exercise: ").strip()

            # Making sure exercise_name is valid
            if exercise_name.isalpha() and exercise_name:
                    
                # Making a Folder for the New Exercise
                Exercise_folder = os.path.join(Exercises_folder, exercise_name)
                os.makedirs(Exercise_folder, exist_ok=True)
                break
        
        # If User Keyboard Interrupts
        except KeyboardInterrupt:
                
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")

        # If any Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

# Function for Deleteing Exercises
def Delete_Exercise():

    while True:

        try:

            print("Deleting an Exercisse")

            # Input for Exercise Name
            exercise_name= input("\nEnter the Name of the Exercise: ").strip()

            # Path to Exercise Folder
            Exercise_folder = os.path.join(Exercises_folder, exercise_name)

            # Checking and Removing Exercise
            if os.path.exists(Exercise_folder):
                shutil.rmtree(Exercise_folder)
                print("\nThe Exercise has been removed!")
            else:
                print("\nNo such Exercise Exists")

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")
        
        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

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

            # Running the function Loop Program
            Loop_Program()

        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")

        # If Any Error Other than Value Error Occurs
        except Exception as e:
            print(f"\nAn Error occurred while performing the action: {e}")

# Function for Looping the Program
def Loop_Program():

    # Looping If There an Error 
    while True:

        print("\nDo you want to Exit or Continue?")
        print("1. Continue")
        print("2. Exit\n")

        try:

            # Taking Input of User
            cont = int(input("Select a Number: "))
            if cont == 2:
                print("\nExiting Fitness Flow. Goodbye!\n")
                exit()

            elif cont == 1:

                # Running Main Menu Function
                main_menu()

            else:
                print("\nError: Please Enter 1 to Continue or 2 to Exit.")
        
        # If Value Error Occurs
        except ValueError:
            print("\nError: Please Enter a Valid Number.")
        
        # If User Keyboard Interrupts
        except KeyboardInterrupt:
            
            print("\n\nDo you want to Quit?")
            print("1. Yes")
            print("2. No")

            # Input if User wants to Quit
            quitting= int(input("\nEnter the Number: "))

            if quitting == 1:
                exit()

            elif quitting == 2:
                continue

            else:
                print("\nInvalid Choice")

        # If Any other Error Occurs
        except Exception as e:
            print(f"\nAn Error Occured while performing the action: {e}")

# Function for Main Menu
def main_menu():

    # Making of Priority Exercise file
    Priority_Folder= os.path.join(base_dir, "Prioritized Exercise")
    Priority_file= os.path.join(Priority_Folder, "Priority Exercise.txt")

    try:
        print("\nFitness Flow")

        if os.path.exists(Priority_file):
            with open(Priority_file, 'r') as x:
                data= x.read()
            print(f"\nYour Priority Exercise Data:\n{data.strip()}")

        # Looping if any Errors Occurs
        while True:

            try:
                # Printing actions that can be performed
                print("\nWhat would you like to do?")
                print("1. Track Workout")
                print("2. Prioritize Exercise")
                print("3. Fitness Challenge")
                print("\n    ==SYSTEM==")
                print("4. Add new Exercise")
                print("5. Delete a Exercise")

                # Input of Action that User wants to perform
                main_choice = int(input("\nEnter the number of what you want to do: "))

                # Running and calling functions based on user choice
                if main_choice == 1:
                    exercise_name = exercise_menu()
                    if exercise_name:

                        # Running Perfform Action function
                        perform_action(exercise_name)

                elif main_choice == 2:

                    # Running Prioritize Exercise function
                    Prioritize()

                elif main_choice == 3:
                    
                    # Runninf Fitness Challenge Function
                    Fitness_Challenge()

                elif main_choice == 4:
                    
                    # Running Add New Exercise Function
                    Add_New_exercise()
                elif main_choice== 5:

                    # Running Delete Exercise function
                    Delete_Exercise()

                else:
                    print("\nInvalid Choice")
                    continue

                # Running the function Loop Program
                Loop_Program()

            # If Value Error Occurs
            except ValueError:
                print("\nError: Please Enter a Valid Number")
                continue
        
            # If User Keyboard Interrupts
            except KeyboardInterrupt:
                
                print("\n\nDo you want to Quit?")
                print("1. Yes")
                print("2. No")

                # Input if User wants to Quit
                quitting= int(input("\nEnter the Number: "))

                if quitting == 1:
                 exit()

                elif quitting == 2:
                    continue

                else:
                    print("\nInvalid Choice")

            # If Any other Error Occurs
            except Exception as e:
                print(f"\nAn Error Occured while performing the action: {e}")

    # If any Error Other than Value Error Occurs
    except Exception as e:
        print(f"\nAn Error occurred while performing the action: {e}")

# Running Main Menu Function
main_menu()