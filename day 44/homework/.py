# #For loop

#1)Print all integers from 0 to 20 

for i in range(21):
   print(i) 

# #2) Print the first 10 natural numbers. for loop ის გამოყენებით

for i in range(1,11):
   print(i)

#3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive for loop ის გამოყენებით

even_numbers = ""
odd_numbers = ""

for i in range(0,  101,2):
   print(i)
for i in range(1,101,2):
   print(i)

# #4) enter even number to the user and then using a for output the sum of all the numbers up to this numbers (for exemple,if he enter 10,output the sum of all the numbers up to 10, for exemple).

num = int(input("enter number: "))
sum = 0
for i in range(num):
    sum += i
print(sum)

#5)write an algorithm thაt multiples of 5(numbers divisible by 5)from 1 to 50
multiples_of_5 = []

for number in range(1, 51):
    if number % 5 == 0:
        multiples_of_5.append(number)

print("Multiples of 5 from 1 to 50:",multiples_of_5)


#while loop

#1)print even numbers up to 20 while loop-ის გამოყენებით
num = 2  

while num <= 20:
    print(num)
    num += 2

#2)print the firs 10 natural numbers
number = 1

while number <= 9:
    print(number)
    number += 1 

#3) write a while loop that ascks the user to guess a number between 1 and 10 until they get it right. the correct number is 7

correct_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == correct_number:
       print("Congratulations! You guessed the correct number.")
       break  
    else:
        print("Wrong guess. Try again.")

#4) write a while loop that processes a list of a numbers,doudling each number,and prints the new list.

numbers=[1,2,3,4,5]

index = 0
doubled_numbers = []
while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print("Original list:", numbers)
print("Doubled list:", doubled_numbers)

#5)write a while loop that repeatedly asks the user to enter a password until the correct password "password123"is entered

correct_password = "password123"

password_correct = False

while not password_correct:

    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Correct password entered. Access granted.")
        password_correct = True  
    else:
        print("Incorrect password. Please try again.")


#if-else

#1)write an if-else statement thet prints "good morning" if the current hour is less then 12 and "good afternoon" otherwise.

import datetime

current_hour = datetime.datetime.now().hour

if current_hour < 12:
    print("Good morning")
else:
    print("Good afternoon")

#2) write an if-else statement that checks if a number is even or odd. if the number is even, print "even" otherwise,print"odd"

number = 7  

if number % 2 == 0:
    print("even")
else:
    print("odd")

#3) Create an if-else statement to check if the temperature is above 30 degrees. if it is,print "it's hot outside!"; otherwise,print "it's not too hot."

temperature = int(input("ramdeni gradusia: "))

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

#4) Create an if-else statement that determines if a person is a teenager. If the age is between 13 and 19 (inclusive), print "You are a teenager!"; otherwise, print "You are not a teenager."

age = int(input("what is your age: "))

if age >= 13 and age <= 19:
    print("You are a teenager!")
else:
    print("You are not a teenager.")