#assigning list with fruits
fruits = ["apple", "banana", "cherry"]

#printing fruits as a list
print (fruits)

#printing fruit second value (apple = 0, banana = 1, cherry = 2)
print (fruits[1])

#replacing first value with orange
fruits[0] = "orange"
print (fruits[0])

#adding new item in list
fruits.append("kiwi")
print (fruits)

#adding item i.e. lemon before banana
fruits.insert(1, "lemon")
print (fruits)

#removing item i.e. cherry from list
fruits.remove("cherry")
print (fruits)