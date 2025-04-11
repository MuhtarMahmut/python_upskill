elements = {0}

print(type(elements))
print(elements)

elements.add(10)
elements.add(10)
elements.add(30)
elements.add(20)
elements.add(10)

print(elements)

elements.remove(10)

print(elements)

elements.pop()

print(elements)

elements.update( [100, 200, 300, 400] )

# print( help(set.update) )

print(elements)

print("-------------------")

s1 = {"Selenium", "Cypress", "Playwright"}
s2 = {"UFT", "Playwright", "Cypress"}

s3 = s2.difference(s1)

print(s3)

print("-------------------")

s4 = s1.intersection(s2)

print(s4)
