
def divby5(a):
    if a % 5 == 0:
        return True
    else:
        return False

def divby7(a):

        if a % 7 == 0:
            return True
        else:
            return False


def divby9(a):
    if a % 9 == 0:
        return True
    else:
        return False

def divby11(a):
    if a % 11 ==0:
        return True
    else:
        return False

if __name__== "__main__":
    n1 = int(input("enter the number:"))
    print(divby5(n1))
    print(divby7(n1))
    print(divby9(n1))
    print(divby11(n1))


