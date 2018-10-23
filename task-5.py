import sys

#Task 1 in a class as requested.
class Task1:
    def __init__(self):
        self.str = "Hello, My name is Jonas"

    def reverseString(self):
        #Lets try this without using the easy methods like
        #word[::-1]
        #"".join(reversed(word))

        reversed = []
        i = len(self.str)
        while i:
            i -= 1
            reversed.append(self.str[i])
        print "".join(reversed)

#Task 2 in a class as requested.
class Task2:
    def __init__(self):
        self.numbers = [456,456345,6456346,1356,1546,1457,145,7246724671,61,345,13451345,3456,4545134,5134,545,145]

    #This returns the first duplicate found and asumes that there are no further duplicates
    def findDuplicateNumber(self):
        seen = []
        for n in self.numbers:
            if n not in seen:
                seen.append(n)
            else:
                print n

#Simple menu with a loop that starts up each Task
def print_menu():
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Start Task 1"
    print "2. Start Task 2"
    print "3. Exit"
    print 67 * "-"

loop=True

while loop:
    print_menu()
    choice = input("Enter your choice [1-3]: ")

    if choice==1:
        t1 = Task1()
        t1.reverseString()
    elif choice==2:
        t2 = Task2()
        t2.findDuplicateNumber()
    elif choice==3:
        loop=False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")
