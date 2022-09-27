#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in September 2022
# A program that finds the area and perimeter of a rectangle, using user inputted variables

import math


def main():
    # Finds the area and perimeter of a rectangle with width and length inputted by the user

    length_of_rectangle = int(input("Enter the length of the rectangle (mm): "))
    width_of_rectangle = int(input("Enter the width of the rectangle (mm): "))
    area_of_rectangle = length_of_rectangle * width_of_rectangle
    perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)
    print("\nThis rectangle's area is {}mm²".format(area_of_rectangle))
    print("This rectangle's perimeter is {}mm".format(perimeter_of_rectangle))

    print("\nDone.")


if __name__ == "__main__":
    main()
