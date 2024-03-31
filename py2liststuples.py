#lists
numbers = [1,2,3]
print(numbers)
#changing the items on the list using the index
numbers[0] = 10
print(numbers)
#output : [10,2,3]

#finding the length of the list
print(len(numbers))


#access item as index
languages = ['python', 'swift', 'c++' ]
print (languages[0])
print (languages[2])

#list slicing in python (slicing operator)
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n']
print (my_list[2:5]) #index 2 to index 4,,,index 5 is exclusive
print (my_list[5:]) #index 5 to end
print(my_list[:]) #everything


#add elements to a python list
# 1. using append : adds an item to end of list
numbers= [21, 83, 39, 93, 92]
print (numbers) # or print ('before append:', numbers)
numbers.append(34)
print (numbers) # or print ('after append:', numbers)


#using extend to join 2 lists
prime_numbers = [2,3,5]
even_numbers = [4,6,8,2]
prime_numbers.extend(even_numbers)
print(prime_numbers) #print('list after extend:', prime_numbers)

#change list items
# 1. using del()
languages = ['python', 'swift', 'java', 'c++', 'html', 'javascript', 'rust', 'R']
del languages[1]
print (languages)
# 2. using remove()
languages.remove('python')
print(languages)
# 3. using pop()
languages = ['python', 'swift', 'java', 'c++', 'html', 'javascript', 'rust', 'R']
removed_language = languages.pop(2)
print("Removed language:", removed_language)  # Output: Removed language: java
print(languages)  # Output: ['python', 'swift', 'c++', 'html', 'javascript', 'rust', 'R']
# returning the deleted item in pop()
# 1. using the list concatenation method(append)
languages = ['python', 'swift', 'java', 'c++', 'html', 'javascript', 'rust', 'R']
removed_language = languages.pop(2)
print("Removed language:", removed_language)  # Output: Removed language: java
languages.append(removed_language)
print(languages)  # Output: ['python', 'swift', 'c++', 'html', 'javascript', 'rust', 'R', 'java']
# 2. Using the insert method (insets at the specified index)
languages = ['python', 'swift', 'java', 'c++', 'html', 'javascript', 'rust', 'R']
removed_language = languages.pop(2)
print("Removed language:", removed_language)  # Output: Removed language: java
languages.insert(2, removed_language) #this inserts the removed language where it was initially
print(languages)  # Output: ['python', 'swift', 'java', 'c++', 'html', 'javascript', 'rust', 'R']
 
 
 #iterating through a list : using the for loop
languages = ['python', 'swift', 'java', 'c++', 'html', 'javascript', 'rust', 'R']
for language in languages :
    print(language)
    
#python list comprehension
numbers = [number*number for number in range(1,6)] #first number included, last number ignored
print (numbers)



#tuples
#cannot be changed once assigned ()
var1 = ('hello')
print(type(var1))
print(var1)  #will be a string

var2 = ('hello',)
print(type(var2))
print(var2) #will be a tuple

var3 = 'hello',
print(type(var3))
 #access,,,each element rep by index numbers (o,1,2,...)
letters = ('w', 'x', 'f', 'a', 'g', 'q', 'b', 'i')
print(letters[3])
print(letters[2])
print(letters[6])

#negative indexing
#-1 = LAST ITEM, -2 = second last item and so forth
letters = ('w', 'x', 'f', 'a', 'g', 'q', 'b', 'i', 'm', 'p')
print(letters[-3])
print(letters[-1])
print(letters[-8])

#python tuple methods

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.count('p'))
print(my_tuple.index('l'))



