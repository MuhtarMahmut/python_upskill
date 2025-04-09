"""
In Java:
    for(int i = 0; i < 5; i++){

    }

"""
for i in range(1, 6):
    print(i)
    #print("Hello")

print("Hello World")

print("--------------------------")

s = "Selenium"

for each in s:
    print(each)

print("--------------------------")

reversed_string = ""

for i in s[::-1]:
    reversed_string += i

print(reversed_string)


print("--------------------------")

for i in range(1, 5):
    for x in range(1, 5):
        print("Hello Selenium")

print("--------------------------")


while True:
    print("Python Programming")
    break


score = int( input("Enter your score:\n") )

while score > 100 or score < 0:
    score = int(input("Please re-enter your score:\n"))


if score >= 0 :
    print("Passed the exam")
else:
    print("Failed the exam")


print("--------------------------")










