
# tuples
# **********************************
# tup1=(1,'khan',5.0)
# print(tup1)
# print(type(tup1))
# tup2=(4,5,'jan')
# print(tup2+tup1)
# # print(tup1*5)


# dictionary data structure
# *****************************************************************************
# diction={'ali':'sinwari','age':40,'salay':5000,'married':'N'}
# print(diction.values())
# print(diction.pop('married'))
# print(diction.items())
# diction['married']='Y'
# print(diction)
# diction['Student']='No'
# print(diction)
# print(diction.clear())

# ********************************************************
# List data structure


# list1=[1,'khan', True,5.5]
# print(list1)
# # list1.sort()
# list2=[4,5,55,0,33,2,666,1]
# #  used to sort
# list2.sort()
# print(list2)
#
# #  used to remove item at given index
# list2.pop(2)
# print(list2)
# # used to add item to list
# list2.append(100)
# print(list2)
# # used to insert a value at specific index
# list2.insert(0,'khan')
# print(list2)
# *************************************************
# function in python
# function defination without argument
def add():
    print(2+3)
#function calling
add()

# function with two argument
def add( x, y):
    print(x+y)
add(2,6)

# function with return type

def add(x,y):
    z=x+y
    return z
sum=add(8,9)
print(sum)
