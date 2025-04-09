browsers = ("Chrome", "Safari", "Firefox", "Internet Explore", "Edge")

print(browsers)
print(type(browsers))
print(len(browsers))

print(browsers[1])
print(browsers[-2])

a1 = browsers[1:-1]
print(a1)

a2 = browsers[2:]
print(a2)

a3 = browsers[:-2]
print(a3)

reversed_tuple = browsers[::-1]
print(reversed_tuple)

result = tuple(reversed(browsers))
print(result)

print("--------------------")

for each in browsers:
    print(each)

print("--------------------")

# browsers[1] = "CYDEO"

# print(browsers)

print("--------------------")

group_scores = ((70, 65, 80), (55, 85, 70), (68, 78, 48))

print(group_scores)

for i in group_scores:
    # print(i)
    for j in i:
        print(j)
        # break

print("--------------------")

t1 = (1, 2, 3, 4,5)
t2 = (6, 7, 8, 9, 10, 11, 12)
t3 = (13, 14, 15, 16)

merged_tuples = t1 + t2 + t3

print(merged_tuples)