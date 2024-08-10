Odd= []
Even= []

Number= int(input("Tell Your Number: "))
if Number%2 == 0:
    Even.append(Number)
else:
    Odd.append(Number)
print(Even)
print(Odd)