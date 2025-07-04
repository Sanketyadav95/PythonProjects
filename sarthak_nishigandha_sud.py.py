# Why python is called a scripting language?
# python reads the code line by line and gives the output line by line
# Why python is dynamic??
# there is no need to mention the data type.
##It doesn't know about the type of the variable until the code is run.
# So declaration is of no use and the type of the variable is determined only
# during runtime.
# ()=parenthesis
#multiline comment
import math

print(2)
print(100)
print(2.005) #float is a decimal number
print('pune')
print("I live in pune") # plain text  is a string
print("'pune'")
print("2")
print(type("2"))
print(type(2))
print(type(2.005))
#booelean value True or False  #True=1 ,False=0


#Numbers
#float,integer
#type function will give the data type of variable.
#working with numbers
#Addition
#add 2 integers
#there is no need to declare data type of 2 numbers.
print(3+2)
print(3+2.5)
print(0.0025+2.5)

#subtraction
print(3-2)
print(3-2.5)

#multiplication
#here also i am not declaring the data type
print(3*5)
print(10*10)
print(6*6.6)

#division(/)
print(10/2)
print(45/6)
print(77/3)
print(22/3)

#floor division //
#it will cut out the demimal part ,it will take only the integer part of answer
print(45/6) #7.5
print(45//6) #7
print(77/3)
print(77//3)

#modulus operator( % )
#it will be remainder
print(10 % 3) #1
print(10 % 2) #0
print(99 % 5) #4

#inbuilt functions for numbers
#1.abs()
#it will give u the absolute (positive) value
print(abs(5))
print(-5)
print(abs(-5))

#2.max()
#it will give you the maximum number
print(max(100,12,400,23,600))
print(max(100,23,545,12))
print(max(1,2,3))
print(max(abs(-500),200,5,0))

#3.min()
#it will give you the minimum number
print(min(10,56,100)) #10
print(min(100,23,545,2)) #2

#4.round()
print(round(3.6)) #4
print(round(3.2101)) #3
print(round(3.526334)) #4
print(round(3.211893001)) #3
print(round(7.77556)) #8
print(round(9.497))


#5.floor()
#it will remove the decimal part and only gives the integer part
from math import *   #* means all
print(floor(13.6)) #13
print(floor(96.230000789)) #96
print(floor(3.526334)) #3
print(floor(3.211893001)) #3
print(floor(7.77556)) #7

#ceil()
#it will give you the next number
print(ceil(3.6)) #4
print(ceil(3.2101)) #4
print(ceil(5.526334)) #6
print(ceil(5.0004)) #6

# floor and ceil for negative numbers
#for negative numbers,floor will work as ceil and ceil will work as floor
print(floor(-2.11456789)) #-3
print(floor(-3.6)) #-4
print(floor(-3.2101)) #-4
print(floor(-3.526334)) #-4
print(floor(-3.211893001)) #-4
print(floor(-7.77556)) #-8


print(ceil(-3.6)) #-3
print(ceil(-10.5623)) #-10
print(ceil(-5.526334)) #-5
print(ceil(-3.211893001)) #-3
print(ceil(-10.8956)) #-10

#7.pow()
print(pow(3,2))# 3^2 base=3,power=2  #9
print(pow(2,2))# 2^2  #4
print(pow(2,10))# 2^10 #1024
print(pow(3,10))  #59049
print(pow(3,20))

#8.sqrt()
print(sqrt(25))
print(sqrt(456))


#variables
#Its a container where we can store the data.data can be a number or a string or
#a boolean value or a list or a tuple or a dictionary.

print("pune")
a="pune"
print(a)
c="I live in pune"
print(c)
x=100
y=200
print(x+y)
a=True
print(a)
Y="I am in mumbai"
y="I am in pune"
print(Y)
d=25.5689
print(d+100)
print(d-10)

#Rules to declare the variable_name
#1.Dont start the variable_name with a numeric
# 2pune=100 is not vàlid
# 2_pune=100 is also not valid
pune=100
print(pune)

#2.we can start a variable_name with a string or text
pune="hello" #this is valid
print(pune)
#22pune="hello" this is not valid
pune22="hello" #this is valid
pune_22="hello" #this is valid

#3.when you want a variable_name by combining 2 words then use _ to combine them
my_number=10
#my-number=10 #is not invàlid

x=12
y=23.564
z=True
bool_value=False
xyz_100="pune"
my_list=[1,2,3,4,5,6]
my_tuple=(4,85,789)
my_dict={"x":1,"y":2}

#string
#strings are plain text (letter,sentence,word)
#strings are always written under quotes "" or ''
h="nikhil"
print(h)
print('I live in pune from last 7 years')
my_number='100'
print(my_number)
print(type(my_number))
my_symbol="@"
print(type(my_symbol))

#Concatenation (+)
#its a process of combining or adding 2 or more strings together.
x1="sarthak"
print(x1+" lives in mumbai")
x2="I am in Pune"
print(x2+" Pune is in maharashtra")
print("Hello "+x1)
print("Hello "+x1+" welcome to pune!")
print("5"+"9") #59 #IMP
print(5+9) #14

my_fav_num=7
print(str(my_fav_num)+" is my fav number")
#str to make int into a string
print("Hello "+"John")
d1=100
d2="2"
#print(d1+d2)
print(str(d1)+" is my fav integer")

my_fav_lang="Python is my fav programming language."
my_string = "Python is booming language in world currently,"
print('Hello everyone '+my_string+my_fav_lang)


#working with strings
#inbulit functions for strings
#1.upper()
#it will convert lowercase to uppercase
k="pune"
m="Your choice of python is awesome"
print(k.upper())
print(m.upper())

#2.lower()
#it will convert uppercase to lowercase
print(k.lower())
k1="Pune"
print(k1.lower())
k2="I am Learning Python"
print(k2.lower())

#3.isupper()
#it will return True if all the letters in the string are uppercase
p="mumbai"
print(p.isupper()) #False
p1="I am in Pune"
print(p1.isupper())
p2="I AM IN PUNE"
print(p2.isupper())

#4.islower()
#it will return True if all the letters in the string are lowercase
p="mumbai"
print(p.islower()) #True
p1="I am in Pune"
print(p1.islower()) #False


#5.len()
#it will give you the length of a string i.e.how many characters are in string
r="sarthak"
print(len(r))
r1="I am learning Python"
#space is a character so it will be counted.
print(len(r1))
r2="Run away from this place"
print(len(r2))

#6.replace()
#it will replace old value by new value in the string
y="I live in pune"
print(y.replace("pune","mumbai"))

y1="Java is the language of choice"
print(y1.replace("Java","Python"))

y3="aadesh is a nice person"
print(y3.replace("a","x"))
print(y3.replace("a","x",1))
print(y3.replace("a","x",2))

y4="pune is nice city,i love pune,because pune is historical city."
print(y4.replace("pune","mumbai"))
print(y4.replace("pune","mumbai",2))

#7.capitalize()
#it will capitalize only the first letter of word or sentence
v="nikhil"
print(v.capitalize())

v1="pune is the place of choice"
print(v1.capitalize())
print(v1.upper())

#8.title()
#it will capitalize the first letter of every word in the sentence
v1="pune is the place of choice"
print(v1.title())
v2="The place of my choice is Pune"
print(v2.title())
v3="nikhil"
print(v3.title())

#9.index()
# it will give the index of the letter in the string
x="pune"
print(x.index("n"))
print(x.index("p"))
print(x.index("pune")) #it will tell u the index of where the the string starts
t="Python is best for everyone"
print(t.index('everyone'))
print(t.index("best"))
print(t.index('for'))

e="essential" #it will go with first occurance of letter or word
print(e.index('s')) #1
print(e.index('e')) #0

e1="python grows rapidly in world,python is a best choice."
print(e1.index('python')) #0

#10.count()
#it will tell how many times the letter or word appears in the string
v="He is in india,working in IT"
print(v.count("in"))#4
print(v.count("i"))#6
print(v.count("I"))#1

#11.split() #default split will be at space
#it will convert sentence into list of words
#but cant apply on single word
#if you split a string,output should be a list
d='pune is historical city'
print(d.split())
d1="nikhil"
print(d1.split())
print(d1.split('k'))

d3="my mail id is hello@gmail.com"
print(d3.split())
print(d3.split("@"))

d4="The city of Pune is Great! Pune is good! live here and see"
print(d4.split("!"))


#12.join()
#it will join the list of words and make a whole string
d='pune is historical city'
#print(d.split())
x=d.split()
print(x)
print(" ".join(x))
print("@".join(x))
print("#".join(x))

x1="my mail id is hello@gmail.com"
k=x1.split('@')
print(k)
print("@".join(k))

h=["Is","engineering","worth?"]
print(" ".join(h))

#13.strip()
#it will remove the whitespace around the string but
# not inside the string
b="  Python and Javascript are in demand currently"
print(b)
print(b.strip()) #default strip will be space

t1="....hello........???"
print(t1)
print(t1.strip(".?"))

t3=",,,,,,,,,hello,,,,,,"
print(t3.lstrip(','))
print(t3.rstrip(','))
print(t3.strip(","))

s="is this correct?"
print(s.strip("h"))
print(s.strip("?"))

g="pune is nice"
print(g.strip('e'))
print(g.strip('c'))
print(g.strip('p'))

x="Computer Programming"
#ComputerProgramming
print(x.replace(" ",""))


#14.isalpha()
#it returns True if all characters in string are alphabets
#only. whitespace is not a alphabet
t="helloworld"
print(t.isalpha()) #True

t1="hello world"
print(t1.isalpha()) #False

t2="Pune22"
print(t2.isalpha()) #False
t3="I live in pune"
print(t3.isalpha())

#15.isalnum()
#it returns True if all characters in string are alphanumeric i.e.alphabets or numbers
c="pune22"
print(c.isalnum())#True

c="pune"
print(c.isalnum())#True

c="22"
print(c.isalnum()) #True

c1="pune#mumbai"
print(c1.isalnum()) #False

#16.isnumeric()
#it returns True if all characters in string are numeric
x="454216"
print(x.isnumeric()) #True

x1="425623p"
print(x1.isnumeric()) #False

#isdigit()
x="454216"
print(x.isdigit()) #True

x2="12345#"
print(x2.isdigit()) #False

#17.center()
x="hello pune"
print(x.center(40))
print(x.center(40,'@'))

#18.casefold()
#it will convert upper case to lower case
x="HELLO WORLD"
print(x.casefold())
print(x.lower())
z1="Pune is Great!"
print(z1.casefold())
print(z1.lower())

#19.swapcase()
#it will convert uppercase to lowercase and lowercase to uppercase
r="Hello Pune"
print(r.swapcase())

#20.startswith()
r="hello ,welcome to pune"
print(r.startswith("hel"))
print(r.startswith("wel"))
#want to check if position 7 to 20 starts with wel
print(r.startswith("wel",7,20))#True
print(r.startswith("wel",6,20)) #False

d="i am at home"
print(d.startswith("ho",7,11)) #False
print(d.startswith("ho",8,11)) #True

d1='Python jobs are booming in the IT now.'
print(d1.startswith("n",5,12))

if d1.startswith("Python"):
    print(d1)
else:
    print("d1 does not starts with Python")

#21.endswith()
r="hello ,welcome to pune"
print(r.endswith('pune'))
print(r.endswith("u",7,20))


#22.find()
#it will return the index of the first occurrence of specified value
#if it does not found that value in the string then it will return -1
x="Python"
print(x.find('o')) #4
print(x.find('w')) #-1
y="this is Nikhil"
print(y.find('Nikhil')) #8
print(y.find('is')) #2
print(y.find('Python')) #-1

v="He is in india,working in IT"
print(v.find("in")+v.find("it"))

#find if 'p' is there in the index btn 6 & 9
p="hello pune"
print(p.find('p',6,8))

v="He is in india,working in IT"
print(v.find('india',5,15)) #9
print(v.find('He',5,15)) #-1

#rfind()
#it searches the string for a specific value and returns the last position
#where it is found

t="hello ,welcome to pune"
print(t.find('e')) #1
print(t.rfind('e')) #21

t1="essential"
print(t1.rfind("s")) #2

#23.istitle()
#it returns True if the first letter of every word in the string is uppercase.
t="Hello ,welcome to pune"
print(t.istitle()) #False
t1="Hello Pune Is Nice"
print(t1.istitle())

#24.removeprefix()
x='pre_record'
#print(x.removeprefix('pre'))

#25.removesuffix()
x1="computer_pro"
#print(x.removesuffix('pre'))

#indexing and slicing
# indexing default goes with left to right (positive indexing),and goes 0 onwords
#if we go in reverse direction indexing goes with -1
#indexing default goes with lower to higher index
k="mumbai"
print(k[3]) #b
print(k[5]) #i
print(k[-1]) #i
print(k[-4]) #m

k1="Python having various modules for many fields"
#whitespace (space,tab) are counted while indexing because whitespace is a character
#lets check the index of v
print(k1[9]) #v
print(k1[14]) #v
print(k1[-31]) #v

#slicing
#syntax:
#start index:stop index+1:stepsize
# slice of a string-a particular portion of a string.
k2="particular"
print(k2[3:7:1])
k3='Python is the no.1 language in world currently.'
#print(k3.index('l')) 19
print(k3[19:27])
#print(k3[31:36])
#indexing default goes with lower to higher index
#print world from given string with negative indexing
print(k3[-16:-8])
print(k3[-28:-20])
print(k3[-10:-16]) #blank because going from higher index to lower index
print(k3[1:5]) #ytho
print(k3[-10:-5])
print(k3[2:]) #from index 2 upto end
print(k3[:5]) #Pytho

k4="Pune is the historical city"
print(k4[-15:-5]) #historical
print(k4[-17:-3]) #e historical c

#capitalize first and fourth letter of the word
#method 1
x="sarthak"
#SarThak
part1=x[0:3] #sar
part2=x[3:] #thak
print(part1.capitalize()+part2.capitalize())

#method2
x="sarthak"
first_letter=x[0] #s
fourth_letter=x[3] #t
in_between=x[1:3] #ar
rest=x[4:7] #hak
print(first_letter.upper()+in_between+fourth_letter.upper()+rest)

s="mumbai"
print(s[::]) #from start to end
print(s[::-1])   #from end to start or reverse string

c='I believe the python rocks for next 15 years'
print(c[::-1])

#slicing with stepsize of 2 or 3
x="abcdefghijklmnop"
print(x[0:6:1])
print(x[0:8:1])
print(x[0:8:2]) #aceg
print(x[0:8:3]) #adg
print(x[0:-1:2]) #acegikmo
print(x[::2]) #acegikmo from start to end with step size of 2

#new line character (\n)
x='hello pune'
print(x)
print('hello\npune')

print('What colors are apples?\n(a)red\n(b)yellow\n(c)magenta')

a=1_2_3 #a=123
print(a*10) #1230

#string representation
#method 1
#f-string
#sam is 20 years old
#print("sam is 20 years old")
name='sam'
age=20
print(f"{name} is {age} years old")

name="Netra"
print(f"Her name is {name}")
print("Her name is Netra")

location='Pune'
state='Maharashtra'
print(f'I live in {location}.{location} is in {state}')

#.format method
print("{} is {} years old".format("nikhil",22))
print('I live in {}.{} is in {}'.format("Pune","Pune","Maharashtra"))
print('I live in {0}.{1} is in {2}'.format("Pune","Pune","Maharashtra"))

name='Eric'
profession='commedian'
affiliation='Monty Python'

print(f"Hi {name}.You are a {profession}.You are in {affiliation}.")
print(f"Hi {name}.\nYou are a {profession}.\nYou are in {affiliation}.")


#Lists[]
#Lists are denoted with []
#Array = it can store the similar kind or type of data
##list is a combination of all data types like numbers ,strings,
# boolean values, tuples ,lists,dictionary etc
#Lists are mutable i.e.we can change them,we can insert new element in the list,
#we can update existing element,we can the delete element in the list
# We can assign a new value to the list

x=[1,5,8,56,78,"hello","pune",True]
#indexing for list
print(x[5]) #hello
print(x[2:7]) #[8,56,78,"hello","pune"]

x1=[4,8,6,78,23,"nikhil",'mumbai',[True,56,'pune']]
print(x1[7][1])

x1=[4,8,6,78,23,"nikhil",'mumbai',[True,56,'pune'],('x',78,False),0.002,1.56]
print(x1[8][2])
print(x1[9])

y=[1,2,3,[4,5,"Hello"]]
print(y[3][2])

#Reassign Hello by Goodbye
y[3][2]="Goodbye"
print(y)

#inbulit functions for lists
#1.append()
#it adds the element bydefault at the end of list
x=[1,5,6,7,56,"hello","ranjith",True]
x.append('USA')
print(x)
x.append('India')
print(x)

#2.insert()
# it adds the element at the particular position or index
x.insert(5,'Goodbye')
print(x)

#3.remove()
#you have to mention the name of element you want to remove
x.remove('hello')
print(x)
x.remove("India")
print(x)
x.remove(True)
print(x)

#4.pop()
#it removes the last element from the list when we are not giving the index
#it removes the element at the index when you have given the index in ()
x.pop()
print(x)
x.pop(3)
print(x)
x.remove(True)
print(x)

y=[0,5,8,6,8,'hello',9,False,'pune'] #value of True=1,and value of False=0
#y.remove(False)
#print(y)
y.pop(7)
print(y)

y1=[5,8,6,89,'hello',False,'pune',0,12]
y1.remove(False)
print(y1)

#in case of remove if there is a boolean value True or False in the list and
# also having 0 or 1 in the list then it will remove the element whichever
#comes first that 0 or False or 1 or True.

y4=[5,8,6,89,'hello',0,'pune',False,12,0,False]
y4.pop(7)
print(y4)

#5.extend()
#to add or join new list to old list or add two lists together

y=[1,5,6,8,2,23,12,1,78]
z=["hello","bye","ranjith","mumbai","pune"]
y.extend(z)
print(y)

c1=[12,23,56,"hello","pune"]
c2=[1,2,3,"x"]
c1.extend(c2)
print(c1)

#6.count()
y=[85,2,4,"nikhil","Jim",0,"sam",'nikhil',False]
#it counts how many times the element appeared in the list
print(y.count("nikhil"))
print(y.count(0)) #False is counted as 0 because its numeric value is 0
print(y.count(False))

#7.reverse()
#it will reverse the list.
y=[85,2,4,"nikhil","Jim",0,"sam",'nikhil',False]
y.reverse()
print(y)
#print(y[::-1])


#8.sort()
#it will sort the list if the list is particular numbers list,
#or list of string.it does not support combination of both
z=[98,5,45,2,56,1,8,48]
z.sort()
print(z)

d=["mumbai","apple","nikhil","dog","cat"]
d.sort()
print(d)

'''
y=[85,2,4,"nikhil","Jim",0,"sam",0.00256,1,56]
y.sort()
print(y)
'''

#what-is-the-difference-between-sort-and-sorted
"""1.The primary difference between the list sort() function and the sorted() 
function is that the sort() function will modify the list it is called on. 
The sorted() function will create a new list containing a sorted version of
the list it is given.
2.A second important difference is that the sorted() function will return a 
new list so you must assign the returned data to a new variable. 
The sort() function modifies the list in-place and has no return value.
"""
vegetables = ['squash', 'pea', 'carrot', 'potato']
#vegetables.sort()
#print(vegetables)

new_list=sorted(vegetables)
#print(vegetables)
print(new_list)

#9.copy()
d=["mumbai","apple","nikhil","dog","cat"]
h=d.copy()
print(h)

#10.clear()
#it will make the list empty
g=[1,2,3,4,5,6,'hello']
print(g)
g.clear()
print(g)


#Assignment 1
d1=["mumbai","apple","nikhil","dog","cat"]
d2=[98,5,45,2,56,1,8,48]
#ADD d2 TO d1 in reverse order
#answer ["mumbai","apple","nikhil","dog","cat",48,8,1,56,2,45,5,98]
#d2.reverse()
#d1.extend(d2)
#print(d1)
print(d1+d2[::-1])


x1=["gini",'entropy','error','data science']
x2=[89,56,23,45,12,78]
print(x1 +x2[::-1])

#Assignment 2
s="Python"
#dont use inbuilt function replace
#output ="python"
z="hello pune"
print(z.replace("pune",'mumbai'))

x=[1,2,3,"hello"]
x[3]="bye"
print(x)

#z[1:2]="s"
#print(z)

#Immutable Objects or data types :int, float, bool, string, tuple

# mutable Objects or data types : list,dictionary,set

s1="I live in pune"
#s1[2]='L'
print(s1.replace('l','L'))
#Strings are a immutable data types which means that its value cannot be updated.
#we cannot assign a new value to a string


#tuple()
#tuples are immutable.i.e. we cannot change them,we cannot assign a new value to the tuple
#tuples are comma separated.
x=(1,2,45,"hello")
print(type(x))
x1=(20) # this is not a tuple because its not comma seperated
print(type(x1))
x2=(20,) # this is a tuple
print(type(x2))
print(x[3])
#x[3]="bye"
#tuples are immutable because its value cannot be updated

#Dictionary {}
# it is denoted by {}
# its a key-value pair
#key:value
#keys are unique ,dont repeat same key again in the same dictionary
x={"country":"india","capital":"delhi","PM":"Modi","company":"Birlasot"}
print(x["country"])
print(x["PM"])

#.get() method
print(x.get("capital"))
print(x.get("country"))

y={"x":1,"y":2,"z":3}
print(y["x"])
print(y.get("x"))
print(y['z'])
print(y.get('z'))

d2={1:"hello",2:"pune"}
print(d2[1])
print(d2.get(1))

d3={'name':['sam','jim','sana','jack'],'age':[23,12,24,28],
    'location':('pune','mumbai','hyderabad','banglore')}

print(d3['name'])
print(d3['location'][2])

y={"x":1,"y":2,"z":3}
z={1:'x',2:"y",3:"z"}

c={'1':1,'2':2,'3':3}
print(c['3'])

#Assignment 3
d={1:1,2:'2','1':1,'2':3}
d['1']=2
print(d[d[d[str(d[1])]]])
#print(d[1])




y={"x":1,"y":2,"z":3}
#how to print the keys from dict
print(y.keys())
print(d.keys())

#how to print the values from dict
print(y.values())
print(d.values())

#how to print both key and value from the dict
print(y.items()) #answer should be a list of tuples

#how to add new key-value pair to current dictionary
m={"country":"india","capital":"delhi","PM":"Modi"}
m["city"]="Pune"
print(m)
m["state"]="Maharashtra"
print(m)

#how to update the value of dictionary
m["country"]="USA"
print(m)

m={"country":"india","capital":"delhi","PM":"Modi"}

#how to delete the key value from dictionary
#del- to delete the key value pair from the dict
del m['country']
print(m)
del m["city"]
print(m)

# with pop()
m.pop('PM')
print(m)

t={'color':'white','rain':True,'nature':'green','x':56,2:100}
print(t.pop(2))
print(t)

x=[[1,2,3],56,["x","y","z"],{1:'hello',2:'bye',3:'welcome'},1.2356,True,(4,5)]
print(x[3][3])


#how to add 2 dictionaries
d1={"x":1,"y":2,"z":3}
d2={1:"hello",2:"pune",3:"john"}
#syntax - {**d1,**d2,**d3....**dn}
d={**d1,**d2}
print(d)

#how to make a dictionary empty
d1={"x":1,"y":2,"z":3}
d1={}
print(d1)

#.clear method()
d2={1:"hello",2:"pune",3:"john"}
d2.clear()
print(d2)

#how to create a dictionary
dic={}
dic['ice-cream']='strawberry'
dic['data-science']='Python'
dic['Machine-Learning']='Python'
print(dic)

#nested dictionary
my_dict2={'nested':{'name':'nikhil','company':'HCL'},1:100,"city":'banglore'}
print(my_dict2['nested']['company'])

Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1]) #Geeks
print(Dict['Dict2']['Name']) #For

