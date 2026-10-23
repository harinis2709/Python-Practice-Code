age = int(input("Enter your age: "))
day = input("weekend or weekday: ")
show = input("Enter the show type: ")
if age < 12:
    ticket = "Child ticket"
    if day == "weekend":
        price = 8
    else:
        price = 6
elif age <= 59:
    ticket = "Adult ticket"
    if show == "premium":
        price = 15
    else:
        price = 12
else:
    ticket = "Senior ticket"
    price = 7
print(ticket)
print("$", price)                        