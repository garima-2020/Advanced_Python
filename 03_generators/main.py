# generators are created using yield function

def complex_calc(i):
# some complex calculations here
    return i*i

def get_numbers():
    for i in range(5):
        yield complex_calc(i) # yield i means dekha jayega jab mujhe chahiye tb dkhnge

#for i in get_numbers():
 #   print (i)      


# if want first number only
a = get_numbers()
# print(a, type(a))
print (next(a)) # for next number
print (next(a)) # 1
print (next(a)) # 4

# n Python, you can create generators using parentheses () instead of brackets []. Parenthesis are not tuple comprehensions, they create generators. List version:

# numbers = [i for i in range(5)]

# Generator version:

# numbers = (i for i in range(5))