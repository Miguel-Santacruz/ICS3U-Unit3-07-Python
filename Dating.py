#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Apr 2022
# This program is a compoun boolean expression program

import random


def main():
    # This function decides if you have an appropiate age

    # input
    string = input("Enter your age please: ")

    # process & output
    print("")
    try:
        age = int(string)
        if age > 25 and age < 40:
            print("You are an acceptable age :D")
        else:
            print("You are NOT an acceptable age, get out! >:(")
    except Exception:
        print("{} is not an age. Are you okay?".format(string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
