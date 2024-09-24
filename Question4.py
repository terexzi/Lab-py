while True:
    try:
        while True:
            num = int(input("Enter a number between 1 and 9999: "))
            if (1 <= num <= 9999):

                def reverse(num):
                    re = 0
                    while (num > 0):
                        a = num % 10
                        re = (re * 10) + a
                        num = num // 10
                    return re


                print(f"The number with its digits reversed is: {reverse(num)}")
                break
            else:
                print("The number is not between 1 & 9999. Try again!")
        break
    except(ValueError):
        print("Invalid input. Try again!")


