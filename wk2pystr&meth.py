#strings and sequences
#single quotes'' or double quotes "" used to represent a string
greeting = "hello"
#accessing string characters in python
# 1. indexing- treats the string as a list and use index values
greeting = "hello"
print(greeting[1])
# 2. negative indexing
greeting = "hello"
print(greeting[-1])
# 3. slicing
greeting = "hello"
print(greeting[1:3])
print(greeting[0:5])

#in python, strings are immutable ie the characters cannot be changed
#however, the variable name can be assigned to a new string
greeting = "hello"
greeting = "ola"
print(greeting)

#python multiline string- uses triple double quotes """ or tripple single quotes '''

message = '''
I cannot give up
I have to be the best
I will work hard
'''
print(message)

#python string operations
# 1. compare two strings
str1 = 'hello world'
str2 = 'I will be the best'
str3 = 'hello world'

print(str1==str2)
print(str3==str1)

#join two or more strings(concatenate) use the plus + sign
greeting = 'Hello, '
name = 'Davis'
result = greeting + name
print(result)

#python string length (uses the len() method)
greeting = "hello"
print(len(greeting))

#string membership test (uses the in, not in function)
greeting = "hello"
print('l' not in greeting)

print('x' in 'moraxella')

#escape sequences in python used to escape some of the characters present in a string (uses the escape character(/))
#example = "He said, "What's there?""
#print(example) - throws error
example = "He said, \"What's there?\""
print(example)
example = 'He said, "What\'s there?"'
print(example)

#python string formatting (f-strings) use these {}
name = 'Davis'
country = 'Kenya'
print(f'{name} is from {country}')




