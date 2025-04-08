n = "Automation Testing"

print(n[0])
print(n[-1])
# print(n[len(n) - 1])
print(len(n))

n = n.lower()

print(n)

print("---------------------------------")

s = "Python Programming Language"

s1 = s[7:]

print(s1)

s2 = s[:18]
print(s2)

reversed_str = s[::-1]
print(reversed_str)


reversed_str2 = ''.join(reversed(s))
print(reversed_str2)

print("---------------------------------")

expected_title = "cydeo"
actual_title = "CYDEO"

print(expected_title.lower() == actual_title.lower())

