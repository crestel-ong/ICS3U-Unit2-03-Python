#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This program solves for the circumfrance of a circle
#    with radius imputed by user

import constants

def main():
    # this function calculates circumfrance

# input 
    radius = int(input("Enter length of the radius (mm): "))
    
# process
    circumfrance = constants.TAU * radius

# output
    print("The circumfrance is {} mm².".format(circumfrance))
    print("\nDone.")


if __name__ == "__main__":
    main()


