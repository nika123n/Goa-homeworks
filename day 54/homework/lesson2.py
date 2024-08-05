#2) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცვს და დააბრუნებს "მაგარია!", თუ რიცხვი 10-ზე მეტია.
def numbers():
    number = int(input("shemoitane ricxvi: "))
    if number > 10:
        return("gerate")
    else:
        return number
print(numbers())