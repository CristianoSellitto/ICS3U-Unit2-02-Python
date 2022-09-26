#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in September 2022
# A program that finds the area and perimeter for a circle, using user inputted varibles

import math


def main():
    # Finds the area and perimeter of a circle with a radius inputted by the user

    radius_of_circle = int(input("Enter the radius of the circle (mm): "))
    area_of_circle = math.pi * radius_of_circle**2
    perimeter_of_circle = 2 * math.pi * radius_of_circle
    print("\nThis circle's area is {}mm²".format(area_of_circle))
    print("This circle's perimeter is {}mm".format(perimeter_of_circle))

    print("\nDone.")


if __name__ == "__main__":
    main()
