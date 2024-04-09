#Program for CIS129 course. Takes order at coffee shop and prints receipt
#prices of things sold at shop
coffeePrice = 5.00
muffinPrice = 4.00
#sales tax percent
tax = 0.06

#asks user how many coffees and muffins were bought, and stores input
numCoffees = int(input("How many coffees do you want to buy?"))
numMuffins = int(input("How many muffins do you want to buy?"))
#calculates subtotal of coffee and muffins
coffeeTotal = numCoffees * coffeePrice
muffinTotal = numMuffins * muffinPrice
subtotal = coffeeTotal + muffinTotal
#Calculates tax
taxTotal = subtotal * tax
#calculates final total
total = subtotal + taxTotal

#Prints out receipt
print("***************************************\nMy Coffee and Muffin Shop \nNumber of coffees bought?\n", numCoffees)
print("Number of muffins bought?\n", numMuffins)
print("***************************************\n\n***************************************\n")
print("My Coffee and Muffin Shop Receipt\n", numCoffees, " Coffee at $5 each: $ ", coffeeTotal)
print(numMuffins, " Muffins at $4 each: $ ", muffinTotal)
print("6% tax: $ ", taxTotal, "\n---------")
print("Total: $ ", total)
print("***************************************")