#How to make a dictionary from 2 lists.
name=['Ram','Rex','Raj','Micheal']
age=[24,34,27,31]
#zip function
#it will combine 2 lists and make a tuple
print(dict(zip(name,age)))

v1=[1,2,3,4,5]
v2=['x','y','z','a']
print(dict(zip(v1,v2)))

x1={"a":2,"b":3,"c":8}
x2={"a":10,"m":3,"c":21}
x={**x1,**x2}  #x={"a":10,"b":3,m":3,"c":21}
print(x)
x={**x2,**x1}
print(x) #{"a":2,"b":3,m":3,"c":8}

rosarys_guest = {'adam':2,'rex':4,'rahul':3,'sam':5,'ayushi':1}
taylors_guest = {'adam':1,'nikhil':2,'rex':1,'sam':1,'raj':1}
total_dict1 = {**rosarys_guest,**taylors_guest}
print(total_dict1)

total_dict={**taylors_guest,**rosarys_guest}
print(total_dict)
#if 2 dictionaries have similar keys and if we are adding them then preferrence
#will be given to the value of the dictionary which we are going to add that is
#here we are adding rosarys_guest dictionary to the taylors_guest dictionary
#so the preferrence is given to the values of rosarys_guest dictionary.

#Assignments
L1=[1,2,[3,4]]
L2=[1,2,{"k1":4}]
print(L1[2][0]==L2[2]["k1"])
#3 != 4
# = is the assignment operator
# == is the equality operator
#False

name='Manavlan'
print(name.replace('a','A',2))

'''vowel=['a','e','i','u']
vowel.append(3,'o')
#vowel.append('o')
print(vowel)'''

test={1:'A',2:'B',3:'C'}
del test[1] #{2:'B',3:'C'}
test[1]='D' #{1:'D',2:'B',3:'C'}
del test[2] #{1:'D',3:'C'}
print(len(test))

test={1:'A',2:'B',3:'C'}
test={}
print(len(test))

a={}
a[1]=1
a['1']=2
a[1]=a[1]+1
print(a)

a=[13,56,17]
a.append([87])
a.extend([45,67])
print(a)

x=10
y=38
x,y=y,x
print(f'x = {x}')
print(f'y = {y}')


a="ABCD"
a.replace('AC','XY')
print(a)

#3
a=['50','100','100','200']
a.sort()
b=['2','6','6','5']
b.sort()
print(a)
print(b)

#4
x,*y={1:2,3:4,5:6} #first key goes to x and remaining keys goes to y
print(x)#1
print(y)

a,*b=1,2,3,4 #first value goes to a and remaining values goes to b
print(a)
print(b)

#set{}
#it will remove repetative values and gives unique values from list,tuple,string etc
#it denoted by {}
#it a sequence of unique values and dictionary is a key-value pair.
#it only holds the unique values
x=[5,1,1,1,5,8,9,88,88,5,6]
print(set(x))

z=[78,12,63,'hello','bombay',True,False,'hello',True]
print(z)
print(set(z))


s="apple"
print(set(s)) #{'a','p','l',''e}


s="aabbgihhoov"
print(set(s))

#Remove items 10, 20, 30 from the following set at once
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

#Taking input from user
#input(prompt)
#when we take input from user,python bydefault takes or saves it as a string
'''name=input("Enter your name: ")
print("Hello "+name)
age=input("Enter your age: ")
print("You are "+age)

#take 2 numbers as a input from user and add them and print the result
num1=int(input("Enter first number: ") )#'2'
num2=int(input("Enter second number: ") )#'5'
print(num1+num2)

#a,b,c=10,20,30
#multi-input from user
num1,num2=input("Enter two numbers: ").split()
print(num1,num2)
print(type(num1))
print(int(num1)+int(num2))

x,y,z=input("enter three values: ").split()
print("No.of boys: "+x)
print("No. of girls: "+y)
print("Total No. of candidates: "+z)'''

'''
temp=float(input("Enter temp in celcius: "))
c=(9/5*temp+32)
print("Celcius temperature {} is the same as {} Farenheit.".format(temp,c))
print(f'Celcius temperature {temp} is the same as {c} Farenheit.')

#palindrome
#string which is same from both sides
#madam
#nitin
#take a input from user as a string and check that string is a palindrome or not
string=input("Enter a string: ").lower() #madam
reverse_string=string[::-1]
print(string==reverse_string)'''

'''Write a program that takes as input an Integer s, the number of seconds
elapsed for a certain event. The program converts s to hours (hh), minutes 
(mm), and seconds (ss) and prints the output as hh:mm:ss.'''
#INPUT: 5
#OUTPUT: 0:0:5
#INPUT: 67
#OUTPUT: 0:1:7
#NPUT: 3692
#OUTPUT: 1:1:32
'''
s=int(input("enter the time in seconds: ")) #5010//3600
hh=s//3600 #1
mm=(s-hh*3600)//60 #5010-1*3600=1410//60= 23
ss=s-hh*3600-mm*60 # 5010-1*3600-23*60=30
#hh:mm:ss = 1:23:30
print("The converted time is {}:{}:{}".format(hh,mm,ss))


#if else conditions
#if condition-1:
    #print('something')
#elif condition-2:
    #print('something')
#elif condition-3:
    #print('something)
#else:
    #print('final statement')

#Building Basic Calculator
num1=int(input("Enter first number: ")) #10
operator=input("Enter operator: ") # "+"
num2=int(input("Enter second number: ")) #20
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator=="%":
    print(num1%num2)
else:
    print("Invalid operator!!")

#logical operators
#and or
#and operator = when both conditions want to be True
#or opearator = when any one of two conditions want to be true
'''
#this is not a code, it is for undestanding the and or
'''if operator=="+" and num1==10:
    print("something1")'''

