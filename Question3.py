tut = 0
#salary finding function
def salary(sale):
    return 100+(sale*0.15)

while (tut!=-1):
    while True:
        try:
            sale = float(input("Enter sales (-1 to end): RM"))
            break
        except:
            print("Invalid Value!! Try again")
    if(sale!=-1):
       print(f"Salary is RM{salary(sale):.2f}")
    tut = sale