<<<<<<< HEAD
def square_root_v1():
=======
def square_root_v1(x):
>>>>>>> 8290040 (Functions for get the square root)
    goal = int(input("Choose a number => "))
    result = 0

    while result**2 < goal:
        result += 1
    if result**2 == goal:
        print(f"The square root of {goal} is {result}")
    else:
        print(f"{goal} did not have been found")
    return result

<<<<<<< HEAD
def square_root_v2():
=======
def square_root_v2(x):
>>>>>>> 8290040 (Functions for get the square root)
    goal = int(input("Choose a number => "))
    epsilon = 0.01
    step = epsilon**2
    result = 0.0

    while abs(result**2 - goal) >= epsilon and result <= goal:
        result += step
    if abs(result**2 - goal) >= epsilon:
        print(f"{goal} did not have been found")
    else:
        print(f"The square root of {goal} is {result}")
    return result

<<<<<<< HEAD
def square_root_v3():
=======
def square_root_v3(x):
>>>>>>> 8290040 (Functions for get the square root)
    goal = int(input("Choose a number => "))
    epsilon = 0.01
    limit = 0.0
    maximun = max(1.0, goal)
    result = (maximun + limit) / 2

    while abs(result**2 - goal) >= epsilon:
        print(f"limit => {limit}, maximun => {maximun}, result => {result}")
        if result**2 < goal:
            limit = result
        else:
            maximun = result
        
        result = (maximun + limit) / 2

    print(f"The square root of {goal} is {result}")
    return result
<<<<<<< HEAD
        
if __name__ == "__main__":
    square_root_v1()
    square_root_v2()
    square_root_v3()
=======
    

print(square_root_v1(9))
print(square_root_v2(9))
print(square_root_v3(9))
>>>>>>> 8290040 (Functions for get the square root)