'''if operator=="+" or num1==10:
    print("something2")'''

'''
#print max number from 3 given numbers
num1=int(input("enter first number: "))#10
num2=int(input("enter second number: "))#45
num3=int(input("enter third number: "))#200
if num1>num2 and num1>num3:
    print(f"{num1} is maximum")
elif num2>num1 and num2>num3:
    print(f"{num2} is maximum")
else:
    print(f"{num3} is maximum")

x=[1,2,3,"hello","pune",2.3,5.2,100,89]
for element in x:
    if type(element)==int:
        print(element)
'''

c='ramesh, mahesh, suresh'
print(c[7:-9]) #positive start index and -ve end index then that will work
print(c[-7:9]) #-ve start index and +ve end index then that will not work
print(c[8:14])
print(c[-14:-8])

#for loop
#iterative loop it will do same action again and again
#s='pune'
s=[1,2,2,3]
for letter in s:
    print(letter)

y=[23,56,'hello','pune','john',100]
for element in y:
    print(element)

d=[1,2,3,4,5]
for number in d:
    print(number+10)

for number in d:
    if number==3:
        break
    print(number**2) #1,4

#this method is not useful
'''
k="sagar"
for letter in k:
    print(letter,end=" ")
'''

#range inbuilt fuction in for loop
for number in range(0,11):
    print(number)


for number in range(5,11,1):
    print(number**2)

for number in range(0,10,-1):
    print(number) #it will not give any output

for number in range(10,0,-1):
    print(number)

for number in range(-1,-10,-1): #-1, -1-1=-2,-2-1=-3
    print(number)

#if we go with negative stepsize,we will take (stop index+1)

for number in range(5,11,1):
    print(number**2)

for number in range(11,5,-1):
    print(number**2)

c='42356'
for num in c:
    print(num)

d=("mumbai",12,45,"pune",89)
for element in d:
    print(element)

x=[1,2,3,5,6,8,9]
print(len(x)) #7
for i in range(0,len(x)):
    print(i)


#we cannot use for loop on interger or float value
#scaler data type- integer,float,bool,None #it is a fixed value and does not have internal part
#non-scaler data types- str,list,tuple,dictionary,set

print([2]*10)
print([2,2]*10)


k=[2]
#print(k[2])
for num in k:
    print(k*10)


#Write a Python program to find sum of elements in list?
x=[1,2,3,4,5,6,7,8,9] #output = 45
sum=0
for element in x:
    sum=sum+element #sum=0+1=1,sum=1+2=3,sum=3+3=6,sum=6+4=10,sum=10+5=15,
    #sum+=element               #sum=15+6=21,sum=21+7=28,sum=28+8=36,sum=36+9=45
print(sum)

#sum += element means sum=sum+element
#sum -= element means sum=sum-element
#sum *= element means sum=sum*element
#sum /= element means sum=sum/element

#Write a Python program to Multiply all numbers in the list?
y=[1,2,3,4,5] #output =120
total=1
for element in y:
    total=total*element #total=1*1=1,total=1*2=2,total=2*3=6,total=6*4=24,total=24*5=120
print(total)

total=1
for element in y:
    total*=element
print(total)

#print all the even numbers between 0 to 50 using for loop
for number in range(0,51):
    if number%2==0:
        print(number)

# != not equal to

#print all the odd numbers between 0 to 50 using for loop
for number in range(0,51):
    if number%2 != 0:
        print(number)

x='leena'
for pune in range(0,5):
    print(x)

#for loop for dictionary
r={"x":1,"y":2,"z":3}
print(r.keys())
for key in r.keys():
    print(key)

print(r.values())
for value in r.values():
    print(value)

#for taking key:value in for loop
for item in r.items():
    print(item)


#for loop using append function ,output should be a list
x="sagar"
for letter in x:
    print(letter)

my_list=[]
x="sagar"
for letter in x:
    my_list.append(letter)
print(my_list)


#for i in range(15,3,-3): #add 1 to the stop range that wil be your stop index i.e.4 here
    #print(i,end=' ')

#for i in range(1,10,3): #add -1 to the stop range that wil be your stop index i.e.9 here
    #print(i,end=' ')

x="sam print only the words that starts with 's' in this sentence."
s=x.split()
print(s)
for word in s:
    if word.startswith("s"):
        print(word)

for word in s:
    if word[0]=="s":
        print(word)

s="print every word in this sentence that has an even number of letters"
x=s.split()
print(x)
for word in x:
    if len(word)%2==0:
        print(word)

s="print every word in this sentence that has an even number of letters"
s=s.split()
mylist=[]
for word in s:
    if len(word)%2==0:
        mylist.append(word)
print(mylist)


#FizzBuzz
# write a python programme that prints integers from 1-100 .but for
#multiples of 3 print 'Fizz' instead of number ,for multiples of 5
# print 'Buzz'.for numbers multiles of both 3 & 5 print 'FizzBuzz'.
for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FIZZBUZZ")
    elif number%3==0:
        print("FIZZ")
    elif number%5==0:
        print("BUZZ")
    else:
        print(number)


#find the maximum number from the given list using for loop
x=[12,45,1,23,89,0,575,78,3,200]
max_num=x[0] #12
for number in x:
    if number>max_num:
        max_num=number #max_num=45,89,575
print(max_num)



phone_number=input("Enter your phone number: ") #'8237198953'
d={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
   '7':'seven','8':"eight","9":"nine"}
output=""
for number in phone_number:
    output=output+d.get(number)+" "  #""+"eight"="eight ","eight "+"two"
print(output)

#write a python program to find the sum of sqaures of only the postive
# integers from the list that are divisible by 3 or 7
x=[2,-3,14,-6,3,9,'pune','hello',True]
#positive intergers (2 conditions - type should be integer,num>0)
#check divisible by 3 or 7
#squares of numbers obtained
#sum of that squares
sum=0
for number in x:
    if type(number)==int and number>0: #2,14,3,9
        if number %3==0 or number%7 ==0:
           sum=sum+ number**2 #sum=0+196=196,sum=196+9=205,sum=205+81=286
print(sum)


#break and continue keyword
#break keyword
for num in range(1,10):
    print(num) #1,2,3,4,5
    if num==5:
        break

#else clause for for & while loop
#after executing whole for loop,it comes to else part and execute it.
#if the for loop  breaks before executing whole, then it will not
#execute the else part

for num in range(1,10):
    print(num)
else:
    print("comes to else after executing whole for loop")

for num in range(1,10):
    print(num) #1,2,3,4,5
    if num==5:
        break
else:
    print("it will not comes to else part because for is breaked")


x=[1,2,3,'hello',2.3]
for i in x:
    if type(i)==float:
        print(i) #2.3
else:
    print('no element is of type float')


x=[1,2,3,'hello']
for i in x:
    if type(i)==int:
        print(i) #1,2,3
else:
    print('no element is of type float')

#continue keyword
#it will skip the part of code where is condition is satisfied
for num in range(1,7):
    if num%2==0:
        continue #it will skip the code after continue
    print(num) #1,3,5

for num in range(1,7):
    if num%2==0:
        break
    print(num)


for num in range(1,10):
    if num==4:
        continue
    print(num+10) #11,12,13,15,...19

#pass keyword
#it will not execute anything

#write a python program to find how many uppercase and lowercase letters are
#there in the string.
x="I live in Pune and Pune is a great city"
upper=0
lower=0
for letter in x:
    if letter.isupper():
        upper=upper+1
    elif letter.islower():
        lower=lower+1
    else:
        pass
print(f'The number of lowercase letters is {lower}')
print(f'The number of uppercase letters is {upper}')

#pangram
#pangram is sentence which contains all alphabets from a to z
#The quick brown fox jumps over the lazy dog
#write the python program to check whether the given string is pangram or not
alphabets="abcdefghijklmnopqrstuvwxyz"
x="The quick brown fox jumps over the lazy dog"
#x="I live in pune"
for letter in alphabets:
    if letter not in x.lower():
        print("the string is not a pangram")
        break
else:
    print("The string is a pangram")

#write a python program to find those numbers which are divisible by 7 and
#multiple of 5 between 1500 and 2700(both include)
for number in range(1500,2701):
    if number%7==0 and number%5==0:
        print(number)


#write a python program to count how many times each letter appears in a string.
z="pune is well known for historical reasons."
#output={"p":1,"u":1,"n":4,"e":3,"":6,"i":3,"s":4,"w":2,"l":3,"k":1,"o":4
# "f":1,"r":3,"h":1,"t":1,"c":1,"a":2,".":1}
d={}
for letter in z:
    if letter not in d.keys():
        d[letter] = 1
    else:
        d[letter] =d[letter]+1
print(d)

#Nested for loop
#in this case the value of outer for loop remains the same till the inner loop is
# executed completely
for x in range(0,5):
    for y in range(0,3):
        print(x,y)
#(0,0)
#(0,1)
#(0,2)
#(1,0)
#(1,1)
#(1,2)
#(2,0)
#(2,1)
#(2,2)
#(3,0)
#(3,1)
#(3,2)
#(4,0)
#(4,1)
#(4,2)

#m=[[1,2,3],[4,5,6],[7,8,9]]
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for element in row:
        print(row,element)
#[1,2,3],1
#[1,2,3],2
#[1,2,3],3
#[4,5,6],4
#[4,5,6],5
#[4,5,6],6
#[7,8,9],7
#[7,8,9],8
#[7,8,9],9

#draw F-shape using for loop
'''
xxxxx
xx
xxxxx
xx
xx
'''
s=[5,2,5,2,2]
for number in s:
    print(number*"x")

x=int(input("Enter row number=")) #4
for i in range(x): #(0,4)
    for j in range(i+1):#(0,1),(0,2),(0,3),(0,4)
        print("*",end='')
    print("") #print() takes you to the new line
#*
#**
#***
#****

num=int(input("Enter row number=")) #4
for i in range(num,0,-1): # (4,0,-1)
    for j in range(0,num-i): #(0,0),(0,1),(0,2),(0,3)
        print(end=" ") #0,1,2,3

    for j in range(0,i): #(0,4),(0,3),(0,2),(0,1)
        print('*',end=" ") #* * * *

    print()

#* * * *  #0 space
# * * *   #1 space,3*
#  * *    #2 space ,2*
#   *     #3 space,1*

#task
#   *         #3 space,1*
#  * *         #2 space ,2*
# * * *       #1 space,3*
#* * * *     #0 space

#problem1

n=4
ans=""
for i in range(1,n+1): #(1,5)
    ans+=str(i)*i+"\n"   #ans=ans+str(i)*i+"\n"  ,ans=""+str(1)*1=""+"1"="1"+\"n"
                        #ans=""+str(2)*2+"\n"=""+"22"="22"+"\n"
print(ans)
#1
#22
#333
#4444
#print(ans[:-1])

#print(str(2)*2)

'''
#prob2
l=[11,22,33]
l[3]=13
#print(l)
print(max(l))
'''


#prob4
d={0:11,1:22,2:33}
s=0
for i in d:
    s+=i #s=s+i ,s=0+0=0,s=0+1=1,s=1+2=3
print(s) #3

#P
#P y
#P y t
#P y t h
#P y t h o
#P y t h o n
'''
s='neccessary'
print(*s[1:5]) #* is for giving space between the letters
text = input('Enter a string: ') #Python
for index in range(len(text)): #(0,6)
    print(*text[:index + 1]) #text[:1]=P,text[:2]=Py,text[:3]=Pyt,text[:4]=Pyth,
    # text[:5]=pytho,text[:6]=python


text = input('Enter a string: ') #Python
for index in range(0,len(text)): #(0,6)
    print(text[0:index + 1]) #text[0:1]=P,text[0:2]=Py,text[0:3]=Pyt,text[:4]=Pyth,

#d="sagar"
#print(*d)

#while loop
#conditional loop
for number in range(0,5):
    print(number)

number=0
while number<5:
    print(number) #0,1,2,3,4
    number=number+1 #number=0+1=1,number=1+1=2,3,4,5


#else clause
i=0
while i<10:
    print(i)#0,1,2,3,4,5,6,7,8,9
    i+=1 #i=i+1,i=0+1=1,2,3,4,5,6,7,8,9,10
else:
    print("whole while loop executed!")

i=0
while i<=5:
    print(i) #0,1,2,3
    if i ==3:
        break
    i+=1 #i=i+1,i=0+1=1,2,3
else:
    print("it does not goes in while loop")

#Guessing number game using while loop
secret_number=10
guess_limit=3
guess_count=0
while guess_count<guess_limit:
    guess=int(input("Enter Guess: ")) #5,7,8,'10'
    guess_count= guess_count+1  # 0+1=1,2,3
    if secret_number==guess:
        print("You win!")
        break
else:
    print("You loose!")

#fibonicci series
#next number is the sum of previous 2 numbers
#0,1=1,1,3,5,8,13,21,35,56

a=0
b=1
while b<100:
    print(b) #1,1,2,3,5,8,13,21,34,55,89
    a,b=b,a+b #(1,1),(1,2),(2,3),(3,5),(5,8),(8,13),(13,21),(21,34),(34,55),(55,89)


#IMP
#reverse number
x=int(input('enter the number you want to reverse: '))#123456
#x=123456
reverse=0
while x>0:
    remainder = x % 10  # 6,5,4,3,2,1
    reverse=(reverse*10)+remainder #reverse=0+6=6,6*10+5=65,65*10+4=654,654*10+3=6540+3=6543,6543*10+2=65432,65432*10+1=654321
    x=x//10  #x=123456//10=12345//10=1234//10=123//10=12//10=1//10=0
print(reverse)


#counting number of digits in a given number and the total sum of digits
x=123456
#output= count of digits=6,total sum of digits=21
count=0
total=0
while x>0:
    remainder = x % 10  # 6,5,4,3,2,1
    count=count+1   #0+1=1+1=2+1=3+1=4+1=5+1=6
    total = total + remainder  # 0+6=6+5=11+4=15+3=18+2=20+1=21
    x = x // 10  # x=123456//10=12345//10=1234//10=123//10=12//10=1//10=0
print(f'Count of digits is {count}')
print(f'Total sum of digits is {total}')
'''
"""
command=""
while command !="quit":
    command=input("Enter your command: ")# f
    if command=="start":
        print("Car is Started!")
    elif command=="stop":
        print('car is stopped!')
    elif command=="help":
        print(
            '''
start=to start the car
stop= to stop the car
quit= to exit
            ''')
    elif command=="quit":
        break
    else:
        print("Invalid command")
"""

