# Dictionaries 
names = {1: "chema", 2: "juan", 3: "ana", 4: True, 5: 1}
array = {"nombre" : "chema", "edad" : 21, "substr" : ("test1", 2, 4)}
#print(array)

# Dictionary elements keys(), values(), items()

#print(names[1])
# print(names.keys())
# print(names.values())
# print(names.items())

# Modify dictionary elements update()

# names[3] = "carla"
# print(names)
# names.update({3: "carlos"})
# print(names)

# Add dictionary elements

# names.update({6: "carlos"})
# print(names)

# Delete dictionary elements del(), pop(), clear()

# names.pop(3)
# print(names)

# names.popitem()
# print(names)

# Clear dictionary
# names.clear()
# print(names)

del names[2]
print(names)
