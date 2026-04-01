def greet():
    print("Hello World")


greet()

def greet_person(name):
    print("Hello", name)

greet_person("Orges")

def shuma(x,y):
    return x+y

result = shuma(10,5)
print(result)

def numrat_cift():
    shuma = 0
    for i in range(1, 10):
        if i % 2 == 0:
            print(i)
            shuma += i
    return shuma

rezultati = numrat_cift()
print("Shuma:", rezultati)
