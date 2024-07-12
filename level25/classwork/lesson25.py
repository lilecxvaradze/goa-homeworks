name = input("please enter your name: ")

print(name.capitalize())

name = input("please enter your name: ")

print(name.upper())

name = "lile".capitalize()
print(name)

name = "lile".upper()
print(name)

name = "LILE".lower()
print(name)

sentence = "my name is lile"

how_much = sentence.count("m")
print(how_much)

#lower მეთოდი გვეხმარება დიდი ასოებით დაწერილი სიტყვა გარდავქმნათ პატარად
#count მეთოდი კი იმაში გვეხმარება რომ დავითვალოთ რომელიმე სიტყვა ან ასო წინადადებაში

sentence = "hello my name is lile."

index = sentence.find("name")

print(index) 
#find()-ის გამოყენების დროს გვიბრუნდება -1 როცა არ გვაქვს მოცემული სიტყვა ან ასო.

sentence2 = "hi lile,i am luka."

index2 = sentence2.index("lile")

print(index2)
#index()-ის დროს კი error.



emails = []

count = int(input("Please enter how many emails do you want to input: "))

for i in range(count):
    email = input("Please enter email: ")

    if email.endswith("@gmail.com"):
        emails.append(email)
        print("Email was correct")
    else:
        print("Invalid email")


print(emails)