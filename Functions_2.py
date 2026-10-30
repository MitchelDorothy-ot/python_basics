from _ast import arguments

def add(a,b,c):
    res = a + b + c
    return res

def addition(*nums):
    """
    Returns the sum of all the numbers passed as arguments
    Parameters:
     integers of floats or a mix of integers and floats
    Returns:
     Integers or floats
     """

    total = sum(nums)
    return total

addition(8,8,8)

def build_profile(**kwargs): #dict key-word args
    for k, w in kwargs.items():
        print(f"{k} : {w}")

def fancy_function(name,*nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)


# anonymous functions = lamda
# def square(num):
#     return num * num
# result = square(5)
# print(result)

square = lambda num: num * num
print(square(5))
res = square(2.9)
print(res)


surafce_area_cylinder = lambda r,h:22/7 * r**2 * 2 + 22/7 * 2 * r * h
print(surafce_area_cylinder(7,20))


people =[
    {"name": "Alex", "age": 30},
    {"name": "Bob", "age": 40},
    {"name": "Charlie", "age": 33},
]
# lamda x:x['age']
sorted_by_age = sorted(people,key=lambda x:x["age"])
print(sorted_by_age)



# build_profile(experience=100, name ="Jane", age = 19, proffession = "Programming", gender = "Female")


# call function
# print (add(9,7,5))

# print(addition(23,23,544))
# print(addition(8,3))
# print(addition(8,3,6,8,9,9))