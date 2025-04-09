items = ["Pen", "Laptop", "Book", "Camera"]
print(items)
print(type(items))
print(len(items))

items.append("Microphone")

print(items)

items.pop(-2)

print(items)

items.remove("Pen")

print(items)

items.extend(("Eggs", "Apples", "Water"))

print(items)

print("----------------------")

languages = ("Python", "Java", "C#", "Ruby", "JavaScript")

temp_list = list(languages)

temp_list.pop(1)
temp_list.remove("Ruby")
print(temp_list)

languages = tuple(temp_list)

print(languages)

print("----------------------")

for each in items:
    print(each)

print("----------------------")

nums = []

for x in range(1, 31):
    nums.append(x)

print(nums)

divisible_by_three = [p for p in nums if p % 3 == 0]

print(divisible_by_three)
