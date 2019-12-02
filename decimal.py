#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: December 2019
# This program rounds decimal places


def rounding(number, decimal_point):
    # This function rounds the inputted number

    # Process
    rounded_number = (number[0]*(10**decimal_point))
    rounded_number = rounded_number + 0.5
    rounded_number = int(rounded_number)
    rounded_number = rounded_number/(10**decimal_point)

    return rounded_number


def main():
    # This function takes the inputted number then outputs the number rounded
    rounding_number = []

    # Input
    while True:
        user_number = input("Enter a number to be rounded: ")
        decimal_place = input("Enter the how many decimal places you want: ")
        print("")

        try:
            user_number = float(user_number)
            decimal_place = int(decimal_place)
            rounding_number.append(user_number)
            if user_number == float(user_number) and \
               decimal_place == int(decimal_place):
                user_rounded_number = rounding(rounding_number, decimal_place)
                print("")
                print("Your rounded number is", user_rounded_number)
                break
            else:
                print("Error! Try again.")
        except Exception:
            print("Error! Try again.")
            print("")


if __name__ == "__main__":
    main()
