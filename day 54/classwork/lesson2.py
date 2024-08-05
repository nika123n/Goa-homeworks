#2) შექმენით ფუნქცია რომელიც შეეკითხება მომხარებელს რიცხვს და დააბრუნებს ლუწია თუ კენტი
def number():
    number = int(input("daasaxele ricxvi: "))
    if number % 2 == 0:
        return("this number is even")
    else:
        return("this number i odd")

print(number())