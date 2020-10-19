#Ask user for name
name = input("What is your name? : ")

#Ask user for age
age = input("How old are you? : ")

#Ask user for city
city = input("What city do you live in? : ")

#Ask user what you enjoy
love = input("What do you love doing? : ")

#Create output text
string = "Your name is {} and you are {} years old. you live in {} and you love {}."
output = string.format(name,age,city,love)

#Print output on screen
print(output)
