while True:


    operator = input("Enter an operator [+, -, *, /]:  ")
    num_1 = (input("Enter number 1: "))
    num_2 = (input("Enter number 2: "))

    try:
        num_1 = int(num_1)
        num_2 = int(num_2)

        if operator == "+":
            print(num_1 + num_2)

        elif operator == "-":
            print(num_1 - num_2)

        elif operator == "*":
            print(num_1 * num_2)

        elif operator == "/":
            print(num_1 / num_2)

        else:
            print("operation not supported.")


    except (ValueError, TypeError,):
        print("Your have to use a number.")

    except ZeroDivisionError:
        print("Your can't divide a number by 0.")


    more = input("Continue [y/n] ")
    if more.lower() == "n":
        print("bye")
        break