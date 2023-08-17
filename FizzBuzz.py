def fizz_buzz(input):
    flag1 = "Fizz " if input % 3 == 0 else ""
    flag2 = "Buzz" if input % 5 == 0 else ""
    if flag2 or flag1:
        return flag1+flag2

    return input


print(fizz_buzz(7))
