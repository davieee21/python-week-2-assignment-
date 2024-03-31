#type conversion and comments 
#implicit (automatic)
x = 123
y = 123.43289
z = x + y
print(z)
print (type(z))
print ("value:",z)
print('data_type:',type(z))

#explicit (manual)
x = '12'
y = 23
x = int(x) #this line converted x which was a class str to a class int
print (x+y)
z = x+y
print (z)
