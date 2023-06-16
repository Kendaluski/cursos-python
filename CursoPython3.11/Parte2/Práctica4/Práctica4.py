#Python strings

string = "test {}"
intest = 10
names = """Chema
juan
ana
"""

# Work with strings

# for i in string:
#     print(i)

# print("String Length:", len(string))
# print(names,"String Length:", len(names))

# Cut string

# print(string[0])
# print(string[1:3])
# print(string[3])

# String methos: upper(), lower(), replace(), format()

print(string.upper())
print(string.lower())
print(string.replace("t","a"))
print(string.format(intest))