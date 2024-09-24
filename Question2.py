#1st function
def first(hour):
    return 3.0
#2nd function
def second(hour):
    return (hour-3)*0.50
#3rd function
def third(hour):
    return 12.0
rate = 0
total = 0
for i in range(5):
    while True:
        hour = float(input("Number of Hours: "))
        if (hour <= 3):
            rate = first(hour)
            print(f"Parking charge: RM{rate:.2f}")
            break
        elif (hour <= 20):
            rate = second(hour) + 3
            print(f"Parking charge: RM{rate:.2f}")
            break
        elif (hour <= 24):
            rate = third(hour)
            print(f"Parking charge: RM{rate:.2f}")
            break
        else:
            print("Invalid input. Limit is 24 hours. Try again!")

    total = total + rate

print(f"Total parking charge for the day: RM{total:.2f}")
