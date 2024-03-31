a = 8
b = 7
a +=b #same as a = a+b
print (a)
a -=b #same as a = a-b
print (a)
a -=b
print (a)

#comparison operator
c = 6
d = 7
print (c==d)
print(c!=d)

#logical operators (and, or, not)
print ((c<d) and (c<=d))
print ((c<d) or (c>=d))
print ((c<d) or (c>=d))
print (not (c<d) or (c>=d))

#membership operators in and not in
x = 'hello world'
print ('h' in x)

#identity operators is and is not - used to check if two values are located on the same part of the memory
x1 = 5
x2 = 5
y1 = 6
y2 = 6
print ( x1 is y1)
print(y1 is not y2)



#python collection user input
num = (input('enter a number: '))
print ('you entered:', num)
print('data type of num:', type(num))

x = (input("tell me your name: "))
print(type(x))
print(x)
