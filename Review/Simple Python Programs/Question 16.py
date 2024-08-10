Numbers= []
for i in range(1, 51):
    Numbers.append(i)

for Number in Numbers:
    if Number%2 == 0 and Number%3 != 0:
        print(f"These Number Aren't Divisible: {Number}")