__author__ = 'Sean'

def dot(n):
    x = int((n-3)/2)
    a = ("+" + "-"*(x) + "+" + "-"*(x) + "+")
    print(a)

def dit(n):
    x = int((n-3)/2)
    a = ("|" + " "*x + "|" + " "*x + "|")
    print(a)


def box(n):
    dot(n)
    dit(n)
    dit(n)
    dit(n)
    dit(n)
    dot(n)
    dit(n)
    dit(n)
    dit(n)
    dit(n)
    dot(n)

dit(10)
print("\n")
dot(10)
print("\n")

box(30)
