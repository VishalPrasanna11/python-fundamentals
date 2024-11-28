def great():
    print("Hello, World!")
    
great()

def sum(a,b):
    return a+b

print(sum(1,2))

def square(x):
    return x**x

print(square(2))


def welcome(name="Revanth"):
    print("Hello, " + name)

welcome()
welcome("John")

def arg(*args):
    for i in args:
        print(i)
        
arg(1,2,3,4,5)
arg("apple", "banana", "cherry")


def keypair(**k):
    for i in k:
        print("key: ", i, "value: ", k[i])
        
keypair(name="John", age=30, color="blue")


