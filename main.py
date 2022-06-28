
# sum
def suma(a, b):
    c = a + b
    return c


# rest
def rest(a, b):
    print(a - b)


# multi
def mult(a, b):
    print(a * b)


# div
def div(a, b):
    print(a / b)


# Menu
i = 0
while i < 2:
    op = input("Which operation? ")
    if op == "suma":
        a = int(input("tell me first number: "))
        b = int(input("tell me second number: "))
        result = suma(a, b)
        print(result)
    elif op == "resta":
        print("2")
    elif op == "mult":
        print("3")
    elif op == "exit":
        i = 2
        print("Bye")
    else:
        print("error")
        i += 1
        if i == 2:
            print("fuck you, bye")
