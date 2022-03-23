# print("Daniela")
# print("*" * 10)

# name = input("What is your name?" )
# print("Hello " + name)
# color = input("What is your favourite color? ")
# print(name + " likes " + color)

# birth_year = input("Year of birth ")
# age = 2022 - int(birth_year)
# print("Your age is " + str(age))

# weight_pounds = input("Enter your weight in pounds ")
# weight_kilos = float(weight_pounds) * 0.4536
# print(weight_kilos)

# good_credit = True

# if good_credit:
#    print("Put down 100000 usd")
# else:
#     print("Put down 200000 usd")

#weight = input("Enter your weight ")
#unit = input("(L)bs or (K)g: ")

#if unit.upper() == "L":
#    w_k = float(weight) * 0.4536
#    print(f"Weight in kilos is {w_k}")
#else:
#    w_k = float(weight) * 2.20
#    print(f"Weight in pounds is {w_k}")

number_guess = 9
in_count = 0
number_count = 3
#while in_count < number_count:
#    in_count += 1
#    guess = int(input("Enter your guess "))
#    if guess == number_guess:
#        print("You won!")
#        break
#else:
#    print("You lost")

command = ""

while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print("start - to start the car, stop, to stop the car, quit - to exit")
    elif command == "start":
        print("Ready to go")
    elif command == "stop":
        print("Car stopped")
    elif command != "quit":
        print("Do not understand")



