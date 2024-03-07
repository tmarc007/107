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

#array (lists and arrays are the same thing)
#list
color = ["white","red","black","blue"]
numberList = [1,2,3]

#add
color.append("pink")

#travel the list
for colors in color:
    print(colors)

print(color[0])

# for(i=0;color.len;i++)
    # let temp = color[i]
      # console.log(temp)
    
#dictionary
me={
    "first_name":"Tom",
    "month":"July",
    "last_name":"Marcello",
    "age":21,
}
print(me["first_name"])

me["age"] = 99
me["color"] = "Blue"
print(me)


