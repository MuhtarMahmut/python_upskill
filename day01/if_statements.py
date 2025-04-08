browser_name = "firefox"

if browser_name == "chrome":
    print("Chrome Browser is Selected")
    print("Opening Chrome Browser...")
elif browser_name == "firefox":
    print("Firefox Browser is Selected")
    print("Opening Firefox Browser...")
else:
    print("Safari Browser is Selected")
    print("Opening Safari Browser...")

print("-----------------------------------------")

score = -200

if 0 <= score <= 100:

    if score >= 60:
        print("Passed the exam")
    else:
        print("Failed the exam")

else:
    print("Failed the exam")

print("-----------------------------------------")

if True:
    pass
else:
    pass


def function_name():
    print("This is a function")
    pass


class Animal:
    pass


