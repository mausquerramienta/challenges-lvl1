# Challenge level 1
# Check if a string or number reads the same forwards and backwards

# I'm going to use a function to do so.
# Here it is how it looks like and an brief description. 

def is_palindrome(input_data):
    original_str = str(input_data)
    reversed_str = original_str[::-1]
    return original_str == reversed_str

    # 1. str(input_data): I'm going to cast the input data into a string. This ensures 
    #    that if the user inputs an integer (such as 12321), it won't crash.
    #    Why use a string type variable? Because according to documentation, a string is an
    #    ordered sequence, which means I can apply "slicing" to it. 
    # 2. [::-1]: This is how to apply slicing feature in Python. Leaving the start and end 
    #    empty means to take the whole string, and the -1 step means to make it backwards.
    #    Returns True if they match, False otherwise. 
    

# TESTS CASES

# Case 1: Standard string palindrome
print(f"radar: {is_palindrome('radar')}") 

# Case 2: Number palindrome
print(f"12321: {is_palindrome(12321)}") 

# Case 3: Not a palindrome
print(f"python: {is_palindrome('python')}") 
