'''
Write a python program to check if a variable is of a specific data type.
'''
def check_variable_type(variable, data_type):
    return isinstance(variable, data_type)

# Example usage
var1 = 10
var2 = "Hello"
var3 = 3.14
var4 = [1, 2, 3]

print(check_variable_type(var1, int))   # True
print(check_variable_type(var2, str))   # True
print(check_variable_type(var3, float)) # True
print(check_variable_type(var4, list))  # True
print(check_variable_type(var1, str))   # False
'''
This function takes a variable and a data type as arguments and returns True if the variable matches the data type, otherwise False.
'''

var = 10.5
if isinstance(var, float):
    print(f"{var} is a float.")
else:
    print(f"{var} is not float.")