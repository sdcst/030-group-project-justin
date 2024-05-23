#!python3
# Volume Calculator
# Feel free to rename your variables
from check import *
from finance import *
from basics_calculator import *
from tictactoe import *
from title import *
from instruction import *


def main():
    counter = 0
    title()
    instructions()
    options = "a"
    while options != "exit":
        options = "a"
        print()
        if counter != 0:
            title()
        while not isint(options) or int(options) < 0 or int(options) > 3:
            options = input("Enter the number corresponding to which function you want to try: \n")
            if options.lower() == "exit":
                quit()
            elif not isint(options):
                print("Invalid Input\n")
                continue
            elif int(options) < 0 or int(options) > 3:
                print("Invalid Input\n")
        if options == "1":
            basic()
        elif options == "2":
            finance()
        elif options == "3":
            games()
        pass
        counter += 1


if __name__ == "__main__":
    main()
