#store many things
from bmi import height

ages = [21,72,45,97,34,34,12,23,39,13] #list

names = ["Habu", "Zack", "Aisha","Habu", "Yaga"]

# function
# ages.append(31)
# ages.clear()
# ages.sort()
# ages.reverse()
# print(ages)

# names.sort()
# print(names)

# habu_count = names.count("Habu")
# print(habu_count)
# print(len(names))
# print(len(ages))

# print(sum(ages)/len(ages))

# #retrieve an element
# print(ages[0])
# print(ages[5]) #index

# print(names[0])

# print(names[-1]) #started for the other end
# print(names[-2])
# print(names[-3:]) #slicing from -3 to the end

# print(ages[3:])
# print(ages[3:5]) #slicing

# print(ages[:3])

# set - to remove duplicates(has no duplicates)
scores = {88,49,84,88,34,74}
print(scores)
scores.add(90)
scores.remove(34)

# tuple - once created, you cannot add more elements
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays[0])

# dictionary
person = {"name": "Jason", "age":22, "weight":52, height:1.88}
print(person["name"])
print(person["age"])

people = [
    {"name": "Aria", "age":29},
    {"name": "Jaco", "age":28},
    {"name": "Hellen", "age":23}
]

print(people[0]["age"])
