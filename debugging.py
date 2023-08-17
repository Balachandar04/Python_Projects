def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

# F5  ---> Start debugging
# F9  ---> Setting Breakpoint
# F10 ---> jump to next statement
# F11 ---> go to the function


print("start")
print(multiply(1, 2, 3))
print("Finish")
