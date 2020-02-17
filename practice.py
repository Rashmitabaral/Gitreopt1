n1 = []
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    ##print(arr[i].pop())
    n1.append(arr[i].pop())
print(n1)

# how to use append--add value to ist

courses = ['History','Math','Physics','CompSc1']
courses.append('Art')
print(courses)

###Output---['History', 'Math', 'Physics', 'CompSc1', 'Art']

### Insert-- we can add value in the list

courses = ['History','Math','Physics','CompSc1']
courses.insert(0,'Art')
print(courses)

###output---['Art', 'History', 'Math', 'Physics', 'CompSc1']

###we can insert another list also

courses = ['History','Math','Physics','CompSc1']
courses_2 =['Art','Education']
courses.insert(0,courses_2)
print(courses)

##3output----[['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSc1']

##But we want to add new list value to 1st list--- we can use
##extend method
### We can use 'append' but append will display another []
# under the same list  '
## that way we use extend method



courses = ['History','Math','Physics','CompSc1']
courses_2 =['Art','Education','chemistry']
courses.extend(courses_2)
print(courses)

###output:['History', 'Math', 'Physics',
# 'CompSc1', 'Art', 'Education', 'chemistry']

#Remove from list--- we can use 'remove' or 'pop'

courses = ['History','Math','Physics','CompSc1']
courses.remove('Math')
print(courses)

## Math remove from list--['History', 'Physics', 'CompSc1']

##but 'pop' will remove last value from  queue
##This is very good for stack and Queue

courses = ['History','Math','Physics','CompSc1']
courses.pop()
print(courses)

##Output---['History', 'Math', 'Physics']

## Very useful Pop method--if we r doing Stack or Queue
# and we want to see which value is removing then we can use like--

courses = ['History','Math','Physics','CompSc1']
popped = courses.pop()
print(popped)
print(courses)

##Output--CompSc1
##['History', 'Math', 'Physics']

##How to sort list
##We can do reverse method

courses = ['History','Math','Physics','CompSc1']
courses.reverse()
print(courses)

##OUTput--['CompSc1', 'Physics', 'Math', 'History']

###If we want to do sorting by alphabetical order then---

courses = ['History','Math','Physics','CompSc1']
courses.sort()
print(courses)

##Output--['CompSc1', 'History', 'Math', 'Physics']

###List and tuple

a = [1,2,3,4]
b = [1,1,1,1]
##print(tuple(map(lambda x,y:x+y,a,b)))
print(list(map(lambda x,y:x+y,a,b)))

a = [2,3,4]
map(lambda x:x*x,a)




