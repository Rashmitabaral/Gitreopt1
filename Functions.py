###Functions:

##What is the purpose of the function is---
##A name for the function
# Aset of inputs to the function
##A return type
###An expression that computes the return value given the set of inputs
###Add new branch to git hub
###this updated file

a = [1,2,3,4]
def square(x):
    return x*x
print(square)


a = [1,2,3,4]
def square(x):
    return x*x
#map(square,a)
list(map(square,a))
print (map(square,a))


a = [4,3,2,1]
print(list(map(lambda x:x*x,a)))



n = [4,3,2,1]
print(list(map(lambda x:x**2,n)))

def square (lst1):
    lst2 = []
    for num in lst1:
        lst2.append(num**2)
        return lst2
    print (square([4,3,2,1]))

print (dir(n))


print({x:x**2 for x in n})

{4: 16, 3: 9, 2: 4, 1: 1}

## Compare def and Lambda

##double x
def double (x):
    return x*2
print(double(4))

## same thing in lambda

lambda x:2*x

#add x and Y

def add(x,y):
    return x + y
print(add(3,4))

n=lambda x,y: x+y
print(n(6,7))

#max of x,y

def mx(x,y):
    if x>y:
        return x
    else:
        return y
    print(mx(16,15))


    mx = lambda x,y:x if x>y else y
    print(mx(8,5))

##Map

##Prints square

def square(lst1):
    lst2 = []
    for num in lst1:
        lst2.append(num**2)
    return lst2
print (square([4,3,2,1]))

##use lambda

n= [5,4,3,2]
print(list(map(lambda x:x**2,n)))

## you can use simple square function

##n= [6,7,8,2]
###print(list(map(square,n)))

n= [6,7,8,2]
print([x**2 for x in n])


n= [6,7,8,2]
print({x:x**2 for x in n})


#print which value is higher

def over_two(lst1):
    lst2 = [x for x in lst1 if x > 4]
    return lst2
print (over_two([6,5,4,3]))

n= [7,6,4,3]
print(list(filter(lambda x:x>4,n)))

##list comprehension

n= [4,5,3,1]
print([x for x in n if x>2])

### Reduce function
###List,[m,n,p]-Function+++> f(f(m,n),p)
#prints 24 using def,lambda and print comprehension

def mult(lst1):
    prod = lst1[0]
    for i in range(1,len(lst1)):
        prod*=lst1[i]
        return prod
    print (mult([4,3,2,1]))

    #Lambda

    n=[4,3,2,1]
    print(reduce(lambda x,y:x*y,n))



print (dir(n))


###Input statement using def function


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def main():
    num1 = int(input("What is number 1?"))
    num2 = int(input("What is number 2?"))
    print(add(num1, num2))
    print(sub(num1, num2))
    print(mul(num1, num2))
    print(div(num1, num2))
main()

####Input statement
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
randomfloat = float(input("Enter a random float: "))
print()
print("Hello " + ) name + " you are " + str(age)
                  + "years old, and your fav float is" + str(randomfloat))


######Functionaction():


def my_function():
    print("Hello From my Function")

def sum_two_numbers(a, b):
    return a + b
