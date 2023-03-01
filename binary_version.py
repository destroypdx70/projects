def square_root_v3(x):
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

