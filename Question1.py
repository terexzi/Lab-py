print("\nStart of Program")
print("User record")
print("-----------")
print("1. Add new record")
print("2. View all record")
print("3. Exit")

def add_record(name, email, mark):
    file = open("user_detail.txt", "a")
    file.write(f"{name},{email},{mark}\n")
    file.close()
    return "record added."
def view_all_record ():
    total = 0
    file = open("user_detail.txt", "r")
    for line in file:
        name, email, mark = line.strip().split(",")
        print(f"\nName: {name}\nEmail: {email}\nMark: {mark}")
        total = total + int(mark)
    print(f"\nTotal mark of the students = {total}")
    file.close()


while True:
    try:
        while True:
            selection = int(input("\nSelect your option: "))
            match selection:
                case 1:
                    name = input("Please enter name: ")
                    email = input("Please enter email address: ")
                    mark = input("Please enter mark: ")
                    print(add_record(name, email, mark))
                    info = input("Do you want to add more info? (y/n)")
                    if(info.lower() == "y"):
                        while True:
                            name = input("Please enter name: ")
                            email = input("Please enter email address: ")
                            mark = input("Please enter mark: ")
                            print(add_record(name, email, mark))
                            info = input("Do you want to add more info? (y/n)")
                            if (info.lower() == "n"):
                                break
                case 2:
                    view_all_record()
                case 3:
                    print("Exit!")
                    break
                case _:
                    print("Wrong Input!")
        break

    except(ValueError):
        print("Invalid input!")