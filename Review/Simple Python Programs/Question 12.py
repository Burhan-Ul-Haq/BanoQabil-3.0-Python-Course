Number_List= []
Number_Input= input("Tell Your Number: ")

for Number in Number_Input:
    converter= int(Number)
    Number_List.append(converter)

if len(Number_List) < 2:
    print("Please Enter Two Numbers")
else:
    Sum= Number_List [0] + Number_List[1]
    print(f"The Sum of two Digit is: {Sum}")