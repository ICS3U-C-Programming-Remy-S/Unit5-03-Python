#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Nov 28, 2023
# This program will ask user for their
# level(mark) and display the middle percent
# of the mark


def calc_mark(level):
    # statement for each level
    if level == "4+":
        return 98
    elif level == "4":
        return 91
    elif level == "4-":
        return 83
    elif level == "3+":
        return 78
    elif level == "3":
        return 74
    elif level == "3-":
        return 71
    elif level == "2+":
        return 68
    elif level == "2":
        return 65
    elif level == "2-":
        return 61
    elif level == "1+":
        return 58
    elif level == "1":
        return 54
    elif level == "1-":
        return 51
    elif level == "F":
        return 30
    else:
        return -1


def main():
    # get level and display message to user
    print("This program will ask user for their level(mark)")
    print("and display the middle percent of the mark.")
    user_level_str = input("Please enter your level or mark: ")

    # Call function and store the result
    result = calc_mark(user_level_str)

    # Check if the input is valid
    if result != -1:
        print(f"The middle percentage mark for {user_level_str} is: {result}%")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
