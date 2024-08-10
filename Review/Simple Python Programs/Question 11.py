Start_Range= int(input("Tell the Start Of Range: "))
End_Range= int(input("Tell the End Range Number: "))

Numbers= []
for i in range(Start_Range, End_Range+1):
    Numbers.append(i)

for Number in Numbers:
    if Number%2 != 0:
        print(f"Odd: {Number}")