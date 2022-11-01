# funtions printing and returning print something in a function, its only for displaying some data, you are doing nothing with the data

# when you return in a function. you are going in another part of your program
from addfruit import add_fruit
from dividefruit import divide_fruit
from subtractfruit import subtract_fruit
from displayfruit import display_fruit
apples=int(input("how many apples?"))
oranges=int(input("how many oranges?"))

#add fruit
fruitAdd=add_fruit(apples, oranges)
#subtract fruit
fruitSubtract=subtract_fruit(apples, oranges)
#divide fruit
fruitDivide=divide_fruit(apples, oranges)
#display the added fruit, subtracted fruit, and divided fruit
display_fruit(fruitAdd, fruitSubtract, fruitDivide)