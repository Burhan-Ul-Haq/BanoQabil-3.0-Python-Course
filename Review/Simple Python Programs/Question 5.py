Number_List= []
Number_Input= (input("Tell Your Number: "))
for Number in Number_Input:
    Number_List.append(Number)

Number_List[0], Number_List [1]= Number_List[1], Number_List[0]
reversed= ''.join(Number_List)   
print(reversed)