x=0
a=5
b=5
if(a>0):
    if (b<0):
        x=x+5
    elif(a>5):
        x=x+4
    else:
        x=x+3 #x=0+3=3
else:
    x=x+2
print(x)

#add all elements in the list and give the total
x=[1,2,3,5,7,9,6]
total=0
for element in x:
    total=total+element
print(total)


#while True
#https://www.freecodecamp.org/news/python-while-loop-tutorial/
#it will create a infinite loop so we have to manually break the loop using break
# Define a variable
i = 5
# Run this loop while i is less than 15
while i < 15:
    # Print a message
    print("Hello, World!")
    break
#every time value of i remains the same i.e i=5

#How to Make an Infinite Loop with While True
while True:
    print('hello, World!')
    break

'''
while True:
    # Code
    if <condition>:
    	break
    # Code
'''
'''
while True:
    user_input = int(input("Enter an integer: "))#3,2
    if user_input % 2 != 0:
        print("This number is odd")
        break


    else:
        print("This number is even please try again!")

x="sudarshan"
first_letter=x[0]
mid_letter=x[floor(len(x)/2)]
last_letter=x[-1]
print(first_letter+mid_letter+last_letter) #srn
'''
#While loop real life example
# statement= while I do not clear the cutoff I will keep on giving my exams
cutoff=400
scores=[100,200,300,399,500]    #scores I got every year
year=0   #indexing in python starts with 0
while scores[year] < cutoff:
    print(f"Your score is :{scores[year]}/1000,cutoff:{cutoff}")
    print("I will attempt next year")
    print("------")
    year=year+1   #adding 1 to current year
else:
    print("Congrats! You have cleared the cutoff")
    print(f"Finally I have cleared my exams after {year+1} attempts")


#Error Handling (try and except)
'''
try:
    number=int(input("Enter a number: ")) #5,a
    print(number)
except:
    print("you entered a wrong value")


try:
    number=int(input("Enter a number: ")) #5,a
    print(number)
except Exception as e:
    print(e)

try:
    x=10
    y=0
    print(x/y)
except:
    print("You cannot divide any number by zero")

try:
    for x in ['a','b','c','d']:
        print(x**2)
except TypeError as e:
    print(e)
finally:
    print('The code finally executed without error!')

try:
    while True:
            user_input = int(input("Enter an integer for input: "))#3,2
            if user_input % 2 == 0:
                print("This number is even")
                break
            else:
                print("This number is odd please try again!")
except Exception as e:
    print(e)


while True:
    try:
        number=int(input("Enter an integer number for an input: "))#5,6
        print(number) #5,6,a
        break

    except ValueError:
        print("Whoops! thats not a number try again")
        continue


#with else part
#it will go to else part when try block runs without error
while True:
    try:
        number = int(input("enter a number: "))
        print(number)

    except:
        print("whoops! thats not a number.please try again")
        continue
    else:
       print("yes thats a number.thank you")
       break
'''

#to check how many times each letter appears in a piece of text
#input= "aaaa"
text="I am in pune from last 7 years."
x={"i":2,"a":1,"m":1}
for letter in text.lower():
    if letter==" ":
        continue
    elif letter not in x.keys():
        x[letter]=1
    elif letter in x.keys():
        x[letter] += 1
    else:
        pass
print(x)

text="I am in pune from last 7 years."
x={"i":2,"a":1,"m":1}
for letter in text.lower():
    if letter.isalpha():
        if letter not in x.keys():
            x[letter]=1
        elif letter in x.keys():
            x[letter] += 1
        else:
            pass
print(x)


#list comprehension
#list comprehension is a unique way of quickly creating a list with python.
#If we are using for loop along with append function to create a list then
#list comprehension is the better choice.
y='mumbai'
mylist=[]
for letter in y:
    mylist.append(letter)
print(mylist)

#with list comprehension
a=[letter for letter in y]
print(a)


for num in range(1,10):
    print(num)

#with append function
my_list2=[]
for num in range(1,10):
    my_list2.append(num)
print(my_list2)

#with list comprehension
b=[num for num in range(1,10)]
print(b)

#create a list of squares of all numbers between 1 to 20 in python with list
# comprehension.
#without list comprehension
g=[]
for num in range(1,21):
    g.append(num**2)
print(g)

#with list comprehension
c=[num**2 for num in range(1,21)]
print(c)

#create a list of all even numbers between 1 to 20 with list comprehension
#without list comprehension
my_list3=[]
for num in range(1,21):
    if num%2==0:
        my_list3.append(num)
print(my_list3)

#with list comprehension
d=[num for num in range(1,21) if num%2==0 ]
print(d)


#with list comprehension
d=[num**2 for num in range(1,21) if num%2==0 ]
print(d)

#without list comprehension
celcius=[0,10,30,34.5]
#farenheit=(9/5)*temp in celcius + 32
list4=[]
for temp in celcius:
    list4.append((9/5)*temp+32)
print(list4)

#with list comprehension
e=[(9/5)*temp+32 for temp in celcius]
print(e)

#use list comprehension to create a list of all numbers btn 1 & 50
#that are divisible by 3
f=[num for num in range(1,51) if num%3==0]
print(f)

#list comprehension with nested for loop
for x in [2,4,6]:
    for y in [100,200,300]:
        print(x,y)
#(2,100)(2,200)(2,300)(4,100)(4,200)(4,300)(6,100)(6,200)(6,300)

#without list comprehension
h=[]
for x in [2,4,6]:
    for y in [100,200,300]:
        h.append(x*y)
print(h)
#(200,400,600,400,800,1200,600,1200,1800)

#with list comprehension
k=[(x*y) for x in [2,4,6] for y in [100,200,300]]
print(k)

#without list comprehension
s='print every word in this sentence that has an even number of letters'
list6=[]
for word in s.split():
    if len(word)%2==0:
        list6.append(word)
print(list6)

#with list comprehension
p=[word for word in s.split() if len(word)%2==0]
print(p)


#fizbuzz with list comprehension
mylist2=[]
for num in range(1,21):
    if num%3==0:
        mylist2.append('Fizz')
    else:
        mylist2.append('Buzz')
print(mylist2)

mylist2=['Fizz' if num%3==0 else 'Buzz' for num in range(1,21)]
print(mylist2)

#PEP8 = Python Enhancement Proposal
#It is set of rules to write neat and clean Python code.
#Keep 2 spaces between 2 functions
#functions
#its just a collection of code to avoid the repetative code
#built-in functions
#user-defined functions
def Intro():  #function definition
    print("Hello world")

Intro()  ##calling the function

def Intro(name):
    print("Hello "+name)
Intro('nikhil')
Intro('sagar')

def Introduction(name,age):
    print("Hello "+name+" you are "+str(age))
Introduction('sagar',25)

#parameter is the value passed to the func when defining a function,e.g-name,age
#argument is the actual value passed to func when we call the func-e.g-sagar,25

def square(num):
    print(num**2)
square(10)

x="sagar"
part1=x[0:3]
part2=x[3:]
print(part1.capitalize()+part2.capitalize())

def first_fourth_letter_capitalize(x):
    part1 = x[0:3]
    part2 = x[3:]
    print(part1.capitalize() + part2.capitalize())
first_fourth_letter_capitalize("nikhil")
first_fourth_letter_capitalize("sudarshan")

#return keyword
#function bydefault returns None if we are not returning anything
#from the function
#return keyword can basically allow python to return information(output)
#from a function

def cube(num):
    return num*num*num
print(cube(3))

#write a python function to capitalize first and fourth letter of the word.
#nikhil=NikHil
def capitalize_first_fourth_letter(word):
    first_letter = word[0] #n
    in_between= word[1:3] #ik
    fourth_letter = word[3] #h
    rest = word[4:] #il
    return first_letter.upper()+in_between+fourth_letter.upper()+rest
print(capitalize_first_fourth_letter('nikhil'))
print(capitalize_first_fourth_letter('sarthak'))

def sum(x,y):
    return x+y
print(sum(3,4))

def subtract(a,b):
    return a-b
print(subtract(10,5))
'''
#write a python function to calculate no.of uppercase and lowercase
#letters in a string
def Uppercase_Lowercase(string):
    upper = 0
    lower = 0
    for letter in string:
        if letter.isupper():
            upper = upper + 1
        elif letter.islower():
            lower = lower + 1
        else:
            pass
    return "no. of uppercase letters: "+str(upper),"no. of lowercase letters: "+str(lower)
print(Uppercase_Lowercase("I live in Pune"))
print(Uppercase_Lowercase("Mumbai and Pune are the Metro cities"))


#vowels=a,e,i,o,u
#pig-latin
#if the word starts with a vowel ,add 'ay' to end of word.if the
#word does not starts with a vowel ,put first letter at the end
#of the word and then add 'ay'
#vowels=a,e,i,o,u
#e.g. apple=appleay,umesh=umeshay
# word=ordway,nikhil=ikhilnay
#harshal=arshalhay
def pig_latin(word):
    first_letter = word[0] #a
    if first_letter in "aeiou":
        pig_word=word + "ay"
    else:
        pig_word=word[1:]+first_letter+"ay"
    return pig_word
print(pig_latin("apple"))
print(pig_latin("pune"))


#palindrome
#madam
#write a python function to check the given string is palindrome or not
def palindrome(string):
    reverse_string=string[::-1]
    if string==reverse_string:
        print("The given string is a palindrome!")
    else:
        print("The given string is not a palindrome!")
palindrome("madam")
palindrome("pune")

#write a python func to check if the string contains duplicate
#values or not
#e.g.string="dkjjjdfsd"
#print duplicates found
#string="asdfghjkl"
#print "all unique"
def duplicate_finder(string): #set(abbbcd)=abcd=len(abcd)=4
    if len(string) == len(set(string)):
        return "All Unique"
    else:
        return "Duplicates Found"
print(duplicate_finder("madam"))
print(duplicate_finder("pune"))


#sentence,word
#pune is a nice city,nice
#output= pune is a NICE city
def highlight_word(sentence,word):
    return sentence.replace(word,word.upper())
print(highlight_word("pune is a nice city","nice"))
print(highlight_word("mumbai and pune are metro cities","metro"))

#write a python function to replace vowels in word by letter 'g'
#vowels=a,e,i,o,u
#nikhil =ngkhgl
#yogesh=ygggsh
#pune=pgng
def translate(word): #pune
    translate=""
    for letter in word:
        if letter in "aeiou":
            translate =translate + "g"
        else:
            translate = translate + letter #translate=""+"p"="p"+"g"="pg"+"n"="pgn"+"g"="pgng"
    return translate
print(translate("pune"))
print(translate("yogesh")) #ygggsh

## write a python function to check the given number is in range or not
#num,low range,high range
#5,1,15
def range_check(num,low,high):
    if num in range(low,high):
        return f"{num} is in the range"
    else:
        return f"{num} is out of range"
print(range_check(10,1,15))
print(range_check(100,1,15))

def prime_check(num):#7
    if num==1:
        return False
    if num==2:
       return True
    for x in range(2,num): #(2,7)
        if num%x==0: #7%2!=0,7%3!=0,7%4 !=0,7%5!=0,7%6!=0
            return False
    else:
        return True
print(prime_check(11))
print(prime_check(1))
print(prime_check(100))

def prime_check(num):#11
    if num==1:
        print("1 is not a prime number")
    if num==2:
        print("2 is a prime number")

    for x in range(2,num): #6
        if num%x==0:
            print(f"{num} is not a prime number")
            break
    else:

        print(f"{num} is  a prime number")
prime_check(9)

#1. Write a Python program to find words which are greater than
# given length k?
def words_greater_than_given_length(sentence):
    words=[]
    x = sentence.split() #list of words
    k=int(input("Enter the given length: "))
    for word in x:
        if len(word)>k:
            words.append(word)
    print(words)
words_greater_than_given_length("I am in pune last eight years")

#2. Write a Python program for removing i-th character from a string?
def removing_ith_character(string):
    s = string.split(" ")
    # s=["hello","this","is","mumbai"]
    index = int(input("Enter position: "))  # 1
    for word in s:
        if s[index] == word:
            s.remove(word)
    sentence = " ".join(s)
    return sentence
print(removing_ith_character("hello this is mumbai"))

#Write a Python program to find uncommon words from two Strings.
#remove comman words from the 2 strings
#"I am in pune"
#"I am in mumbai"
def uncommon_words():
    string1 = str(input("Enter String 1: "))
    string2 = str(input("Enter String 2: "))
    a = string1.split() #["I","am","in","pune"]
    b = string2.split() #["I","am","in","mumbai"]
    print(a, "\n", b)
    UC = []
    for word in a:
        if word not in b:
            UC.append(word)
    for word in b:
        if word not in a:
            UC.append(word)
    print(UC)
uncommon_words()

## Write a Python program to find all duplicate characters in string.
def duplicate_characters(string):

    char = []
    duplicate = []
    for i in string:
        if i not in char:
            char.append(i)
        else:
            duplicate.append(i)
    #print(duplicate)
    print("Duplicate characters are: ", set(duplicate))
duplicate_characters("hello pune")
duplicate_characters("I live in pune and pune is a metro city")

#Write a Python Program to check if a string contains any special character?
def checking_special_characters(string): #"hello@pune"
    spl_char = '[@_!#$%^&*()<>?/\|}{~:]'
    x=[]
    for char in string:

        if char not in spl_char:
            continue
        else:
            x.append(char)
    return "Special Char found in given string are: ", x
print(checking_special_characters("hello@pune"))

#Write a Python program to Extract Unique values from dictionary values?
# d = {'511': 'Vishnu', '512': 'Vishnu', '513': 'Ram', '514': 'Ram', '515': 'sita'}
def Extract_unique_values(d):
    #d = {'511': 'Vishnu', '512': 'Vishnu', '513': 'Ram', '514': 'Ram', '515': 'sita'}
    l = []
    for val in d.values():
        if val in l:
            continue
        else:
            l.append(val)

    print(l)
Extract_unique_values({'511': 'Vishnu', '512': 'Vishnu', '513': 'Ram', '514': 'Ram', '515': 'sita'})

#2. Write a Python program to find the sum of all items in a dictionary?
d = {'a':[100,101],'b':[102,103],'c':[104,105]}
l = []
for i in d.values():
    for j in i:
        l.append(j)
del sum
print(sum(l))
'''
#7. Write a Python program to sort Python Dictionaries by Key or Value?
d = {'a': 1000, 'f': 200, 'd': 300, 'c': 400, 'b': 500, 'e': 600}
sort = sorted(d.keys())
sort1 = sorted(d.values())
print("Sorted by key: ",sort)
print("Sorted by value: ",sort1)
"""
Q.1. Write a program that calculates and prints the value according to the 
given formula:
Q = Square root of [(2 C D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a 
comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to 
the program:
100,150,180
The output of the program should be:
18,22,24
"""
'''
D = [int(i) for i in input("Enter values:\n").split(',')]#[1,2,3,4,5]
C = 50
H = 30
E = []
for j in range(0,len(D)): #(0,5)
    Q = ((2 * C * D[j]) / H) ** 0.5  # Q=sqrt(2*50*1/30)
    E.append(floor(Q))
print("Output:",E)
'''
#IMP
#A namespace is a system that has a unique name for each and every object in
# Python. An object might be a variable or a method. Python itself maintains
# a namespace in the form of a Python dictionary.
## Types of namespaces :
# built-in namespaces e.g print()
# local namespaces #user defined
# global namespaces #user defined
# Scope refers to the coding region from which a particular Python object is
# accessible. Hence one cannot access any particular object from anywhere
# from the code, the accessing has to be allowed by the scope of the object.

