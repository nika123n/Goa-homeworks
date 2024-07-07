#1) მომხმარებელს შემოატანინეთ ათი რიცხვი, ეს რიცხვები დაამატეთ სიაში, ამ სიიდან დაახარისხეთ ეს რიცხვები ორ ჯგუფად, რიცხვები რომლებიც მეტია 100 ზე და რიცხვები რომლებიც ნაკლებია 100 ზე
it_is_more_100=[]
it_is_less_100=[]
numbers=[]
for i in range(10):
    number=input("დაასახელე ნებისმიერი 10 რიცხვი: ")
    numbers.append(number)

it_is_more_100 = []
it_is_less_100 = []

for number in numbers:
    if numbers <= 100:
        it_is_more_100.append(number)
    else:
        it_is_less_100.append(number)

print("100ze meti ricxvebi: ",it_is_more_100)
print("100ze naklebi ricxvebi: ",it_is_less_100)