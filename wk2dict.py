#dictionaries 
#they are ordered items, store elements in key/value pairs

capital_city = {"nepal": "kathmandu", "italy": "rome", "Kenya": "nairobi"}
print(capital_city)
#keys and values can be of different types
numbers = {1: "one", 2: "two", 3: "three"}
print(numbers)


#add elements to a dictionary (done by adding the key with [])
capital_city = {"nepal": "kathmandu", "italy": "rome", "Kenya": "nairobi"}
print("initial dictionary:", capital_city)
capital_city["japan"] = "tokyo"
print("updated dictionary: ", capital_city)


#change value of the dictionary also use[]
student_id = {111: "Erick", 112: "Kyle", 113: "Davis"}
print ('Initial dictionary: ', student_id)
del student_id[111]
print('updated student id:',student_id)
student_id[112] = 'Stan'
print (student_id)

#accessing elements from the dictionary use the keys to access the corresponding values
student_id = {111: "Erick", 112: "Kyle", 113: "Davis"}
print(student_id[113])


#dictionary Membership test- tests if a key is in a dictionary or not. uses the keyword (in)
#only for keys not values
student_id = {111: "Erick", 112: "Kyle", 113: "Davis"}
print(1 in student_id)
print(113 in student_id)
print (119 not in student_id)

#iterating through a dictionary
#iterates through the keys in the dictionary. Use the loop
student_id = {111: "Erick", 112: "Kyle", 113: "Davis"}
for x in student_id:
    print(x)