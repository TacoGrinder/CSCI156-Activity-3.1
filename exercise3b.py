__author__ = 'Sean'

def knockintro():
    print ("Knock, Knock")
    print ("Who's there?")

def setup(n):
    print (n)
    print (n + " " + "Who?")

def knockknock(n, b):
    knockintro()
    setup(n)
    print(n + " " + b)

knockintro()
setup("Sean")
print("\n")

knockknock("whale", "don't just stand there!")
print("\n")
knockknock("orange", "you glad I didn't say banana")