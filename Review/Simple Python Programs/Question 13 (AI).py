Number_input= int(input("Tell the Number: "))

for x in range(2, Number_input+1):
    if Number_input%x ==0:
        print(f"The Smallest Divisor is: {x}")
        break