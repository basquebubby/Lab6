print "Do you want to add for find the factorial?"
answer = raw_input("Add or Fact: ")
def add():
    print "How many numbers do you want to add together?"
    userlistone = []
    x = raw_input("How many times: ")
    for number in range(int(x)):
        userinput = int(raw_input("Enter a number: ")) #Remeber the int()
        userlistone.append(userinput) #Inputs the user input into the list
    print "The answer is " + str(sum(userlistone))

def fact(): #Finds the factorials and the whole factors of a number
    print "What factorial of a number do you want to find?"
    userinput = raw_input("Number: ")
    import math
    total = str(math.factorial(int(userinput)))
    print total
    print "Finding factors of your number too"
    import time
    time.sleep(1)
    print "..."
    time.sleep(1)
    def print_factors(x):
        print "The factors of " + userinput + " are: "
        for i in range(1, x + 1):
            if x % i == 0:
                print(i)
    print_factors(int(userinput))
if answer == str("Add"):
    add()
if answer == str("Fact"):
    fact()