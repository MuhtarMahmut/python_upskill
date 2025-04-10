try:
    x = 100 / 0
    print(x)
except Exception:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("Finally block")

print("test completed")

print("-------------------------")

try:

    raise IndexError()

except ArithmeticError:
    print("Exception is ArithmeticError")

except OSError:
    print("Exception is OSError")

except SyntaxError:
    print("Exception is SyntaxError")

except Exception:
    print("Different Exception")

print("-------------------------")

raise Exception("Program is now terminated")