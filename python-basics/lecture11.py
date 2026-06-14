def get_number(name):
    try:
        return int(input(f"enter your number ({name}) : "))
    
    except ValueError:
        print("error : value is not a number")
        print("handling by using 0 as val")
        return 0

def add(a, b):
    c = a + b
    print("result of addition is", c)
    return c

val1 = get_number("val 1")
val2 = get_number("val 2")
val3 = get_number("val 3")

print("running add function with values :", val1, val2)

answer = add(val1, val2)

print("add function executed successfully")

print("running add function with values :", answer, val3)

add(answer, val3)

print("add function executed successfully")