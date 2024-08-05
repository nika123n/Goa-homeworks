#7) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.
def number():
    number = int(input("shemoitane ricxvi: "))
    if number % 2 == 0:
        return("True")
    else:
        return("Folse")
print(number())