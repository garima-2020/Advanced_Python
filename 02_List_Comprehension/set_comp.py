# removes duplicate autoomatically

values = [1, 2, 2, 3, 3, 4]

unique_squares = {x * x for x in values}
print(unique_squares)