#local variable and global variable in function
#local variables
#it is defined inside a function and its scope is limited to that
#function only.

#global variables
#it is defined outside a function and it is accessible to all the
#functions upto end of project or we can access it anywhere in the code.

x=8 #global variable
def square(num):
    x=3 #local variable
    return x*num
print(square(5))

a=5 #global
def square(num):
    a=2 #local variable
    return num+a
print(square(3))

def subtract(num):
    return x-num
print(subtract(2)) #8-2=6

#if you want to make local variable as global you can use the keyword global
def cube(num):
    global a
    a=2
    return num-a
print(cube(20)) #20-2=18

def multiply(num):
    return num*a
print(multiply(3)) #3*2=6

#LEGB RULE: #L=local,E=enclosed,G=global,B=built-in
x=50
def func(x):
    x=10
    print(f'x is {x}')
    x=200
    print(f'I just locally changed x to {x}')
func(x)

name="This is a global string"
def greet():
    #name="sammy"
    def hello():
        name="nikhil"
        print("hello "+name)
    hello()
    print("hello " + name)
greet()


#4 types of arguments
#1.position argument:
def person(name,age):
    print(name)
    print(age)
person("nikhil",20)

#2.keyword argument
def person(name="nikhil",age=23):
    print(name)
    print(age)
person()

#3.default argument
def person(name,age=18):
    print(name)
    print(age)
person("john")
person("sam")

#4.variable length argument
'''def sum(a,*b): #* means multiple arguments
    c=a+b
    print(c)
sum(5,6,34,78) #a=5,b=(6,34,78)'''

#5 is assigned to a and remaining values assigned to b
#a=5 b=(6,34,78)
def sum(a,*b):
    c=a #c=5
    for i in b:
        c=c+i #c=5+6=11,c=11+34=45,c=45+78=123
    print(c)
sum(5,6,34,78)

def plus(*x): #* denotes multiple values
    total=0
    for i in x:
        total=total+i
    return total
print(plus(20,30,40,50)) #x=(20,30,40,50)

# *args- we use this when we are not sure how many arguments are going to be
#passed to a function or if we want to pass a stored list or a tuple of arguments
# to a function.

'''
Question 4:
Write a Python program that accepts a sequence of whitespace separated words as 
input and prints the words after removing all duplicate words and sorting 
them alphanumerically.Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world


words = [str(i) for i in input("Enter words:\n").split(' ')]
words.sort()
c = []
for k in words:
    c.append(k)
print(c)
#['again', 'and', 'and', 'hello', 'hello', 'makes', 'perfect', 'practice',
# 'world', 'world']

alphanum = []
for word in c:
    if word not in alphanum:
        alphanum.append(word)
print()
print("Alphanumerically sorted words are as follows:")
for j in alphanum:
    print(j,end = " ")
'''
'''
Question 3:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
6.At least 1 spl character should be there.
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
'''
#password validation
passwords = [str(i) for i in input("Enter passwords:\n").split(",")] #"Abc@112"
spl_char = ["$", "#", "@"]
correctpass = []
for i in passwords:
    if (len(i) < 6 or len(i) > 12):
        continue
    if (i.isupper() or i.islower()):
        continue
    num = any(j.isdigit() for j in i)
    if (not num):
        continue
    spl = any(j in spl_char for j in i)
    if (not spl):
        continue

    correctpass.append(i)
print()
print("Correct password is: ")
for k in correctpass:
    print(k, end=" ")
'''

#Lambda function/keyword

#lambda is a anonymous function often used as inline function which
#does not need a name and it is returned at runtime.
#lambda is an ananomous function that is without name and it can be
#called at runtime
def add(a,b):
    return a+b
print(add(5,4))

a1=lambda a,b:a+b
print(a1(5,4))

def square(num):
    return num**2
print(square(5))

b1=lambda num:num**2
print(b1(5))

def sum(num):
    return num+10
print(sum(5))

c1=lambda num:num+10
print(c1(5))

def length_string(string):
    if len(string) % 2 == 0:
        return "even"
    else:
        return string[0]
print(length_string("yogesh")) #even
print(length_string("sam")) #s

d1=lambda string:'even'if len(string) % 2 == 0 else string[0]
print(d1("yogesh"))
print(d1("sam"))

def check_even(num):
    return num % 2 == 0
print(check_even(9)) #False
print(check_even(6)) #True

e1=lambda num:num % 2 == 0
print(e1(9)) #False


#map function
def square(num):
    return num**2
#print(square([1,2,3,4,5,6]))
mynum=[1,2,3,4,5,6]
print(list(map(square,mynum)))

print(list(map(lambda num:num**2,mynum)))

def length_string(string):
    if len(string) % 2 == 0:
        return "even"
    else:
        return string[0]
#print(length_string(["kirti","sudhir","mayuri","sonal","bhagyashri","leena"]))
names=["kirti","sudhir","mayuri","sonal","bhagyashri","leena"]
print(list(map(length_string,names)))

print(list(map(lambda string:"even" if len(string) % 2 == 0 else string[0] ,names)))


mynames=["Andy","Eve","Sam","John","Rohit"]
x=[]
for name in mynames:
    x.append(name[0])
print(x)

def first_letter(name):
    return name[0]
print(list(map(first_letter,mynames)))

print(list(map(lambda name:name[0],mynames)))


#filter function
def check_even(num):
    return num % 2 == 0
mynums=[1,2,3,4,5,6]
print(list(map(check_even,mynums)))
print(list(filter(check_even,mynums)))
print(list(filter(lambda num:num % 2 == 0,mynums)))

def CheckLeap(Year):
  # Checking if the given year is leap year
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Given Year is a leap Year")
  # Else it is not a leap year
  else:
    print ("Given Year is not a leap Year")
CheckLeap(2000)

def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(leap_year(2000))


#enumerate function
#it prints the element with its index in for loop and output is in tuple
x="kirti"
for letter in x:
    print(letter)

print(enumerate(x))
for letter in enumerate(x):
    print(letter)

d=[2,56,78,"hello"]
print(enumerate(d)) #(0,2),(1,56),(2,78),(3,"hello")
for tuple in enumerate(d):
    print(tuple)

#zip function
#it zips together 2 lists
l1=[1,2,3,4]
l2=["a","b","c","d"]
print(zip(l1,l2)) #(1,"a"),(2,"b"),(3,"c"),(4,"d")
for tuple in zip(l1,l2):
    print(tuple)


#input & output/ File handling in python
#Reading from a external file


#there are 4 modes of opening the file
#1.open("employee.txt","r") #read only mode/it only reads the file
#2.open("employee.txt","a") #append mode/it adds the info to the end
#of file
#3.open("employee.txt,"w") write mode/it adds the new info to the file
# but it overwrites the file
#4.open("employee.txt","+r") #read and write mode

#There are 4 functions in read mode.
#1.readable()
#it shows file is readable or not
#employee_file=open("employee.txt","r")
#print(employee_file.readable())

#2.read()
#it reads all the information in the file
#print(employee_file.read())

#3.readline()
#it reads the info line by line from start to end,one line at a time
#print(employee_file.readline())
#print(employee_file.readline())

#4 readlines()
#it reads the particular line in the file
#print(employee_file.readlines()[3])
#employee_file.close()


# open the file with "with" keyword
#with open("employee.txt","r") as employee_file:
    #print(employee_file.read())

#it automatically close the file ,you dont have to close manually

#writing information into external file from current python file

#employee_file=open("employee.txt","a")
#employee_file.write("\nAnna=Data Scientist")
#employee_file.write("\nDavid = Data Analyst")

#employee_file=open("employee.txt","w")
#employee_file.write("Robert=Google engineer")

#employee_file=open("new_employee.txt","w")
#employee_file.write("Ruby=Amazon engineer")

#employee_file=open("index.html","w")
#employee_file.write("<p> This is Html</p>")

#how to delete the file in python
import os
#os.remove("index.html")
'''
if os.path.exists("index.html"):
    os.remove("index.html")
else:
    print("file does not exist")

if os.path.exists("new_employee.txt"):
    os.remove("new_employee.txt")
else:
    print("file does not exist")
'''
employee_file=open("employee.txt","+r")
#print(employee_file.read())
print(employee_file.write("David=Microsoft Manager"))


#modules and pip
#module is a simple python file we can import into our current python
#file
#A module is a file containing Python definitions and statements.
# A module can define functions, classes, and variables.

#package is a collection of modules.

#2 types of modules
#1.builtin modules.e.g os,random,datetime,re,math
#2.external modules e.g.speech_recognition,speedtest,pandas,numpy etc

#pip = it is used to install external modules
#pip = it is referred as a package manager which is used to install,
#uninstall,update different python modules
#pip install module-name
#pip install pandas

#pypi=python package index where we can search different python modules

#how to check pip version
#pip --version
#how to update pip version
#python -m pip install --upgrade pip

#random module
#to select the random number(integer) from a range low to high
import random
import numpy
print(random.randint(50,100))
print(numpy.random.randint(50,100,5))


#Datetime
#it will show the current time and date
import datetime
x=datetime.datetime.today()
print(x)
y=datetime.date.today()
print(y)
z = datetime.time.min
print(z)
p = datetime.time.max
print(p)

#hour:min:sec
#year-month-date
x = datetime.time(5, 25, 1)
print(x)

d1 = datetime.date(2021, 2, 16)
print(d1)
d2=d1.replace(year=2022)
print(d2)
d3=d1.replace(month=6)
print(d3)
d4=d1.replace(day=15)
print(d4)

#to_datetime is pandas function which is used to convert string like dates
#into main format (year-month-date)
x="21 august 2021" #2021-08-21
import pandas as pd
y=pd.to_datetime(x)
print(y)

y="2022/01/26"
d=pd.to_datetime(y)
print(d)

f="26 feb 2022"
t=pd.to_datetime(f)
print(t)


#Converting Strings Using datetime
#%b = Month as locale’s abbreviated name. e.g Jan,Feb,Dec
#%d= Day of the month as a zero-padded decimal number.e.g.01, 02, …, 31
#%B =Month as locale’s full name. e.g=January, February, …, December
#%I =Hour (12-hour clock) as a zero-padded decimal number. e.g 01, 02, …, 12
#%M= Minute as a zero-padded decimal number.e,g 00, 01, …, 59
#%S= Second as a zero-padded decimal number. e,g 00, 01, …, 59
# %p = Locale’s equivalent of either AM or PM. e.g AM, PM (en_US);
#%f = Microsecond as a decimal number, zero-padded to 6 digits.e.g 000000, 000001, …, 999999
#%a = Weekday as locale’s abbreviated name.e.g Sun, Mon, …, Sat (en_US);
#%A Weekday as locale’s full name.e.g Sunday, Monday, …, Saturday
#%m = Month as a zero-padded decimal number.01, 02, …, 12
#%y = Year without century as a zero-padded decimal number. 00, 01, …, 99
import datetime

date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

'''
#percentage of letter in a given file
def count_char(text,char): #("aadesh",a)
    count=0
    for letter in text:
        if letter == char:
            count += 1
    return count
filename=input("Enter a filename: ")
with open(filename) as f:
    text=f.read()
for char in "abcdefghijklmnopqrstuvwxyz":
    perc=100 * count_char(text,char)/len(text)
    print("{} - {}% .".format(char,round(perc,2))) #a-0.2%


#voting application in python
import random
num=int(input("Enter number of candidates: ")) #3
cand=input(f'Enter {num} candidates now:\n').split() #[list of names]
print("Candidates are: ",cand)
print("Voting is live....please wait for the results...")
print("Voting has been finished.... and wait is over")
print("Here are the results")
votes=[]
for x in range(0,num): #(0,3)
    c=random.randint(1,100)
    votes.append(c)
for i in range(num): #(0,3)
    print(cand[i],':',votes[i]) #cand[0]:votes[0]
print("Hence the winner is...")
maximum=max(votes) #95
count=0
for r in range(num): #(0,3)
    if votes[r]==maximum:
        count=r #count =2
