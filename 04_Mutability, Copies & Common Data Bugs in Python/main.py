a = [3,5,2,21]

b = a  # b bhi usi a ki list ko refer krra h to hai to ek hi chiz 

b[1] =  666
print (a) # [3, 666, 2, 21]

# if want copy then

a = [3,5,2,21]

b = a.copy()
b[1] =  666
print (a) # [3, 5, 2, 21]

# hidden mutation inside func
def add_item (items):
    items.append(10)

data = [1,2,3]
add_item(data)

print (data) # [1,2,3,10]

# if dont want to modify add copy 
def add_item (items):
    items.append(10)

data = [1,2,3]
add_item(data.copy())

print (data)