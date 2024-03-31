#python variables
site_name = 'power learn project'

print(site_name)

site_name = '3'
print(site_name)

a, b, c = 5, 3.2, 'hii'
print(a)
print(b)
print(c)

a = b = c = d = 3000
print(a,b,c,d)

#python data types

#numeric data types
num1 = 5 #int
num2 = 5.1 #float
num3 = 1+3j #complex

#list data type enclosed with brackets []
languages = ['swift', 'java', 'python']

print(languages[0])  #acessed from index 0 thus for the languages, it is 0..1..2, not 1,2,3

#tuple data types....are immutable(cant be modified) use parenthesis for tuples()
product = ('microsoft', 'tuple', 499.392)
print(product[2])

#string data types  rep by single/double quotes
name = 'davis'
message = 'Ill be the best soon'

print(message)


#set data types unordered collection, separated by commas innside braces {}
student_id = {112, 114, 172, 283, 8483}
print(student_id)
print(type(student_id))

#dictionary data types: ordered, stores elements in key/value types use brackets {}
capital_city = {'Nepal' : 'Kathmandu', 'Italy' : 'Rome', 'Kenya' : 'Nairobi'}
#access : use keys to retireve values
print(capital_city['Kenya'])