print(cand[count],':',maximum)
'''
#collections module
#counter=it is a dictionary sub class helps to count hashable objects.
#Inside of it elements are stored as keys and counts of objects
#stored as values.
from collections import Counter
l=[1,1,1,2,2,3,3,3,4,4,5,5,5] #{1:3,2:2,3:3,4:2,5:3}
x=Counter(l)
print(x)

s="assssvavasvsbsbsbba"
y=Counter(s)
print(y)

t=("x","y","x","y","z",(1,2))
m=Counter(t)
print(m)

text="how many times each word show up in this sentence word word show up up"
c=text.split()
print(c)
print(Counter(c))


#re=regular expression or regex
#re is only used for strings or text.
#it is a sequence of characters that forms a search pattern.they can be
#used to check if a string contains the specified search pattern.
#it is used to match the pattern
import re
#1.search
x="I am in pune"
v=re.search('pune',x)
print(v)

b=re.search("am",x)
print(b)

c=re.search("mumbai",x)
print(c)

#2.findall
#it returns a list containing all matches
y="pune is nice city,i live in pune."
n=re.search("pune",y)
print(n)
s=re.findall("pune",y)
print(s)

r="mumbai and pune are metro cities.pune is my choice out of that."
print(re.search("pune",r))
print(re.findall("pune",r))

#3.split()
# it returns a list where a string has been split at each match
text="what is your email,is it hello@gmail.com?"
k=re.split('@',text)
print(k)

d="my fav game is cricket! let me know yours! thanks."
print(re.split("!",d))

#4.sub()
#sub function replaces the matches with text of your choice
text="the rain in pune"
h=re.sub("\s","@",text)  #\s= whitespace,\S = non-whitespace
print(h)

# ^ starts with (^ is called circumflex)
# $ ends with
# \b checks specified character is at the beginning or at the end of word
# \A returns a match if specified character is at the beginning of string
# \Z returns a match if specified character is at the end of string
# \d returns a match if specified character is digit
# \D returns a match if specified character is non-digit
# \w returns a match if specified character is alphanumeric(a-z,A-Z,0-9,_)
# \W returns a match if specified character is non-alphanumeric
# \s= whitespace
# \S = non-whitespace
print(re.search("\Athe",text))
print(re.search("pune\Z",text))
print(re.search(r"\bain",text))
print(re.search(r"ain\b",text))
print(re.search("^the",text))
print(re.search("pune$",text))

# r indicates the raw string.this means that python interpreter should not
# try to interpret any special characters and instead should just pass the
# string to function as it is.

text="This is a string with some numbers 1233 and 89566 and symbol # hashtag."
print(re.findall(r"\d+",text))  #+ means one or more occurances
print(re.findall(r"\D+",text))
print(re.findall(r"\w+",text))
print(re.findall(r"\W+",text))
print(re.findall(r"\s+",text))
print(re.findall(r"\S+",text))

#. means any character letters space etc.
print(re.search(r"aza","plaza"))
print(re.search(r"P.ng","Penguin"))
print(re.search(r"p.ng","clapping"))
print(re.search(r"^x","xenon"))
print(re.search(r"p.ng","ponge"))
print(re.search(r"py.+n","python programming"))

#character set []
# it is used when you wish to match any one of group of characters at a point
# in input
#[abc] it searches for occurances of either a or b or c
test_phrase = "sdsd....sssddd...sdddsddd...dsds...dsssss..sdddd"
print(re.findall(r"sd+",test_phrase)) #s followed by one or more d
print(re.findall(r"sd*",test_phrase)) #s followed by zero or more d
print(re.findall(r"sd?",test_phrase)) # s followed by zero or one d
print(re.findall(r"sd{3}",test_phrase)) # s followed by 3 d's
print(re.findall(r"sd{2,3}",test_phrase)) # s followed by 2 or 3 d's
print(re.findall(r"s[sd]+",test_phrase)) #s followed by one or more s or d

#Exclusion
# we can use ^ to exclude terms by incorporating it into bracket
# [^...]
text="This is a string! But it has some punctuation.How can we remove it?"
#use [^!.?] will check for matches that are not !.? or space
print(re.findall(r"[^!.?]+",text))

# Character Range
text_new = "This is an example sentence.Lets see if we find some letters."
# [a-z]+  sequence of lowercase letters
# [A-Z]+  sequence of uppercase letters
# [a-zA-Z]+  sequence of lowercase or uppercase letters
# [A-Z][a-z]+  one uppercase letter followed by lowercase letters
print(re.findall(r"[a-z]+",text_new))
print(re.findall(r"[A-Z]+",text_new))
print(re.findall(r"[a-zA-Z]+",text_new))
print(re.findall(r"[A-Z][a-z]+",text_new))

#re.IGNORECASE
print(re.search(r"p.ng","Penguin",re.IGNORECASE))

# "|" any one of two (means or)
print(re.search(r"cat|dog",'I like cats'))
print(re.search(r"cat|dog",'I like cats and dogs'))
print(re.findall(r"cat|dog",'I like cats and dogs'))

print(re.search(r"Py.+n","Python Programming"))

print(re.search(r"o+l+","goldfish"))
print(re.search(r"o+l+","woolly"))

#match the countries that starts and ends with "a"
print(re.search(r"A.*a","Argentina"))
print(re.search(r"A.*a+","Azerbaijan"))
print(re.search(r"^A.*a$","Australia"))
print(re.search(r"^A.*a$","Azerbaijan")) #None

pattern =r"^[a-zA-Z_][a-zA-Z0-9_]*$"
text1="_this_is_a_valid_variable_name"
print(re.search(pattern,text1))
text2="this is not a valid variable'"
print(re.search(pattern,text2)) #None
# because whitespace are not included in possible characters
print(re.search(pattern,"my_variable1"))
print(re.search(pattern,"2my_variable1")) #None
#because in pattern it starts with letters or underscore only

#Write a function to check if the text passed looks like a standard sentence
# meaning that it starts with an uppercase letter,followed by atleast some
# lowercase letters and ends with a fullstop, question mark or exclamation
# mark.
import re
def check_sentence(text):
    result=re.search(r"^[A-Z][a-z]*[.?!]$",text)
    return result!=None
print(check_sentence("Is this is a sentence?"))
print(check_sentence("Hello!"))

# to match any string of exactly 5 letters
print(re.search(r"[a-zA-Z]{5}","a ghost is in Homme"))
print(re.findall(r"[a-zA-Z]{5}","a ghost is in Homme"))
print(re.findall(r"[a-zA-Z]{5}","a ghost is in Homme and it is appeared"))
# but we want exact 5 letters words. for this we use \b at the start and end
print(re.findall(r"\b[a-zA-Z]{5}\b","a ghost is in Homme and it is appeared"))
# if we want a match a range of 5 to 10 letters or numbers
# to match any string of exactly 5 letters
print(re.search(r"[a-zA-Z]{5}","a ghost is in Homme"))
print(re.findall(r"[a-zA-Z]{5}","a ghost is in Homme"))
print(re.findall(r"[a-zA-Z]{5}","a ghost is in Homme and it is appeared"))
# but we want exact 5 letters words. for this we use \b at the start and end
print(re.findall(r"\w{5,10}","a ghost is in Homme and it is appeared"))
print(re.findall(r"\w{5,10}","I really like Strawberries"))
# here min is 5 and max is 10
print(re.findall(r"\w{5,}","I really like Strawberries"))
#here max range is undefined

import re
def long_words(text):
    pattern=r"\w{7,}"
    result=re.findall(pattern,text)
    return result
print(long_words("I like to drink coffee in the morning"))
#write a python function that returns all the words that are atleast 7 characters

#Capturing groups ()
#last name,first name
#first name followed by last name
#first create a matching pattern that matches a grp of letters followed by a
#comma and then another grp of letters,To capture groups we put each grp of
#letters into ()
pattern=r"^(\w*),(\w*)$"
#print(re.search(pattern,"Joshi,Nikhil"))
result=re.search(pattern,"Joshi,Nikhil")
print(result.groups())
print(result[0])
#beacuse we have defined 2 separate grps ,the groups method returns a tuple
# of 2 elements.we can also use indexing to access groups.The first element
#contains the text matched by entire regular expression.i.e.at 0 index the
#entire text comes
#at index 1 =Joshi
#at index 2 =Nikhil
print(result[1])
print(result[2])
#"{} {}".format(result[2],result[1])
def rearrange_name(name):
    result=re.search(r"^(\w*),(\w*)$",name)
    if result is None:
        return name
    return "{} {}".format(result[2],result[1])

print(rearrange_name("Joshi,Sarthak"))
print(rearrange_name("Hopper,Grace M."))
# this will not work because \w will match only the letters so it didnt
# recognize the middle initial part of given name
def rearrange_name(name):
    result=re.search(r"^([\w\. ]*),([\w\. ]*)$",name)
    if result is None:
        return name
    return "{} {}".format(result[2],result[1])
print(rearrange_name("Hopper,Grace M."))




#Extracting PID using regex
import re
log="July 31 07:51:48 Mycomputer bad_process[12345]:ERROR Performing package upgrade"
regex=r"\[(\d+)\]"
print(re.search(regex,log))
print(re.search(regex,"A completely diffirent string that also has  numbers [34567]"))
result=re.search(regex,"A completely diffirent string that also has  numbers [34567]")
print(result[1])




#webbrowser
"""
import time
import webbrowser
set_alarm=input("Set the website alarm as H:M:S(all in 2 digits): ")
url=input("Enter the website you want to open: ")
Actual_Time=time.strftime("%I:%M:%S")
while Actual_Time != set_alarm:
    print("The time is: ",Actual_Time)
    Actual_Time = time.strftime("%I:%M:%S")
    time.sleep(1)
if Actual_Time == set_alarm:
    print("You should see your page now:-")
    webbrowser.open(url)


#phonenumbers
import phonenumbers
from phonenumbers import carrier,geocoder,timezone
mobileNo=input('Enter mobile Number with country code: ')
mobileNo=phonenumbers.parse(mobileNo)
#get timzone of phone number
print(timezone.time_zones_for_number(mobileNo))

#get the carrier of a phone number
print(carrier.name_for_number(mobileNo,'en'))

#getting region information
print(geocoder.description_for_number(mobileNo,'en'))

#validate the phone number
print("valid Mobile Number: ",phonenumbers.is_valid_number(mobileNo))

#checking possibility of a number
print('checking possibility of a number: ',phonenumbers.is_possible_number(mobileNo))
"""
import requests
response=requests.get("https://www.amazon.com")
print(response)

'''
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
'''

#Object Oriented Programming(OOPS)

#class
#object
#while defining a class first letter must be capital.
#class is a overall template,or it's a general template/description
#Class creates a user-defined data structure, which holds its own data
# members and member functions, which can be accessed and used by
# creating an instance(object) of that class.
#actual value should be the object
#object is the instance of the class
#class Employee(name,id,location)
#whenever we will declare the class name with parenthesis that will creat an object
#employee1=Employee()
#name,id,location=class attribute or variable
#employee1=Employee("sudhir",1234,"pune")
#employee2=Employee("yogesh",4567,"mumbai")
#class Student(name,clg,rank):
#s1=Student("nikhil","mit",3)
#s2=Student("prajakta","xyz",1)
#s3=Student("sudarshan","mit",2)


#The init method is similar to constructors in C++ and Java .
# Constructors are used to initialize the object's state.
# The task of constructors is to initialize(or assign) the values to the data
# members of the class when an object of class is created.
#__init__ =constructor or method that initialize the object
#and it allows the class to initialize the attributes of the class and
#this method is called when object is created
#self refers to newly created object
class Employee:
    def __init__(self,name,id,location):
        self.name=name
        self.id=id
        self.location=location
        #self.age=22
employee1=Employee("nikhil",1234,"Pune")
employee2=Employee("sagar",5678,"banglore")
print(employee1.name)
print(employee2.name)
print(employee2.location)


class Student():
    def __init__(self,name,college,gpa):
        self.name = name
        self.college = college
        self.gpa = gpa
student1=Student("Netra","MIT",7.2)
student2=Student("Sagar","VIT",3.3)
print(student1.college)
print(student2.gpa)

class Company():
    def __init__(self,name,location,CEO):
        self.name=name
        self.location = location
        self.CEO=CEO
infy=Company("INFOSYS","PUNE","NARAYAN MURTHY")
tcs=Company("TCS","BANGLORE","XYZ")
print(infy.CEO)

#class function or class method
#function which is defined inside of a class
class Student():
    def __init__(self,name,college,gpa):
        self.name=name
        self.college=college
        self.gpa=gpa

    def gpa_calculaton(self): #this is called as a method or class function
        if self.gpa>3.5:
            return True
        else:
            return False

student1=Student("Netra","MIT",7.2)
student2=Student("Sagar","VIT",3.3)
print(student1.gpa_calculaton()) #True
print(student2.gpa_calculaton()) #False

#Area of circle
class Circle():
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
        #self.pi=pi

    def area_circle(self):
        return self.pi*self.radius**2

    def circumference(self):
        return 2*self.pi*self.radius
c1=Circle(1)
print(c1.area_circle()) #3.14
print(c1.circumference()) #6.28
c2=Circle(2)
print(c2.area_circle()) #12.56
print(c2.circumference()) #12.56

#distance and slope of line
#slope=y2-y1/x2-x1
#distance=sqrt((x2-x1)**2+(y2-y1)**2)
class Line():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5

    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)
l1=Line(3,2,8,10)
print(l1.distance())
print(l1.slope())

#create a bank account class that has 2 attributes owner and balance.
#and 2 methods deposit and withdrawl.As an added requirement withdrawls
#may not exceed the available balance.
class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance


    def deposit(self,deposit_amt):
        self.balance=self.balance+deposit_amt

    def withdrawl(self,withdrawl_amt):
        if self.balance>withdrawl_amt:
            self.balance = self.balance - withdrawl_amt
        else:
            print("Insufficient funds!")

    def __str__(self):
        return f"owner:{self.owner}\nBalance:{self.balance}"
a=Account("sagar",500)
print(a)
a.deposit(1000)
print(a)
a.withdrawl(1000)
print(a)
a.withdrawl(10000)
print(a)


#mini project/Multiple choice quiz
question_prompts=["What colors are Apples?\n(a)Red\n(b)Purple\n(c)orange\n\n",
                  "what colors are Bananas?\n(a)Teal\n(b)Magenta\n(c)Yellow\n\n",
                  "what colors are strawberries?\n(a)Yellow\n(b)Red\n(c)Blue\n\n"
                  ]

class Question():
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer
#a=Question(question_prompts[0],"a") #object
#b=Question(question_prompts[1],"c")
#c=Question(question_prompts[2],"b")
questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")

]
def run_test(questions):
    score=0
    for object in questions:
        user_answer=input(object.prompt) #a
        if user_answer==object.answer:
            score=score+1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)

##Q3. How do you distinguish between a class object(variable) and an instance object(variable)?
class Test:
    x=10 #static variable (class object)
    def __init__(self,a,b):
        self.a=a
        self.b=b
print(Test.x)
#print(Test.a)

t1=Test(3,4) #t1 is the instance object that created manually
print(t1.a)
print(t1.x)

#when u write the class then class object is created automatically.
# class object holds static member variables i.e. x=10 in this case.
# so if we dont make the instance object then also we can access the
# the class object by name of class in this case Test such as by
# printing (Test.x)

#Inheritance
#It allows you to inherit functionalities from an existing class into
#new class
#Inheritance is basically where we can define a bunch of attributes,
#functions/methods inside of a class and we can create another class
#and we can inherit all those attributes and methods into new class.
class Chef():
    def make_chicken(self):
        print("the chef makes chicken")

    def make_salad(self):
        print("the chef makes salad")

    def make_special_dish(self):
        print("the chef makes BBQ ribs")

mychef=Chef()
print(mychef.make_chicken())
print(mychef.make_special_dish())
print(mychef.make_salad())


class Chinesechef(Chef):
    def make_fried_rice(self):
        print("the chef makes fried rice")
mychinesechef=Chinesechef()
print(mychinesechef.make_fried_rice())
print(mychinesechef.make_salad())

#with inheritance
# super class
class Shape:

    # constructor
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

        # public member function

    def displaySides(self):
        # accessing protected data members
        print("Length: ", self.length)
        print("Breadth: ", self.breadth)

    # derived class
o=Shape(8,10)
print(o.displaySides())

class Rectangle(Shape):

    # constructor
    def __init__(self, length, breadth):
        # Calling the constructor of
        # Super class
        Shape.__init__(self, length, breadth)

        # public member function

    def calculateArea(self):
        # accessing protected data members of super class
        print("Area: ", self.length * self.breadth)

# creating objects
obj = Rectangle(80, 50)
obj.displaySides()
obj.calculateArea()

# Multilevel Inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
#The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
#The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()


# Multiple Inheritance
class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))




# Composition in Python OOPS
'''
In composition one of the classes is composed of one or more instance of 
other classes. In other words one class is container and other class is
 content and if you delete the container object then all of its contents 
 objects are also deleted.
