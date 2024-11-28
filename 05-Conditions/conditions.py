x = 10

if x > 5:
    print("x is greater than 5")


y = 3

if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")


z = 7

if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is 5 or less")

def switch_case(value):
    if value == 1:
        return "Case 1"
    elif value == 2:
        return "Case 2"
    elif value == 3:
        return "Case 3"
    else:
        return "Default case"

print(switch_case(2))



