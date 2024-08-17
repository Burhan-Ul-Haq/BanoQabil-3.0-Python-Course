import os
from datetime import datetime

base_dir = r"C:\Users\PMLS\Desktop\Burhan\Programming\Python\Fitness Flow"

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

Exercises_folder = os.path.join(base_dir, "Exercises")

if not os.path.exists(Exercises_folder):
    os.makedirs(Exercises_folder)

def exercise(name):

    Exercise_folder = os.path.join(Exercises_folder, name)
    if not os.path.exists(Exercise_folder):
        os.makedirs(Exercise_folder)

    High_Score_Weight = 0
    High_Score_Sets = 0

    weight = int(input(f"Tell How Much Weight Have you Pulled for {name} (KGs): "))

    sets = int(input(f"Tell How Many Sets Have you Taken for {name}: "))

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

    log_file = os.path.join(Exercise_folder, f"{name} log.txt")
    high_score_file = os.path.join(Exercise_folder, "High Score.txt")

    with open(log_file, 'a') as f:
        f.write(f"Date: {current_time}\nWeight: {weight} KGs\nSets: {sets}\n\n")

    if weight > High_Score_Weight:
        High_Score_Weight = weight

    if sets > High_Score_Sets:
        High_Score_Sets = sets

    with open(high_score_file, 'w') as g:
        g.write(f"Date: {current_time}\nHigh Score:\nWeight: {High_Score_Weight} KGs\nSets: {High_Score_Sets}\n")

    print(f"{name}:\nDate: {current_time}\nWeight: {weight} KGs\nSets: {sets}\nHigh Score:\nWeight: {High_Score_Weight} KGs\nSets: {High_Score_Sets}")

exercise_name = input("Tell your Exercise Name: ")
exercise(exercise_name)
