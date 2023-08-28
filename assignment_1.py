           #Basics of Python
           #python multipurpose language .
           # print is a magic word and also a function to display any thing.

     # 1.Arithmatic operations 

f = 9+3         # we can do addition of any two numbers.
print(f)
g = 8-4         # we can also do subtraction of any two numbers,
print(g)
h = 4*5         # we can also do multiplication as well.
print(h)

Result = f + g * h      # we can also do differents arithmatic operation together.
print(Result)
print(type(Result))      # we can also find the type of our answer.

a = 8/6   # we can also do divion of any two numbers.
print(a)
a = 8//6     # if we put double slash fordivision our answer will come asroundup in condition if we have a answer in float.
print(a)
b = 4%2   # its answer will always 0.
print(b)

result1 = (a + b) / h  # here we also do differents arithmatic operation together
print(result1)
print(type(result1))        # we can also find the type of our answer.

result2 = (a + f) / g       # here we also do differents arithmatic operation together
print(result2)
print(type(result2))          # we can also find the type of our answer.
             # Another Example
x = 1+2     # here we do addition.
print(x)

y = 8-3          # here we do subtraction.
print(y)

z  = 4*5          # here we do multiplication.
print(z)

result3 = (z - y) // x      # here we also do differents arithmatic operation together
print(result3)
print(type(result3))          # we can also find the type of our answer.

          # 2, Data types
        #integere ( 12,345,567,6789)
print(type(6))     # its an integer data type.
print(type(18))
        #string (' '," ",'''   ''')
print("Hello")         #'hello' is string data type.
B = 'nature'
print(type(B)) 





             #3. Variables and its types
             # using variables also save us from repetition.
             # variable means a container that stores everything.

a = 60     # in it a store the value 60.
print(type(a))   # here we find the type of the variable.

b = "Green mountains"    # we can also store a sting value in a variable.
print(type(b))      # here we find the type of the variable.

c = (2+8)      # we can also store the result of any arithmatic operation in avariable.
print(c)
print(type(c))    # here we find the type of the variable.

Father = "#most Loyal person, Do everything for you, unexpressive person"   # we can also store a sting value in a variable, we cannot use key words of python as a variable so choose a name very carefully.
print(Father)
print(type(Father))     # here we find the type of the variable.

Father = ("#most Loyal person", "Do everything for you", "unexpressive person", 12345)     # here we can write the same thing in another form.
print(Father)

                 #4.Type casting
                 # means changing the data type of a variable

a = 6.10       # as we know the given value is in float.
print("the type of a before typecasting ", type(a))    # here we find the type of the variable.
a = int(a)
print("the type of a after typecasting ", type(a))     # here we find the type of the variable after changing its type to integer type.
a = str(a)
print("the type of a after typecasting ", type(a))     # here we find the type of the variable after changing its type again from integers to string.
print(type(a))
a=int(a)   # we can also change the type of a variabe by this method.
print(type(a))   # here we find the type of the variable.
print(a)     # here we simply print a after changing its type.


                  #5.Indexing
                  # means to find position of a word
                  # remember  that indexing always starts fron zero(0)
a= "Simplicity is the best"
print(a[0])      # here we find a word at position 0.
print(a[4])      # here we find a word at position 4.
print(a[8])      # here we find a word at position 8.
print(a[11])      # here we find a word at position 11.
print(a[18])      # here we find a word at position 18.

print(a[2:7])     # here we can also find the words at the position between 2 and 7.
print(a[2:9])     # here we can also find the words at the position between 2 and 9.
print(a[ :9])     # here we can also find the words at the position fron strating to the position 7, the blank space mean the position starts from 0.
print(a[4: ])    # here we can also find the position from  4 to the last position, the blank space after the colon mean its goes to the last position.
print(a[4: :15])   # here we can also print the word between two position like 4 and 15 , the blank space between two numbers means it will print the words between these two words.
print(a[ : ])       # here we put the both position blank which means it will give the full string as a result.

        #6.Conditions

        # if condition
x = 10   # here we give a value to a variable.
if x>5:       # in this line we give a if condition .
    # as given below we give both conditions True so it will gives both conditions as a result.
    print("x is greater than 5")
    print("x is also greater than 3")

     #  2nd example
x = 10      # here we give a value to a variable.
if(x>15):     # in this line we give a if condition .
    # as given below we give different conditions, if we give a condition out of the block (block of code) it will always gives that condition as an output that is out of the block
    print("x is greater than 5")
    print("x is also greater than 3")
print("x is greater than 15")

     # Using  if with else
x = 10       # here we give a value to a variable.
if(x>8):      # in this line we give a if condition .
    print("x is greater than 8")     # if this statement is true as pr contion then it will be shown as an output.
else:     # other wise the next statement after else will be shown as an output.
    print("x is smaller than 8")
         
     
     # Another example (in which we take value from user)

a = input("Enter your marks") # in this we take a value from the user.
a = int(a)      
print(a,type(a))   # it show the value given by user and also its type.
if a>70:
    print("you are a good student")      # if this statement is true as pr the value given by the user, if that value fulfil the above condition then it will be shown as an output.
else:          # other wise the next statement after else will be shown as an output.
    print("Do work hard")

             #elif condition
    # If we have more than one condiion
     #    Use of elif with if else
marks = input("Enter your marks")       # in this we take a value from the user.
marks = int(marks)      
print(marks,type(marks))      # it show the value given by user and also its type.
if(marks<40):
    print("do hardwork")    # if this statement is true as pr the value given by the user, if that value fulfil the above condition then it will be shown as an output.
elif(marks<60):     # it this elif condition if your marks are less than 60 it will give the elif statement as an output.
    print("you are a good student but put some more effort")
else:          # in else condition if your marks are above than 60 its statement will be shown as an answer.
    print("you are an excellent student")

  
      #7. LOOPs
      # while loop
      # for loop   (In python we only use these two loops)


     # while loop
     # in while loop we give condition but not know it really or correctly.

     #syntax of while loop
'''while(condition):
        block of code
'''

i = 0  # here we give value to a variable
while i<=12:   # here we give condition  but if we run it will print an infinity loop as an output.
    print(i)    
    i = i + 1  # this will add 1 after every time  the loop runs.
   

  # For loop
  # in for loop we already know the condition
  # syntax of for loop
'''for(condition):
        block of code
'''
for i in range(12):  # here we give a condition ourself
    print(i)      # in this output will be from 0 to 11.


color = ["green","red","blue","yellow","orange"]     # here we give some values
for i in color:     # here we give a condition
    print(i)     # in this output will be al the value we have given before the condition.

    #8. Function in python
      # TYPES OF FUNCTIONS
        # > built in funtion: That already present in language. ie.print()
        # > user define function: That we made ourself. addition()
        
# Syntax
'''
def funtion name():
    block of code
function calling
'''
# Function  definition and declaration
def intro():
    print("hello, what is your name?")
# Function calling
intro()     # always call the fuction outside the block of the code.

       # example
   # function defining and declaration
def multiplication():    # in this we will declare first what we are going to perform
    a = 14   # here we assign a value to a
    b = 6    # here we assign a value to b
    c = a*b   # here we do program of multiplication between a and b value, then store the answer in an another variable c.
    print(c)   # then we can have our output by print out it after defining all the program.
    # function calling
multiplication()      # at the last we will call that funtion that we declare at first.

        
