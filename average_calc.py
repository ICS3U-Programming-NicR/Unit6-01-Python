#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 2 2022
# display 5 ints in a line

import random
import constants


def average_rand_num():
    total = 0
    array = []
    for counter in range(constants.MAX_ARRAY_SIZE):
        rand_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        array.append(rand_num)
        print("The {} number added is {}".format(counter + 1, array[counter]))
        total = array[counter] + total
    average = total / counter
    return average


def main():
    average_f = average_rand_num()
    print("The average calculated is {}".format(average_f))


if __name__ == "__main__":
    main()