'''


class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return (self.pay * 12)


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)


obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())


class Salarynew:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus



class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salarynew(pay, bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()

emp = Employee('max', 25, 15000, 10000)
print(emp.total_salary())

# In our example Employee class acts like Container and Salary class
# inside the Employee class acts like content in it. Composition represents
# part-of relationship. In our eg. Salary is part of Employee.


#polymorphism in OOPS
#Polymorphism means multiple forms.
# In python we can find the same operator or function taking multiple forms.
# It also useful in creating different classes which will have class methods
# with same name
#Polymorphism in operators
print(4+5)
print("4"+"5")
print("ab"+"cd")
"""
In the first example, as the data sent are two integer values,the operator
did the addition operation of two numbers.And in the second example, as the
same values are sent as data in the form of string, and the same operator 
did the concatenation (concatenation is the process by which two strings 
are joined end-to-end) 
In the third example, the data sent are two strings but the operator 
is same as the above and it did the concatenation of the two strings.

Operator overloading is the type of overloading in which an operator can
be used in multiple ways beyond its predefined meaning.
print(2*7)
print("a"*3)
the multiplication operator did the multiplication of two numbers in the 
first one, but in the second one as the multiplication of a string and an 
integer is not possible so the character is printed repeatedly for 3 times. 
So it shows how we can use a single operator in different ways.
"""
##polymorphism in functions or classes
#1.In python polymorphism refers to the way in which different classes
#can share the same method name and then those methods can be called
#from the same place even though overrided different objects might be passed in.
#2.In python polymorphism let us define methods in child class that have the
#same method name in parent class
class Dog():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name+" says woof!"
d=Dog("niko")
print(d.speak())

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Meow!"

c=Cat("felix")
print(c.speak())

class India():
    def capital(self):
        print("Delhi is the capital of india")

    def language(self):
        print("Hindi is the language of india")

    def  type (self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Washington D.C is the capital of USA")

    def language(self):
        print("English is the language of USA")

    def type(self):
        print("USA is a developed country")

ind=India()
usa=USA()
for country in (ind,usa):
    country.capital()
    country.language()
    country.type()

#polymorphism with inheritance
class Bird():
    def intro(self):
        print("There are many types of birds")

    def flight(self):
        print("most of the birds can fly but some cannot")

class Sparrow(Bird):
    def flight(self):
        print("sparrow can fly")

class Ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly")

brd=Bird()
spw=Sparrow()
ost=Ostrich()
#print(spw.intro())
#print(ost.intro())
for x in (brd,spw,ost):
    x.intro()
    x.flight()

#method overidding(replace)
#the concept of method overriding allows us to change or override the Parent
#class function in the Child class
#to override the parent class method you have to create a method in the child
#with the same name and same number of parameters
#you cant override a method in the same calss.
class Employee():
    def message(self):
        print("This is a msg from employee class")


class Department(Employee):
    def message(self):
        print("This department class is inherited from employee class")

class Sales(Employee):
    def message(self):
        print("This Sales class is also inherited from employee class")
emp = Employee()
print(emp.message())
print("---------")
dept=Department()
print(dept.message())
print("---------")
sl=Sales()
print(sl.message())

# Another Example of Method Overriding
class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class ICICI(Bank):
    def getroi(self):
        return 8


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi())
print("SBI Rate of interest:", b2.getroi())
print("ICICI Rate of interest:", b3.getroi())

##Abstraction
#Abstraction is something when you are not able to cal my variable or data
#it is process of protecting your variables,methods from someone
#Public
#public (a) =Public attributes can be freely used inside or
#outside of a class definition.

class test:
    def __init__(self, a, b, c, d):
        self.a = a         #self.a = public ,self._a=protected,self.__a=private
        self.b = b
        self.c = c
        self.d = d

    def test_custom(self, v):
        return v - self.a

    def __str__(self):
        return "this is my test code for abstraction"

o = test(4,5,6,7)
print(o.test_custom(7)) #3
print(o)
print(o.a) #4

#protected (_)
#protected (_a)
#Protected members or variables of a class are accessible from within the
# class and are also available to its sub-classes. No other environment is
# permitted access to it. This enables specific resources of the parent
# class to be inherited in the child class
#it is callable on the object also.
class Test:
    def __init__(self, a, b, c, d):
        self._a = a         #self.a = public ,self._a=protected,self.__a=private
        self.b = b
        self.c = c
        self.d = d

    def test_custom(self, v):
        return v - self._a

    def __str__(self):
        return "this is my test code for abstraction"
o = Test(4,5,6,7)
print(o.test_custom(7))#3
print(o)
print(o._a)

class Test2(Test):
    def test_custom2(self,v1):
        return v1-self._a
o1=Test2(4,5,6,7)
print(o1.test_custom2(10)) #6

class Geek:
    # protected data members or variables
    _name = "Nikhil"
    _roll = 12345

    # public member function
    def displayNameAndRoll(self):
        # accessing protected data members
        print("Name: ", self._name)
        print("Roll: ", self._roll)
#creating objects of the class
obj = Geek()
# calling public member
# functions of the class
print(obj.displayNameAndRoll())

#with inheritance
# super class
class Shape:

    # constructor
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

        # public member function

    def displaySides(self):
        # accessing protected data members
        print("Length: ", self._length)
        print("Breadth: ", self._breadth)

#s=Shape(8,10)
#print(s._length)

class Rectangle(Shape):

    # constructor
    def __init__(self, length, breadth):
        # Calling the constructor of
        # Super class
        Shape.__init__(self, length, breadth)

        # public member function

    def calculateArea(self):
        # accessing protected data members of super class
        print("Area: ", self._length * self._breadth)
# creating objects
obj = Rectangle(80, 50)
obj.displaySides()
obj.calculateArea()
print(obj._length)


#Private variable
#These members are only accessible from within the class.
# No outside Access is allowed
#nobody should be able to access it from outside the class
class test:
    def __init__(self, a, b, c, d):
        self.__a = a         #self.a = public ,self._a=protected,self.__a=private
        self.b = b
        self.c = c
        self.d = d

    def test_custom(self, v):
        return v - self.__a

    def __str__(self):
        return "this is my test code for abstraction"
o = test(4,5,6,7)
print(o.test_custom(10)) #6
#print(o.__a)
print(o._test__a)

class employee:
    def __init__(self, name, sal):
        self.__name = name  # private attribute
        self.__salary = sal  # private attribute

    def displayNameSalary(self):
        print("Name: "+self.__name)
        print("Salary: "+str(self.__salary))

e1=employee("Bill",10000)
print(e1.displayNameSalary())
#print(e1.__name)

#encapsulation
#It is a method of packing data and functions operating on data into a single component
#and restricting the access to some of objects components.
# This puts restrictions on accessing variables and methods directly
# and can prevent the accidental modification of data. To prevent
# accidental change, an object’s variable can only be changed by
# an object’s method. Those types of variables are known as private
# variables.
# class is an example of encapsulation as it encapsulates all the
# data that is functions ,variables etc inside it.
#The aim is to hide the actual implementation of the class
#To avoid freezing internal representation,we expose "conceptual representation"



class test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "this is the return form of  test class "


class test1:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "this is the return form of  test1 class "

class test2:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "this is the return form of  test2 class "

class final:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.x) + "  " + str(self.y) + "  " + str(self.z)
t= test(4,5,6)
print(t)
t1 = test1(3,4,5)
t2 = test2(5,6,7)
f=final(t,t1,t2)
print(f)

##Using Getter and Setter methods to access private variables
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age #private variable is not accessible outside the class

    def display(self):
        print(self.name)
        print(self.__age)

    def setage(self,age):
        self.__age=age

    def getage(self):
        print(self.__age)
p=Person("NIKHIL",25)
print(p.display())
#print(p.__age)
print(p.name)
print(p.getage())
print(p.setage(27))
print(p.getage())

#Abstract classes
# In Python, an abstraction is used to hide the irrelevant data/class
# in order to reduce the complexity.
#A class which contains one or more abstract methods is called an abstract
# class
#An abstract method is a method that has a declaration but does not have
# an implementation.
#Abstract class can be inherited by the subclass and abstract method
# gets its definition in the subclass. Abstraction classes are meant to
# be the blueprint of the other class
#Python comes with a module that provides the base for defining Abstract
# Base classes(ABC) and that module name is ABC.
from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

from abc import ABC, abstractmethod
class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

#Generator (yield)
#generators are used to generate sequence of values overtime
#generators don't hold entire result in the memory it yields 1 result at a time
#with regular function
def create_cubes(n):
    result=[]
    for x in range(n): #(0,10)
        result.append(x**3)
    return result
print(create_cubes(10))

#with generator
def create_cubes_gen(n):
    for x in range(n):
        yield x**3
mynum=create_cubes_gen(10)
print(mynum)
print(next(mynum)) #0
print(next(mynum)) #1
print(next(mynum)) #8
for num in create_cubes_gen(10):
    print(num)

#sqaures of numbers
def sqaure_nums(nums):
    result=[]
    for i in nums:
        result.append(i*i)
    return result
my_nums=sqaure_nums([1,2,3,4,5])

#with generator
def sqaure_nums_new(nums):
    for i in nums:
        yield(i*i)
print(sqaure_nums_new([1,2,3,4,5]))
myresult=sqaure_nums_new([1,2,3,4,5])
print(next(myresult))
print(next(myresult))
for num in sqaure_nums_new([1,2,3,4,5]):
    print(num)

#create a generator that yields n random numbers btn low and high range
import random
def random_numbers(low,high,n):
    for i in range(n): #(0,12)
        yield random.randint(low,high)

rand_nums=random_numbers(1,10,12)
print(next(rand_nums))
print(next(rand_nums))
for result in rand_nums:
    print(result)


#fiboniccci series
#0,1,1,2,3,5,8,13,21
a=0
b=1
while b<100:
    print(b) #1,1,2
    a,b=b,a+b #a=1,b=0+1=1,a=1,b=a+b=1+1=2,a=2,b=2+1=3,a=3,b=3+2=5

#with generator
def generating_fibinacci(n):
    a=0
    b=1
    for i in range(n):
        yield b
        a,b=b,a+b
for num in generating_fibinacci(11):
    print(num)

#iterator
#iter function
s="hello"
'''for letter in s:
    print(letter)'''
s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
for result in s_iter:
    print(result)


'''
Create a list by picking an odd-index items from the first list and even index items from the second

Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]

l2 = [4, 8, 12, 16, 20, 24, 28]

Expected Output:

Element at odd-index positions from list one

[6, 12, 18]

Element at even-index positions from list two

[4, 12, 20, 28]

Printing Final third list

[6, 12, 18, 4, 12, 20, 28]
'''
l1 = [3, 6, 9, 12, 15, 18, 21]
odd=[]
for i in range(0,7):
    if i%2 !=0:
        odd.append(l1[i])
print(odd)

l2 = [4, 8, 12, 16, 20, 24, 28]
even=[]
for i in range(0,7):
    if i%2 ==0:
        even.append(l2[i])
print(even)

final=odd+even
print(final)

#method 2
l1=[l1[i] for i in range(0,7) if i%2 !=0]
print(l1)
l2=[l2[i] for i in range(0,7) if i%2 ==0]
print(l2)
print(l1+l2)

'''
Slice list into 3 equal chunks and reverse each chunk

Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

Expected Outcome:

Chunk 1 [11, 45, 8]

After reversing it [8, 45, 11]

Chunk 2 [23, 14, 12]

After reversing it [12, 14, 23]

Chunk 3 [78, 45, 89]

After reversing it [89, 45, 78]
'''
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
Chunk1=sample_list[0:3]
print(Chunk1)
reverse_chunk1=Chunk1[::-1]
print(reverse_chunk1)
Chunk2=sample_list[3:6]
print(Chunk2)
reverse_chunk2=Chunk2[::-1]
print(reverse_chunk2)
Chunk3=sample_list[6:]
print(Chunk3)
reverse_chunk3=Chunk3[::-1]
print(reverse_chunk3)

'''
Count the occurrence of each element from a list

Write a program to iterate a given list and count the occurrence of each 
element and create a dictionary to show the count of each element.

Given:

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

Expected Output:

Printing count of each item

