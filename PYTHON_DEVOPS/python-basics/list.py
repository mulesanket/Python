# List of integers
a = [2, 2, 2, 2, 2, 2]
print(type(a))
print(a)

# List of strings
b = ["guava", "apple", "orange"]
print(type(b))
print(b[1])

#List of dictionary
list_dictionary = [{"name": "sanket", "age": "25"}, {"key": "value"}]
print(type(list_dictionary))
print(list_dictionary)

# List operations
# Add, remove, pop (deletes last element)
my_list = [1, 2, 3, 4, 5, 6]
my_list.append(7)
print(my_list)

#Loop through list
my_loop_list = [11, 12, 13, 14, 15]
for num in my_loop_list:
    print(num)

"""
List are created using Square-bracket "[]"
List can any type of data (string, int, dictionary)
List in python are ordered means each item in a list has specific index.
List are mutable means we can chnage list after creation
"""