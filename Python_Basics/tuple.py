#Tuple

my_tuple = ("sanket", 25, 58.00, "cybage software")
print(type(my_tuple))
print(my_tuple)

# Tuple of integers
a = (2, 2, 2, 2, 2, 2)
print(type(a))
print(a)

# Tuple of strings
b = ("guava", "apple", "orange")
print(type(b))
print(b[1])

#Tuple of dictionary
tuple_dictionary = ({"name": "sanket", "age": "25"}, {"key": "value"})
print(type(tuple_dictionary))
print(tuple_dictionary)

# Tuple operations - Cannot Do - Cannot Do - MAIN DIFFERENCE: LIST & TUPLE
# my_tuple = (1, 2, 3, 4, 5, 6)
# my_tuple.remove([0])
# print(my_tuple)

#Loop through Tuple
my_loop_tuple = (11, 12, 13, 14, 15)
for num in my_loop_tuple:
    print(num)


"""
Tuple are created using Square-bracket "()"
Tuple can store any type of data (string, int, dictionary)
Tuple in python are ordered means each item in a list has specific index.
Tuple are immutable means we can't change tuple after creation
"""