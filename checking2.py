from functools import reduce
##import operator

#print(reduce(operator.mul,(3,4,5),1))
n = [4, 3, 2, 1]
print(reduce(lambda x,y:x*y,n))

list =['abcd',786,2.23,'john',70.2]
print(list)


lst1 = ['abcd', 786 , 2.23, 'john', 70.2 ]
lst2 = [123, 'john']
print (lst1 + lst2)


What is the output of print list[1:3]
if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?


What is the output of print str[2:5] if str = 'Hello World!'?


How will you get all the keys from the dictionary?

How will you get all the values from the diction

How will you convert a string to an int in python?

What is the output of len([1, 2, 3])?

def f(x = 100, y = 100):
   return(x+y, x-y)
x, y = f(y = 200, x = 100)
print(x, y)

A - 300 -100
B - 200 0
C - 200 100
D - 0 300

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3


def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list

