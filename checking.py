# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print(x)


# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


line = "hello how are you\nI am testing the new line escape sequence\nthis seems to work"

print(line)


###
##We have a class defined for vehicles.
#Create two new vehicles called car1 and car2.
#Set car1 to be a red convertible worth $60,000.00 with a name of Fer,
#and car2 to be a blue van named Jump worth $10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name,
                                                   self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())


def fibonacci1(n):
    if n==1 or n==2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)

for i in range(1,10):
    print (fibonacci1(i))

    def fibonacci2(n):
        a,b = 1,1
        for i in range(n-1):
            a, b = b, a+b
            return a

    for i in range(1,10):
        print(fibonacci2(i))
