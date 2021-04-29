#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 29 April 2021
# This program adds two numbers together


def main():
    # this function adds two numbers together

    # input
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    # process
    sum = num1 + num2
    print("")

    # output
    print('The answer to {0} + {1} is {2}'.format(num1, num2, sum))


if __name__ == "__main__":
    main()
