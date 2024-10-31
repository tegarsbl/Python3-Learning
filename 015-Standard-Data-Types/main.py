"""
Standard Data Types
Python has five standard data types-
- Numbers
- String
- List
- Tuple
- Dictionary
"""

# Python Numbers
var1 = 1
var2 = 10
print(var1,var2)

# Python Strings
str = 'Hello World!'
print(str) # Prints complete string
print(str[0]) # Prints first character of the string
print(str[2:5]) # Prints characters starting from 3rd to 5th
print(str[2:]) # Prints string starting from 3rd character
print(str * 2) # Prints string two times
print(str + "TEST") # Prints concatenated string

# Python Lists
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list) # Prints complete list
print(list[0]) # Prints first element of the list
print(list[1:3]) # Prints elements starting from 2nd till 3rd 
print(list[2:]) # Prints elements starting from 3rd element
print(tinylist * 2) # Prints list two times
print(list + tinylist) # Prints concatenated lists

# Python Tuples
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print(tuple) # Prints complete tuple
print(tuple[0]) # Prints first element of the tuple
print(tuple[1:3]) # Prints elements starting from 2nd till 3rd 
print(tuple[2:]) # Prints elements starting from 3rd element
print(tinytuple * 2) # Prints tuple two times
print(tuple + tinytuple) # Prints concatenated tuple

# Python Dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict['one']) # Prints value for 'one' key
print(dict[2]) # Prints value for 2 key
print(tinydict) # Prints complete dictionary
print(tinydict.keys()) # Prints all the keys
print(tinydict.values()) # Prints all the values


# Data Type Conversion
"""
int(x [,base])
float(x)
complex(real[,imag])
str(x)
repr(x)
eval(str)
tuple(s)
list(s)
set(s)
dict(d)
frozenset(s)
chr(x)
unichr(x)
ord(x)
hex(x)
oct(x)
"""

