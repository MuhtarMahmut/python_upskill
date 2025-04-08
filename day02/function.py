import numbers


def return_value():
    # print("This is a function")
    return 1000


print(return_value())


def return_integer() -> int:
    print("This is int function")


return_integer()


# print(return_integer())


def cube(num: int) -> int:
    return num * num * num


print(cube(10))


def addition(num1: numbers, num2: numbers, num3: numbers = 0, num4: numbers = 0) -> numbers:
    return num1 + num2 + num3 + num4


print(addition(100, 15.5))
print(addition(100, 200, 300))
print(addition(100, 200, 300, "400"))


def functions() -> int:
    pass
