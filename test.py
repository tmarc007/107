print("Hello world!")

# let variable = 21;
variable = 21
name = "Tom"
last_name = "Marcello"
total = 23.65
age = 21
found = True

# if / else statement
# if(var==var2){
# logic
# }
if age < 100:
    print("You're not that old")
elif age == 100:
    print("congratz you're not that old")
else:
    print("sorry it seems that you're old")
# functions use def to define functions
# functions in JS: say_hello(){}

def say_hello():
    print("Hello there")

def say_goodbye(name):
    print("Goodbye" + name)

# Call a function
say_hello()
say_goodbye("Tom")

# Concatinate
print("Hello my name is " + name + ", and I am " + str(age) + " years old")



