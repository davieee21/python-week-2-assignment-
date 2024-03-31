# sets {} usually has no particular order thus output order may be different
student_id = {112,113,115,116,118,120}
print("Student Id:", student_id)
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel letters:', vowel_letters)

empty_set = () #class tuple
empty_set2 = set() #class set
empty_dictionary = {} #class dictionary
print(type(empty_set))
print(type(empty_set2))
print(type(empty_dictionary))

#set data types are unordered and as such indexing is meaningless
#you cant duplicate items in a set

#adding items to a set use add() function
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
vowel_letters.add('x')
print(vowel_letters)

#update python set
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
student_id = {112,113,115,116,118,120}
vowel_letters.update(student_id)
print(vowel_letters)

#remove an element from set (use discard())
student_id = {112,113,115,116,118,120}
student_id.discard(112)
print(student_id)

#iterate over a set in python (use for loop to acess each id)
student_id = {112,113,115,116,118,120}
for student_id in student_id:
    print(student_id)

#find number of set elements (use len())
student_id = {112,113,115,116,118,120}
print('total Elements:', len(student_id))

#python set operations
#set union in python (uses (|) or union())

A = {1,2,3}
B = {0,4,5}
print (A|B)
print(A.union(B))

#set intersection in python (uses (&) or intersection())
a = {1,3,5,8,}
b = {1,8,4,9}
print (a&b)
print (a.intersection(b))

#differentiate between two sets (uses (-) or difference()) 

a = {1,3,5,8,}
b = {1,8,4,9}
print(a-b) #elements of set a that are not in set b
print(a.difference(b))

#set difference uses (^) or symmetric_difference()
a = {1,3,5,8,}
b = {1,8,4,9}
print(a^b)
print(a.symmetric_difference(b))

#check if two sets are equal
a = {1,3,5,8,}
b = {1,8,4,9}
if a == b:
    print('you guy my guy')
else:
    print('jaba')

a = {1,3,4,8,}
b = {1,8,4,3}
if a == b:
    print('you guy my guy')
else:
    print('jaba')
    