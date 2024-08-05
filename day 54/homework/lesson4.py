# 4) შექმენი ფუნქცია, რომელიც მომხმარებელს შემოატანინებს ტექსტს და დააბრუნებს ტექსტის სიგრძეს
def text():
    text = input("what is your name? ")
    return(len(text))
print(text())