#syntax, variable, data types
# chatgpt ex 1
print("BONJOUR!!")
print("He gives his harness bells a shake \nTo ask if there is some mistake.")
print("The only other sound’s the sweep\nOf easy wind and downy flake.\nThe woods are lovely, dark and deep.")
print("But I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep.")

# chatgpt ex 2

city = "Paris"
population = 2140526
temperature = 18.5
is_capital = True
print(city,population,temperature,is_capital)#or
print(city, "\n", population, "\n", temperature, "\n", is_capital)#or
print(f"City: {city}\nPopulation: {population}\nTemperature: {temperature}\nCapital: {is_capital}")
# 3rd is best 

a = 5
b = 10
a,b=b,a
print("a=",a,"b=",b)

#chatgpt ex 3

name = "Andri"         
age = 18       
height = 50.2 
likes_python = True  
print(f"name:{name}\nage:{age}\nheight:{height}\nlikes_python:{likes_python}")

age = float(18)
print(type(age)) #or
print(isinstance(age, float))   # checks if age is float

s = "Python"
print(len(s))        
print(s.upper())     
print(s.lower())     
print(s[0])          
print(s[-1])        

#game

import random

secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

print(f"You guessed: {guess}")
print(f"Secret number was: {secret}")
if guess == secret:
    print("Correct!!🥳")
else:
    print("Wrong 😔")

