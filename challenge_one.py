# Challenge level 1
# Remove duplicate elements from an array, ensuring only unique values in it 

# I'm going to use a function to do so. 
# Here it is how it looks like and an brief description. 

def remove_duplicates(input_array):
    return list(set(input_array))
    # 1. set(): The function set() takes the original list and converts it into a set. 
    #    According to documentation, a set is a collection which is unordered, unchangeable*, and unindexed.
    #    When making this transformation, Python's engine scans the elements and automatically 
    #    removes any value that already exists in the set, leaving only unique values.
    # 2. list[]: Since sets and lists are different data types, to keep the initial array an list type
    #    I'll just have to cast the set into a list() to return the data in the exact same format.
    

# TESTS CASES

# Case 1: Standard array with multiple duplicates
standard_array = [1, 2, 2, 3, 4, 4, 4, 5]
print(remove_duplicates(standard_array)) 

# Case 2: Empty array
empty_array = []
print(remove_duplicates(empty_array))

# Case 3: Array with a single repeated element
identical_array = [7, 7, 7, 7, 7]
print(remove_duplicates(identical_array))

# Case 4: Array with no duplicates
no_duplicates_array = [1, 2, 3, 4]
print(remove_duplicates(no_duplicates_array))

# Case 5: Array with different data types
mixed_array = ["a", 1, "b", 1, "a", 2]
print(remove_duplicates(mixed_array))
