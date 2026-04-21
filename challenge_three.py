# Challenge level 1
# Look for the max and min values in an array and calculate it's length 

# I'm going to use two functions to do so.
# Here it is how them look like and an brief description. 

# Find Max/Min values without built-in functions.
def find_max_and_min(input_array):
    if not input_array:
        return None, None
    
    max_val = input_array[0]
    min_val = input_array[0]
    
    for num in input_array:
        if num > max_val:
            max_val = num  # New record for maximum found
        if num < min_val:
            min_val = num  # New record for minimum found
            
    return max_val, min_val

    # First, let's see if it is not an empty array.
    # Then, I declared my max and min values variables.
    # I did it with the given array in position 0. 
    # Next thing to do is to iterate through every value in an array with conditionals.
    # Finally, start looping through each number to compare it against our current value.


# Calculate String Length
def get_string_length(input_string):
    count = 0

    for character in input_string:
        count += 1
        
    return count

    # First, declare a counter at zero.
    # Python treats strings as iterable sequences. For every character 
    # (including spaces and symbols) we find, we increment our counter.



# TESTS CASES

# Case 1: Positive and negative intergers
numbers = [4, 1, 9, -3, 5]
max_res, min_res = find_max_and_min(numbers)
print(f"Max: {max_res}\nMin: {min_res}")

# Case 2: Empty Array
print(f"Empty Array: {find_max_and_min([])}")

# Case 3: Standard string
text = "Python Developer"
print(f"Length: {get_string_length(text)}")

# Case 4: Empty String
print(f"Empty String: '{get_string_length('')}'")
