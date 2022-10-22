"""car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car2 = car["model"]
print(car2)

"""


"""def moible_price_bdt(price_usd,exchange_rate):
    bdt_price = price_usd * exchange_rate
    return bdt_price

xaomi_price = moible_price_bdt(130,121.89)
print(round(xaomi_price))"""


"""def hello(name):
    print("Hi There",name)

hello("Abrar Fahad")
"""

def add(x,y):
    sum = x + y
    print(sum)
add(10,20)

def sub(x,y):
    sub = x - y
    print(sub)
sub(30,20)

def mod(x,y):
    z = x % y
    print(z)
mod(58,10)

def floor(x,y):
    z = x // y
    print(z)
floor(58,10)


# function with return
"""
def larger(a,b):
    if a > b:
        return a
    else:
        return b

result = larger(23,34)
print(larger(23,34))
"""

"""
def voter(age):
    if age >18:
        return "You are Voter"
    else:
        return "Your are Not voter"
result = voter(10)
print(result)

"""

"""
def sum(a,b):
    c=a + b
    return c

print(sum(2.3,3))
"""
"""
def f(name):
    print("Your name IS :"+name)
name_input = input("Enter Your Name :")
f(name_input)

"""

"""
def add(a,b):
  
    c = a + b
    return c
x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
add(x,y)
print(add(x,y))
"""
def add_or_sub(a,b):
    add = a + b
    sub = a - b
    return f'The add is {add}\nAnd The sub is {sub}'
x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
result = add_or_sub(x,y)
print(result)


