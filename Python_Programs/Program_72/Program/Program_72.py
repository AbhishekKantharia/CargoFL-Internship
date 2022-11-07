netAmount = 0
while True:
    s = int(input("Enter a Number: "))
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print("The Net Amount is:", netAmount)