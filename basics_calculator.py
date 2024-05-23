import math

def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def basic():
    print("function calculator(1)")
    print("Surface area of basic shapes(2)")
    print("volume of basic shapes(3)\n")
    user_option = "a"
    while not isint(user_option):
        user_option = input("Enter the number corresponding to what you want to calculate: ")
        if user_option.lower() == "exit":
            return None
        if not isint(user_option):
            print("Invalid Input")
            continue
        while 0 > int(user_option) or int(user_option) > 3:
            user_option = input("Enter the number of the user_option of the surface area you want to calculate: ")
            if user_option.lower() == "exit":
                return None
            if 0 > int(user_option) or int(user_option) > 3:
                print("Invalid Input")
    user_option = int(user_option)
    fn, sn, op = "a", "a", "a"
    if user_option == 1:
        a = 0
        while not isfloat(fn):
            fn = input("Enter the first number: ")
            if fn.lower() == "exit":
                return None
            elif not isfloat(fn):
                print("Invalid Input")
        while op != "+" and op != "-" and op != "*" and op != "/":
            op = input("Enter operation(+, -, *, /): ")
            if op.lower() == "exit":
                return None
            elif op != "+" and op != "-" and op != "*" and op != "/":
                print("Invalid Input")
        while not isfloat(sn):
            sn = input("Enter the second number: ")
            if sn.lower() == "exit":
                return None
            elif not isfloat(sn):
                print("Invalid Input")
        fn = float(fn)
        sn = float(sn)
        if op == "+":
            a = fn + sn
        elif op == "-":
            a = fn - sn
        elif op == "*":
            a = fn * sn
        elif op == "/":
            a = fn / sn
        print("The answer is", a)
        return None
# function calculator
    elif user_option == 2:
        a = 0
        print("Square/rectangle(1)\ncylinder(2)\nsphere(3)")
        shape = "j"
        while not isint(shape):
            shape = input("Enter the number of the shape of the surface area you want to calculate: ")
            if shape.lower() == "exit":
                return None
            elif not isint(shape):
                print("Invalid Input")
                continue
            while 0 > int(shape) or int(shape) > 3:
                shape = input("Enter the number of the shape of the surface area you want to calculate: ")
                if shape.lower() == "exit":
                    return None
                elif 0 > int(shape) or int(shape) > 3:
                    print("Invalid Input")
        shape = int(shape)
        if shape == 1:
            x, y, z = "a", "b", "c"
            while not isint(x) and not isint(y) and not isint(z):
                x = input("Enter height: ")
                if x.lower() == "exit":
                    return None
                elif not isint(x):
                    print("Invalid Input")
                y = input("Enter width: ")
                if y.lower() == "exit":
                    return None
                elif not isint(y):
                    print("Invalid Input")
                z = input("Enter length: ")
                if z.lower() == "exit":
                    return None
                elif not isint(z):
                    print("Invalid Input")
            x, y, z = int(x), int(y), int(z)
            if x == y == z:
                a = x * x * 6
            else:
                a = (x * z + x * y + y * z) * 2
        if shape == 2:
            x, y = "a", "b"
            while not isint(x) and not isint(y):
                x = input("Enter height: ")
                if x.lower() == "exit":
                    return None
                elif not isint(x):
                    print("Invalid Input")
                y = input("Enter radius of the circle: ")
                if y.lower() == "exit":
                    return None
                elif not isint(y):
                    print("Invalid Input")
            x, y = int(x), int(y)
            a = (2 * math.pi * y * x) + (2 * math.pi * (y ** 2))
        if shape == 3:
            x = "a"
            while not isint(x):
                x = input("Enter radius of the sphere: ")
                if not isint(x):
                    print("Invalid Input")
                elif x.lower() == "exit":
                    return None
            x = int(x)
            a = 4 * math.pi * (x ** 2)
        print("The answer is", a)
        return None
# Surface Area
    elif user_option == 3:
        a = 0
        print("Square/rectangle(1)\ncylinder(2)\nsphere(3)")
        shape = "j"
        while not isint(shape):
            shape = input("Enter the number of the volume shape you want to calculate: \n")
            if shape.lower() == "exit":
                return None
            elif not isint(shape):
                print("Invalid Input")
                continue
            while 0 > int(shape) or int(shape) > 3:
                shape = input("Enter the number of the volume shape you want to calculate: ")
                if shape.lower() == "exit":
                    return None
                elif 0 > int(shape) or int(shape) > 3:
                    print("Invalid Input")
        shape = int(shape)
        if shape == 1:
            x, y, z = "a", "b", "c"
            while not isint(x) and not isint(y) and not isint(z):
                x = input("Enter height: ")
                if x.lower() == "exit":
                    return None
                elif not isint(x):
                    print("Invalid Input")
                y = input("Enter width: ")
                if x.lower() == "exit":
                    return None
                elif not isint(y):
                    print("Invalid Input")
                z = input("Enter length: ")
                if x.lower() == "exit":
                    return None
                elif not isint(z):
                    print("Invalid Input")
            x, y, z = int(x), int(y), int(z)
            if x == y == z:
                a = x ** 3
            else:
                a = x * y * z
        if shape == 2:
            x, y = "a", "b"
            while not isint(x) and not isint(y):
                x = input("Enter height: ")
                if x.lower() == "exit":
                    return None
                elif not isint(x):
                    print("Invalid Input")
                y = input("Enter radius of the circle: ")
                if x.lower() == "exit":
                    return None
                elif not isint(y):
                    print("Invalid Input")
            x, y = int(x), int(y)
            a = math.pi * x * (y ** 2)
        if shape == 3:
            x = "a"
            while not isint(x):
                x = input("Enter radius of the sphere: ")
                if x.lower() == "exit":
                    return None
                elif not isint(x):
                    print("Invalid Input")
            x = int(x)
            a = (4/3) * math.pi * (x ** 3)
        print("The answer is", round(a, 2))
        return None