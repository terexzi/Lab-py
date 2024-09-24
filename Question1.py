print("\nStart of Program")
print("User Management")
print("----------------")
print("1. Add new record")
print("2. View all record")
print("3. Search record")
print("4. Exit")

#Add New Record Function
def add_record(name, email):
    file = open("user_management.txt", "a")
    file.write(f"{name}, {email}\n")
    file.close()
    return "Record added."

#View All Records Function
def view_record():
    file = open("user_management.txt", "r")
    for line in file:
        print(line.strip())
    file.close()

#Search Record Function
def search_record(value):
    file = open("user_management.txt", "r")
    for line in file:
        if line.startswith(value):
            return line

while True:
    try:
        while True:
            selection = int(input("\nSelect your option:"))
            match selection:
               case 1:
                   name = input("Please enter your name:")
                   email = input("Please enter your email address:")
                   print(f"{add_record(name, email)}")
                   continue
               case 2:
                   # calling the view_record function
                   view_record()
                   continue
               case 3:
                   value = input("Enter name to search record :")
                   print(f"{search_record(value)}")
                   continue
               case 4:
                   break

               case _:
                   print("Wrong number! Try again")
        break

    except(ValueError):
        print("Invalid Input, try again!!")


