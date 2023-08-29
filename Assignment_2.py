         #BASICS OF PYTHON (2nd Part)
           # pythonis a multipurpose language ,and also easiest languageto learn.
           # print is a magic word and also a function to display any thing in python.

        #DATA STRUCTURES 
        #here we can storre different types of data.

        #1. List
            #List is a collection which is ordered and changeable. Allows duplicate members.
            # List is Muteable( means we can do changes in the List).
List1 = [1,2,3,4,5,6,7,8,9,10]
List2 = [24,56,"Nature view",8.9,True]
print(List1)    # it will give the whole List as an output.
print(List2)    # it will give the whole List as an output.

#checking type of list

print(type(List1))    #here it will gives the type of the list1.
print(type(List2))    #here it will gives the type of the list1.

#indexing of list (position of values)
    # indexing always starts from zero(0).  

a = [2,4,6,8,10,12,14,16,18,20]

print("The value at index 0 is",a[0])       # here we find a word at position 0.
print("The value at index 2 is",a[2])       # here we find a word at position 2.

print(a[2:7])        # here we find words from index 2 to index 7.
print(a[ :8])        # here it will give words from starting of index(o) to the index 8 because blank space before colon means its the first index.
print(a[4: ])          # here it will give words fron index 4 to onward because the is blank space after the colon that means it will all the List onward to the last index fron index 4.

print(a[2: :8])      # here it will give the value on index 2 and then it will count 8 index forward and then print the value on that 8th index.
print(a[ : ])        # here it will print all the List because both the places are blank.43


            # operations on list

#updation on list
     # change values at different specific index.
a = [1,2,3,4,5,6,7,8,9,10]
a[3] = 12      # here we change value of index 3 (we change value 4 by the value 12)
a[6] = 6       # here we change value of index 6 (we change value 7 by the value 6)
a[8] = 14       # here we change value of index 8 (we change value 9 by the value 14)
print(a)       # here we print the List that form after all the changes.

#Addition of value
a.append(17)      # to add a new value at the end of the list
print(a)           # here we print the List that form after adding the value at the end of the list..


a.insert(6, 13)        # to add a value at any index in a list, 1st argument = index,2nd argument = value (to be inserted) Like insert value 13 at the index 6.
a.insert(4, 3)         # to add a value at any index in a list, 1st argument = index,2nd argument = value (to be inserted) Like insert value 3 at the index 4.
print(a)               # here we print the List that form after inserting the values.
#sorting the list 
print("list before sort function: ",a)      # here we simply print the list before sorting.
print(len(a))        # to check the length of our list
 
a.sort()         # to sort list in ascending order
print("list after sort function", a)       # here we print the list after sorting.
print (a)
#Count (a specific value if it present multiple times OR to count how many times a value is present in the list.)
print(a.count(3))      # to count a specific value in list

#Remove
a.remove(9)       # to a value by its own name like ye remove 9 from the list.
print(a)
#Pop
a.pop(2)          #to remove a value by its index place like here we remove value from index 2.
print(a)
# adding values of different data types at the end of the list.
a = a*2      # here we multiply the whole list by 2 means it will print 2 times.
a.append("Waterfall")      # here we add a string at the end of the List.
a.append(4.5)     # here we add a float value at the end of the list
print(a)        # here we print thelist after all the changes in the list.


        #2. Tuple
        #Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
        # tuple is like List but it is imuteable( we cannot do changes in it).
tup = (0,1,3,4,4,5,6)
print(tup)           # it can also show duplicate  vales mean two same values
print(type(tup))     # here we can alsp print the type of the Tuple
#         #Operations on Tuple

   # operations that does not work on Tuple
tup.append('water')   # this operation does not work for Tuples so if you try then error comes up.
tup.remove(2)         #we can't remove values from tuple
print(tup)
tup[3] = 4           #we can't change a value with another value
print(tup)
print(tup.add(7))            #we can't add a value in tuple
print(tup)

