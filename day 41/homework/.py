#1)გადოგვეცემა რიცხვებით სავსე სია, ჩვენ ამ სიიდან უნდა შევკრიბოთ ყველა ხუთის ჯერადი რიცხვი და დავბეჭდოთ მათი ჯამი 
sum= 0
numbers =[10,30,40,11,15,90,77,25,7,2,99]
for i in range(len(numbers)):
    if numbers[i] % 5 == 0 :
        sum += numbers[i]
print(sum)


