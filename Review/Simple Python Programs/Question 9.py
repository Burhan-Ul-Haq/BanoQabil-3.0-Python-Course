Number_List= []
Number_Input= input("Tell Your Number: ")

for Number in Number_Input:
    converter= int(Number)
    Number_List.append(converter)
    
print(Number_List)
Quotient, Remainder = divmod(Number_List[0], Number_List[1])
print(f"Quotient: {Quotient}")
print(f"Remainder: {Remainder}")