"""
Java Variables or in static typed programming languages:
    String varNam = data


Python Variables or in dynamicly typed progreamming languages:
    varName = data

"""

name_of_student = "Elena"

print(name_of_student)
print(type(name_of_student))

name_of_student = 3.5

print(name_of_student)
print(type(name_of_student))

name_of_student = True

print(name_of_student)
print(type(name_of_student))

s = '35'

num = int(s)

print(num)
print(type(num))

print("-------------------------------------")

prog_language = "python"
version = 3.13

print("My programming language is {} programming language and the version is {}".format(prog_language, version))

print(f"My programming language is {prog_language} programming language and the version is {version}")


# print("My programming language is " + prog_language + 3.13)


print("---------------")

str1 = "python programming"

print("python" in str1)

print(True and True) # &&

print(False or True) # ||

s1 = "Java"
s2 = "Java"

print(s1 is s2) # used for checking if two reference variables are referencing to same objects (== operator of java)


"""
String s1 = "Java";
String s2 = "Java";

String s3 = new String("Java);

s1 == s2  ===> true
s1 == s3  ===> false
"""


