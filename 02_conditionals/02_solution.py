age = int(input("Enter person age: "))

day = str(input("Enter day: "))

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)