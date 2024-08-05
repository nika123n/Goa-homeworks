#6) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს და თუ ის დადებითი იქნება, დააბრუნებს "დადებითი", და თუ უარყოფითი იქნება, "უარყოფითი".
def number():
    number = int(input("shemoitane ricxvi: "))
    if number > 0:
        return("dadebiti")
    else:
        return("uaryofiti")
print(number())