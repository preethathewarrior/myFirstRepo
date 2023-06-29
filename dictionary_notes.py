'''#Dictionaries
  ordered collection of data
  mutable means chageable can be updated removed or inserted
  key-value pair
  eg: items={"india":Delhi,           # here india is key and delhi is value,
             # duplicate cannot be used as key but  values can be duplicate
             "nepal":"kathmandu",
             "England": "london"}
  enclosed with {}
  muliple values are allowed in single key. folllowing hashmap techiniques
 eg:
   student={
       "name":"jack", #here we given the corresponding key and values
       "marks":[45,89,47,98,90], # values can be made as list
       "class":7 }
dict1={}    # empty dictionary creation
print(type(dict1))
'''
'''symbol={
    "H":"hydrogen",
    "He":"Helium",
    "li":"lithium",
    "C":"Carbon",
    "o":"oxygen","N":"Nitrogen"}
print(symbol)
print(symbol.keys()) # here the output will be in list
print(symbol.values()) # here the output will be in list
print(symbol.items()) # here each key-value pair will be get seperately
print(symbol["H"]) # in order to get a particular value , put the key in the square bracket
symbol["p"]="Phosphorous" # in order to add a key value
print((symbol))
symbol["C"]='carbondioxide'# inorder to update
print((symbol))
del symbol["p"] we use key to delete the keyvalue pair
print((symbol))
symbol.update({"s":"sulphur"})
print((symbol))

student={
    1:"George",
    "class":6,
    "mark":[22,48,90,77,67]
}
print(student)
print(student.items())
print(student.get("class")) # in order to view the value of the key given. here in the bracket we put the key
#print(student.pop(1)) #here 1 is the key
print(student)
# in order to show the dictionary as list and to store in another
newlst=list(student) #list() is a function
print(newlst) # here the result is keys
newlst=list(student.items()) # in order to show the key value pair
print(newlst)
s1=dict(newlst) # to convert the list into dictionary
print(s1)

student.clear() # the reserved space memory will be there but there wont be any value. # empty dictionary
print(student)'''
#task: create a dictionary of students and
# get the user input of student name and print their corresponding marks.
s=input("Enter the student name")
sub=input("Enter the sub:")
'''dictionary={
    "Devika":[45,78,39,88,89],
    "Anamika":[76,89,78,90,90],
    "Dev":[78,90,45,67,89],
    "Priya":[78,89,99,98,67]
}
print(dictionary.get(s))'''

dict1={
     "Devika":{"phy":45,"math":78},
    "Anamika":{"phy":76,"math":89}
}
print(dict1.get(sub))