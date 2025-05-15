def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Division by zero not possible")

try:
    first_num = int(input("Enter a number: "))
    second_num = int(input("Enter another number: "))
    op = input("Enter operator add subtract multiply divide: ")

    match op:
        case "add":
            print(add(first_num, second_num))
        case "subtract":
            print(subtract(first_num, second_num))
        case "multiply":
            print(multiply(first_num, second_num))
        case "divide":
            print(divide(first_num, second_num))
        case _:
            print("Enter valid operator")
except ValueError:
    print("Enter numbers only")

##
print("Enter numbers. If you want to quit enter q: ")
nums = []
while True:
    inp = input()
    if inp == "q":
        break
    nums.append(int(inp))

total = nums[0]
op = input("Enter operator add subtract multiply divide: ")

for i in range(1, len(nums)):
    match op:
        case "add":
            total = add(total, nums[i])
        case "subtract":
            total = subtract(total, nums[i])
        case "multiply":
            total = multiply(total, nums[i])
        case "divide":
            total = divide(total, nums[i])
        case _:
            print("Enter valid operator")

print(total)
##
expr = input("Enter expression: ")
res = int(expr[0])
num = 0
curr_op = expr[1]

for i in range(2, len(expr)):
    if expr[i].isdigit():
        num = num * 10 + int(expr[i])
    else:
        match curr_op:
            case '+':
                res = add(res, num)
            case '-':
                res = subtract(res, num)
            case '*':
                res = multiply(res, num)
            case '/':
                res = divide(res, num)
            case _:
                print("Enter valid operator")
        curr_op = expr[i]
        num = 0

match curr_op:
    case '+':
        res = add(res, num)
    case '-':
        res = subtract(res, num)
    case '*':
        res = multiply(res, num)
    case '/':
        res = divide(res, num)
    case _:
        print("Enter valid operator")
print(res)