# Indexing
# we call a value by its index(position).
print(tup[3])    # here we can call a value by its index no. like value on index 3.
print(tup[5])    # here we can call a value by its index no. like value on index 5.

 #count ( in this we can count how many time a value is present i the Tuple).
print(tup.count(4))  # we can call that value by its own name.
print(tup.count(2))
# data types in tuple( we can use differnt data types in tuple)
tuple1 = (24, True, 4.0, "precioue")
print(tuple1)
print(type(tuple1))


             #3. Dictionary
             #Dictionary is a collection which is ordered** and changeable. No duplicate members
Dict_1 = {
    "Name" : "Precious",
    "Degree" : "Bioinformatics",
    "Roll no" : 5264,
    "Marks" : [12,18,25,8,14]
}
print(Dict_1)     # here we print the all dictionary that we entered before.
print(type(Dict_1))       # here we can check the type of dictionary.
print(Dict_1.items())       # here it will show all the items in the dictionary.

        #Operations on Dictionary
print("keys of dictionary are: ", Dict_1.keys())      # here it will show all the keys of the dictionary, that are peresent in the left side.
print("values of dictionary are: ", Dict_1.values())      # here it will show all the values of the dictionary, that are peresent in the right side.
       # here we can print the value by calling the keys
print(Dict_1["Name"])      # here we call the value that is present the key Name.
print(Dict_1["Degree"])    # here we call the value that is present the key Degree.
print(Dict_1["Roll no"])   # here we call the value that is present the key Roll no.
print(Dict_1["Marks"])     # here we call the value that is present the key Marks.
      # clear  (use to  delete all the data of the dictionary)
Dict_1.clear()   #here by using this we can clear OR blank the dictionary.
print(Dict_1)
      # updating the dictionary
      # we can add a new item in the dictionay
Dict_1["subject"] = "Genetics"   # here we add a new item called subject = Genetics.
print(Dict_1.items())            # here we can print that item in the dictionary.
    #pop  (To remove a key and value from the dictionary)
Dict_1.pop("subject")      # here we remove thes ubject from the items of the dictionary.
print(Dict_1)              # here we print the dictionary after removal of that item.
#2nd way of updating the value of any key in the dictionary.
Dict_1["Degree"] = "Data science"       # here we change the value of the key item from bioinformatiocs to Data science. 
print(Dict_1)             # here we print the key after changing its value.


          #4. Set
          #Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members
          #Sets are written with curly brackets

A = {1,2,3,4,5,6,8,9,10}
print(A)         # we can  print the whole set values like this.
print(type(A))      # here we can find the type of the set.
  
    #Operation on the set
A = {1,2,3,4,5,6,8,9,10}
# #Data types in a set
B= set([1,2,"Fine",6.8,True])        #(we can also write like this) 
print(B)            # we can  print thr whole set values like this.
print(type(B))      # here we can find the type of the set.

# Add   (memory will be ellocated at remdom possition)
A.add(7)            #we can add a value in set
print(A)
#Pop  (Remove a rendom item from the set)
A.pop()
print(A)

#Remove  (we can remove a value from the set)
A.remove(2)         #we can remove a value from the set by its own name.
print(A)
#Clear (we can remove all the value from the set )
A.clear()       # here by this set will become empty.
print(A)
 #Discard ( use to remove the specified items)
A.discard(3)       # here we can remove a value by its own name.
print(A)

# Operation by using two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)   # this will print all the value of two set without repeatition of any value.

print(z)

x.update(y)     # in this method it will insert the items from set y into set x

print(x)

z = x.difference(y)    # in this method it will return a set that contains the items that only exist in set x not in set y.

print(z)

z = x.intersection(y)    # in this method it will return a set that contains the items that exist in both set x, and set y

print(z)

z = x.isdisjoint(y)     #in this method it will return True if no items in set x is present in set y

print(z)

z = x.issubset(y)       # in this method it will return True if all items in set x are present in set y

print(z)

# Another way(if we assign an empty set to a variable)
a = {}
print(type(a))        # here its type will be change from set to Dictionary.