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


def finance():
    ii = "a"
    while not isint(ii):
        ii = input("Is the interest simple interest(1) or compound interest(2)? ")
        if ii.lower() == "exit":
            return None
        elif not isint(ii):
            print("Invalid Input\n")
            continue
        while int(ii) < 0 or int(ii) > 2:
            ii = input("Is the interest simple interest(1) or compound interest(2)? \n")
            if ii.lower() == "exit":
                return None
            elif int(ii) < 0 or int(ii) > 2:
                print("Invalid Input\n")
    ii = int(ii)
    if ii == 1:
        p, r, t = "a", "b", "c"
        while not isfloat(p):
            p = input("initial amount you currently have: ")
            if p.lower() == "exit":
                return None
            elif not isfloat(p):
                print("Invalid Input\n")
        while not isfloat(r):
            r = input("annual interest rate(in decimals): ")
            if r.lower() == "exit":
                return None
            elif not isfloat(r):
                print("Invalid Input\n")
        while not isfloat(t):
            t = input("how many years after you want to know: ")
            if t.lower() == "exit":
                return None
            elif not isfloat(t):
                print("Invalid Input\n")
        p, r, t = float(p), float(r), float(t)
        i = p * r * t
        a = p * (1 + (r * t))
        print(f"You'll have ${str(a)} after {str(t)} years and you've made ${str(i)} amount of interests")
        return None
    if ii == 2:
        p, r, n, t = "a", "b", "c", "d"
        while not isfloat(p):
            p = input("initial amount you currently have: ")
            if p.lower() == "exit":
                return None
            elif not isfloat(p):
                print("Invalid Input\n")
        while not isfloat(r):
            r = input("interest rate(in decimals): ")
            if r.lower() == "exit":
                return None
            elif not isfloat(r):
                print("Invalid Input\n")
        while not isfloat(n):
            n = input("number of times interest is compounded per year: ")
            if n.lower() == "exit":
                return None
            elif not isfloat(n):
                print("Invalid Input\n")
        while not isfloat(t):
            t = input("how many years after you want to know: ")
            if t.lower() == "exit":
                return None
            elif not isfloat(t):
                print("Invalid Input\n")
        p, r, n, t = float(p), float(r), float(n), float(t)
        i = round(p * (((1+(r/t))**(t*n))-1), 2)
        a = round(p * ((1+(r/t))**(n*t)), 2)
        print(f"You'll have ${str(a)} after {str(t)} years and you've made ${str(i)} amount of interests")
        return None
