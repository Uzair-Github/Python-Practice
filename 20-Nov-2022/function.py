#this is a function

#take word from user and save it in store word
store = input("Enter a word: ")

#def stands for define-function
#def func means we added a function named "func" like a new variable is introduced
def func():
#the store in function "func" is different from store of your input
#the store in function "func" is store of function, not of the whole program

    store = "Alpha"
    print ("Your word is: " ,store)

func()
#the store of program is your word that you have input it
print ("Your word is: " , store)