{11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
'''
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d={}
for element in sample_list:
    if element not in d.keys():
        d[element]=1
    else:
        d[element] = d[element] +1
print(d)


first_list = [2, 3, 4, 5, 6, 7, 8]
'''
Create a Python set such that it shows the element from both lists in a pair

Given:

first_list = [2, 3, 4, 5, 6, 7, 8]

second_list = [4, 9, 16, 25, 36, 49, 64]

Expected Output:

Result is {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
'''
second_list = [4, 9, 16, 25, 36, 49, 64]
final_list=zip(first_list,second_list)
#for t in final_list:
    #print(t)
result_set=set(final_list)
print(result_set)

#Converting Strings to datetime object Using datetime module
#%b = Month as locale’s abbreviated name. e.g Jan,Feb,
#%d= Day of the month as a zero-padded decimal number.e.g.01, 02, …, 31
#%B =Month as locale’s full name. e.g=January, February, …, December
#%I =Hour (12-hour clock) as a zero-padded decimal number. e.g 01, 02, …, 12
#%M= Minute as a zero-padded decimal number.e,g 00, 01, …, 59
#%S= Second as a zero-padded decimal number. e,g 00, 01, …, 59
# %p = Locale’s equivalent of either AM or PM. e.g AM, PM (en_US);
#%f = Microsecond as a decimal number, zero-padded to 6 digits.e.g 000000, 000001, …, 999999
#%a = Weekday as locale’s abbreviated name.e.g Sun, Mon, …, Sat (en_US);
#%A Weekday as locale’s full name.e.g Sunday, Monday, …, Saturday
#%m = Month as a zero-padded decimal number.01, 02, …, 12
#%y = Year without century as a zero-padded decimal number. 00, 01, …, 99
import datetime

date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)


import datetime

date_time_str = 'Jun 28 2018 7:40AM'
date_time_obj = datetime.datetime.strptime(date_time_str, "%b %d %Y %I:%M%p")
print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

#commonly used time formats and the tokens used for parsing:
'''
"Jun 28 2018 at 7:40AM" -> "%b %d %Y at %I:%M%p"
"September 18, 2017, 22:19:55" -> "%B %d, %Y, %H:%M:%S"
"Sun,05/12/99,12:30PM" -> "%a,%d/%m/%y,%I:%M%p"
"Mon, 21 March, 2015" -> "%a, %d %B, %Y"
"2018-03-12T10:12:45Z" -> "%Y-%m-%dT%H:%M:%SZ"
'''
'''
Convert string into a datetime object

For example, You received the following date in string format. Please convert
it into Python’s DateTime object.

Given:

date_string = "Feb 25 2020 4:20PM"

Expected output:

2020-02-25 16:20:00
'''
date_string = "Feb 25 2020 4:20PM"
import datetime
date_time_obj = datetime.datetime.strptime(date_string,"%b %d %Y %I:%M%p")
print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

'''
Find the day of the week of a given date

Given:

given_date = datetime(2020, 7, 26)

Expected output:

Sunday
'''
import datetime
given_date = datetime.datetime(2020, 7, 26)
print(given_date.strftime("%A"))
#%A tells the day of week

'''
Subtract a week (7 days) from a given date in Python

Given:

given_date = datetime(2020, 2, 25)

Expected output:

2020-02-18
'''
from datetime import timedelta
given_date = datetime.datetime(2020, 2, 25)
print(given_date)
a= given_date-timedelta(7)
print('Given Date :',given_date)
print('7 days before Given Date :',a)

#decorators in python
'''
Functions are first-class objects in the Python because they can reference
to, passed to a variable,you can pass the function as a parameter to another
function and returned from other functions as well.
The decorator in Python is a particular form of a function that takes 
functions as input or arguments and returns a new function as output. 
In Decorators, functions are taken as the argument into another function 
and then called inside the wrapper function.
'''
def func1(msg):
    print(msg)
func1("Hi") #Hi
x=func1
x("Hello") #Hello

# The x referred to function func1 and act as function.
# Python provides the facility to define the function inside another
# function. These types of functions are called inner functions.
# Consider the following example:
def func():
    print("We are in first function")

    def func1():
        print("This is first child function")

    def func2():
        print("This is second child function")

    func1()
    func2()
func()

#A function that accepts other function as an argument is also called
# higher order function.
def add(x):
    return x+1 #10+1=11
def sub(x):
    return x-1 #10-1=9

def multiply(x):
    return x*2
def operator(func, x):
    temp = func(x)
    return temp
print(operator(add,10)) #11
print(operator(sub,10)) #9
print(operator(multiply,10)) #10*2=20
#output 9,21
#In the above program, we have passed the sub() function and add() function
# as argument in operator() function.

#Decorating functions with parameters
def divide(x,y):
    print(x/y)
def outer_div(func):
    def inner(x,y):
        if (x < y):
            x, y = y, x #x=4,y=2
        return func(x, y) #divide(4/2)=2
    return inner #2
divide1=outer_div(divide)
divide1(2,4) #2

#with @ symbol
def outer_div(func):
    def inner(x,y):
        if(x<y):
           x,y = y,x #x=20,y=5
        return func(x,y) #divide(20,5)=(20/5)=4
    return inner #4
# syntax of generator
@outer_div
def divide(x,y):
    print(x/y)
divide(5,20) #4

# simple decorator that will convert a sentence to uppercase. We do this
# by defining a wrapper inside an enclosed function.
def uppercase_decorator(function):
    def wrapper():
        func=function() #"hello there"
        make_uppercase = func.upper() #"HELLO THERE"
        return make_uppercase #"HELLO THERE"
    return wrapper #"HELLO THERE"

#Our decorator function takes a function as an argument, and we shall,
# therefore, define a function and pass it to our decorator.
# We learned earlier that we could assign a function to a variable.
# We'll use that trick to call our decorator function.
def say_hi():
    return 'hello there'
decorate=uppercase_decorator(say_hi)
print(decorate())

#Python provides a much easier way for us to apply decorators.
# We simply use the @ symbol before the function we'd like to decorate
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())

##Applying Multiple Decorators to a Single Function
def split_string(function):
    def wrapper():
        func = function() #hello there
        splitted_string = func.split() #["hello","there"]
        return splitted_string #["hello","there"]

    return wrapper #["hello","there"]
@split_string
def say_hi():
    return 'hello there'
print(say_hi())


@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())

##Accepting Arguments in Decorator Functions
'''
Sometimes we might need to define a decorator that accepts arguments. 
We achieve this by passing the arguments to the wrapper function
'''
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments
@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {} and {}".format(city_one, city_two))

cities("Pune", "New Jersey")


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs): #*args=tuple,**kwargs=dictionary
        print('The positional arguments are', args) #()
        print('The keyword arguments are', kwargs) #{}
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

#decorator using positional arguments.
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)
function_with_arguments(1,2,3)

#Keyword arguments are passed using keywords.
@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="John", last_name="Smith")


# importing libraries
import time
import math
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs) #factorial of 10

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ",  end - begin)

    return inner1
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))
# calling the function.
factorial(10)

d1 = {'a': 10, 'b': (20,30,40), 'c': [ {'d': [1,2,3,4,5]} ]}
#print 3 from this dictionary
print(d1['c'][0]['d'][2])

class A :
    def func1(self):
        print('A')
class B(A) :
    def func1(self):
        print('B')
class C(B,A) :
    def func1(self):
        print('C')
class D(C,B,A) :
    def func1(self):
        print('D')
c=C()
print(c.func1())


t1 = (1,2,3, [4,5,6])
#output (1,2,3,4,5,6)



#DATABASE CONNECTIVITY WITH PYTHON
import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password="Kantnishu@19",
                             database='sar_sud_nish'
                        )
print(mydb)

mycursor=mydb.cursor()       #cursor is method to connect python and sql.
#1.CREATE DATABASE
#mycursor.execute("CREATE DATABASE sar_sud_nish")
#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
   #print(db)
#mycursor.execute("CREATE TABLE company(name VARCHAR(255),location VARCHAR(255),CEO VARCHAR(255))")
#mycursor.execute('CREATE TABLE students(name VARCHAR(255),college VARCHAR(255))')
#mycursor.execute("SHOW TABLES")
#for db in mycursor:
   #print(db)

#3.INSERT INTO
#mycursor.execute("INSERT INTO company(name,location,CEO) VALUES('WIPRO','PUNE','AZIZ PREMJI')")
#mydb.commit()
#print(mycursor.rowcount,"record inserted")

#4.INSERT MANY VALUES
'''
sql="INSERT INTO students(name,college) VALUES(%s,%s)" #%s means string
val=[
    ('peter','V.I.T'),
    ('Amy','COEP'),
    ('Hanna','PCCOE'),
    ('Micheal','PVG'),
    ('Sandy','MMCOE'),
    ('amruta','FERGUSSION')]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"records inserted")

sql="INSERT INTO company(name,location,CEO) VALUES(%s,%s,%s)" #%s means string
val=[
    ('TCS','PUNE',"TATA"),
    ('INFY','HYDERABAD',"NARAYAN MURTHY"),
    ('PERSISTENT','PUNE','ANAND DESHPANDE'),
    ('WIPRO','NOIDA','AZIZ PREMJI'),
    ('IBM','BANGLORE','KRISHNA'),
    ('HCL','MUMBAI','XYZ')]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"records inserted")

#5.SELECT FROM
mycursor.execute("SELECT * FROM company")
result=mycursor.fetchall()
for x in result:
    print(x)

mycursor.execute("SELECT name,CEO FROM company")
result=mycursor.fetchall()
for x in result:
    print(x)
  
#6.WHERE
mycursor.execute("SELECT * FROM company WHERE name='WIPRO'")
result=mycursor.fetchall()
for x in result:
    print(x)

mycursor.execute("SELECT * FROM company WHERE name='WIPRO' and location='PUNE'")
result=mycursor.fetchall()
for x in result:
    print(x)


#7 ORDERBY (ASC,DESC)
mycursor.execute("SELECT * FROM company ORDER BY name")
result=mycursor.fetchall()
for x in result:
    print(x)

#8 ORDERBY (ASC,DESC)
mycursor.execute("SELECT * FROM company ORDER BY location DESC ")
result=mycursor.fetchall()
for x in result:
    print(x)

#9.update
mycursor.execute("UPDATE company SET location='PUNE' WHERE name='INFY'")
mydb.commit()
print(mycursor.rowcount,"records updated")


mycursor.execute("UPDATE company SET CEO='RATAN TATA' WHERE location='PUNE' and name='TCS'")
mydb.commit()
print(mycursor.rowcount,"records updated")


#10.Alter the table or add new column
mycursor.execute("ALTER TABLE students ADD COLUMN Rating int(3) NOT NULL")
mycursor.execute("DESCRIBE students")
for i in mycursor:
    print(i)
'''
#mycursor.execute("ALTER TABLE students CHANGE name first_name VARCHAR(255)")
#mycursor.execute("ALTER TABLE students CHANGE rating college_rating int(3)")
#mycursor.execute("ALTER TABLE students DROP college_rating")


#11.PRIMARY KEY
#Its a unique value associated with each row in the table
#mycursor.execute("CREATE TABLE Person(name VARCHAR(50) NOT NULL,age int NOT NULL ,personID int NOT NULL PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Person(name,age) VALUES('nikhil',22)")
#mydb.commit()
#print(mycursor.rowcount,"record inserted")
'''
mycursor.execute("INSERT INTO Person(name,age) VALUES('John',30)")
mydb.commit()
print(mycursor.rowcount,"record inserted")

sql="INSERT INTO Person(name,age) VALUES(%s,%s)"
val=[
    ('peter',23),
    ('Amy',25),
    ('Hanna',27),
    ('Micheal',32),
    ('Sandy',29),
    ('amruta',21)
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"records inserted")
'''
#A FOREIGN KEY is a field (or collection of fields) in one table, that
# refers to the PRIMARY KEY in another table.

#The table with the foreign key is called the child table, and the table
# with the primary key is called the referenced or parent table.

#The FOREIGN KEY constraint prevents invalid data from being inserted
#into the foreign key column, because it has to be one of the values
# contained in the parent table.

#parent table in which PersonID is the primary key
#Person Table
'''
PersonID	LastName	FirstName	Age
1	        Hansen	        Ola	     30
2	        Svendson	    Tove	 23
3	        Pettersen	    Kari	 20
'''
#Orders Table (Child table because it contains foreign key)
#PersonID here is the foreign key
'''
OrderID	OrderNumber	PersonID
1	    77895	    3
2	    44678	    3
3	    22456	    2
4	    24562	    1
'''
#create a person table
#sql="CREATE TABLE Persons (PersonID int NOT NULL,LastName VARCHAR(50), FirstName VARCHAR(50), age int NOT NULL,PRIMARY KEY (PersonID))"
#mycursor.execute(sql)
'''
sql="INSERT INTO Persons (PersonID,LastName,FirstName,age ) VALUES(%s,%s,%s,%s)"
val=[
    (1,"Hansen","Ola",30),
    (2, "Hansen", "Ola", 30),
    (3, "Svendson", "Tove", 23),
    (4, "Pettersen", "Kari", 20),
    (5, "sagar", "Joshi", 28),

]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"records inserted")
'''

#The following SQL creates a FOREIGN KEY on the "PersonID" column when
# the "Orders" table is created:
#sql="CREATE TABLE Orders (OrderID int NOT NULL,OrderNumber int NOT NULL, PersonID int, PRIMARY KEY (OrderID),FOREIGN KEY (PersonID) REFERENCES Persons(PersonID))"
#mycursor.execute(sql)
#To allow naming of a FOREIGN KEY constraint, and for defining a
# FOREIGN KEY constraint on multiple columns, use the following SQL syntax:
#sql="CREATE TABLE Orders_new (OrderID int NOT NULL,OrderNumber int NOT NULL,PersonID int,PRIMARY KEY (OrderID), CONSTRAINT FK_PersonOrder FOREIGN KEY (PersonID)REFERENCES Persons(PersonID))"
#mycursor.execute(sql)
'''
from datetime import datetime
#mycursor.execute("CREATE TABLE Test(name VARCHAR(50) NOT NULL, created datetime NOT NULL , gender ENUM('M','F','O'),personID int NOT NULL PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("INSERT INTO Test(name,created,gender) VALUES(%s,%s,%s)",("nikhil",datetime.now(),"M"))
mydb.commit()
print(mycursor.rowcount,"record inserted")
'''
#mycursor.execute("INSERT INTO Test(name,created,gender) VALUES(%s,%s,%s)",("sagar",datetime.now(),"M"))
#mydb.commit()
#print(mycursor.rowcount,"record inserted")

#11.wildcard character (%)
#with this you can select records that starts,includes or ends with a given
#letter or phrase
#mycursor.execute("CREATE TABLE customers(name VARCHAR(50) NOT NULL,address VARCHAR(255) NOT NULL,customerID int NOT NULL PRIMARY KEY AUTO_INCREMENT)")
'''
sql="INSERT INTO customers(name,address) VALUES(%s,%s)" #%s means string
val=[
    ('peter','Lowstreet4'),
    ('Amy','Applest652'),
    ('Hanna','Mountain21'),
    ('Micheal','Valley345'),
    ('Sandy','highstreetway78'),
    ('amruta','oneway98'),
    ('John','Highway21')]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"records inserted")


mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")
result=mycursor.fetchall()
for x in result:
    print(x)


mycursor.execute("SELECT * FROM customers WHERE name LIKE '%a'")
#%a means at the end
#a% means at the start
result=mycursor.fetchall()
for x in result:
    print(x)

mycursor.execute("SELECT * FROM customers WHERE name LIKE 'p%'")
result=mycursor.fetchall()
for x in result:
    print(x)

#14.LIMIT
#you can limit the number of records returned from a query
#select first 5 records from the customers table
mycursor.execute("SELECT * FROM Person LIMIT 5")
result=mycursor.fetchall()
for x in result:
    print(x)


#15.OFFSET
#if you want to select 5 records starting from 3 we can use OFFSET keyword
mycursor.execute("SELECT * FROM Person LIMIT 5 OFFSET 2")
result=mycursor.fetchall()
for x in result:
    print(x)

mycursor.execute("SELECT * FROM company LIMIT 1 OFFSET 2")
result=mycursor.fetchall()
for x in result:
    print(x)

#12 DELETE FROM
#whenever you want to delete record from table
mycursor.execute("DELETE FROM customers WHERE address='Mountain21'")
mydb.commit()
print(mycursor.rowcount,"record deleted")


mycursor.execute("DELETE FROM customers WHERE address LIKE '%way%'")
mydb.commit()
print(mycursor.rowcount,"records deleted")


mycursor.execute("DELETE FROM Person WHERE name='nikhil' and age=22")
mydb.commit()
print(mycursor.rowcount,"record deleted")
'''

#13. DROP TABLE
mycursor.execute("DROP TABLE IF EXISTS students")



import pandas as pd
import numpy as np
df=pd.read_csv('Brokerlink_Report_CCJS 311 ORT Model Intelligence-Led Policing (2225).csv')
df.head()





