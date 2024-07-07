#1)Print all integers from 0 to 20 

for i in range(21):
   print(i) 

#2) Print the first 10 natural numbers. for loop ის გამოყენებით

for i in range(1,11):
   print(i)

#3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive for loop ის გამოყენებით

even_numbers = ""
odd_numbers = ""

for i in range(0,  101,2):
   print(i)
for i in range(1,101,2):
   print(i)

#4) Write a program that calculates and print the sum of numbers from 1 to 10 using a for loop.

sum = 0
for i in range(11):
   sum +=1
print(sum) 

#5)Enter a number to the user and then using a for loop output the sum of all the numbers up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).

num = int(input("enter number: "))
sum = 0
for i in range(num):
    sum += i
print(sum)

#Print the squares of numbers from 1 to 15.
#დაბეჭდე 1 დან 15 მდე რიცხვების კვადრატები

for i in range(1,15):
    print(i * i)




