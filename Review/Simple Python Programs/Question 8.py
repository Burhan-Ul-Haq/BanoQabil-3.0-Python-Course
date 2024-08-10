Start_Range= int(input("Tell the Start Range: "))
End_Range= int(input("Tell the End Range: "))
Divider= int(input("Tell the Number to Divide by: "))

Numbers= []
for i in range(Start_Range, End_Range+1):
    Numbers.append(i)

for Number in Numbers:
    if Number%Divider == 0:
        print(f"These Number Are Divisible: {Number}")