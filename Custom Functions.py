from Numbers import result

def greet():
    print("Hello")

def greeting(name):
    print(f"Hello {name}")
# greet() #call (use) a fn
def volume_cylinder (radius, height):
    v = 22/7 * radius**2 * height
    a = 22/7 * radius**2 *2 + 22/7 * radius* 2 *height
    print(round(v, 2))
    return v ,a


def volume_cylinder2(radius, height):
    v = 22/7 * radius**2 * height
    return v
def volume_surface(radius, height):
    v = 22 / 7 * radius ** 2 * height
    a = a = 22/7 * radius**2 *2 + 22/7 * radius* 2 *height
    return v,a

# greeting('Sila')
# greeting('Samia')
# greeting('Ahmed')
# volume_cylinder(10,20)
# volume_cylinder(8,18)

# result = volume_cylinder(6.5,8.9)
# print(round(result,3))
with open("volume.txt","w") as file:

     file.write(str(result))

volume, area = volume_cylinder(radius=10, height=20)
print(f"volume is {volume} and area is {area}")

# named parameters
v,a = volume_cylinder(radius=10, height=20)

def divide(a,b, should_round = False):
    res =  a/b
    if should_round:
        return round(res,2)
    else:
        return res
print(divide(9,5.11, True))
print(divide(a=10,b=15, should_round=True))



