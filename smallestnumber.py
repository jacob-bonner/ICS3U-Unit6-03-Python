#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program finds the smallest number in an array


import random


def calculate(array_of_numbers):
    # This function finds the smallest number in a list

    # Variables
    small_number = 100

    # Process
    for counter in array_of_numbers:
        if counter < small_number:
            small_number = counter

    # Output
    return small_number


def main():
    # This function creates an array of 10 numbers then prints out the smallest

    # Array
    number_array = []

    # Adding numbers to an array
    for counter in range(10):
        random_number = random.randint(1, 100)
        print(random_number)
        number_array.append(random_number)

    # Process
    smallest_number = calculate(number_array)

    # Output
    print("")
    print("The smallest number in the array is", smallest_number)


if __name__ == "__main__":
    main()
