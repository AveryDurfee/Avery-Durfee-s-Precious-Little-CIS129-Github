#Program for CIS129 course. Takes order at coffee shop and prints receipt
#prices of things sold at shop
coffeePrice = 5.00
muffinPrice = 4.00
applePrice = 1.50
mossBowlPrice = 23.25
#sales tax percent
tax = 0.06

#asks user how many coffees, muffins, apples, and bowls of moss were bought, and stores input
numCoffees = int(input("How many coffees do you want to buy?"))
numMuffins = int(input("How many muffins do you want to buy?"))
numApples = int(input("How many apples do you want to buy?"))
numMossBowls = int(input("How many bowls of delicious moss do you want to buy?"))
#calculates subtotal of items bought
coffeeTotal = numCoffees * coffeePrice
muffinTotal = numMuffins * muffinPrice
appleTotal = numApples * applePrice
mossTotal = numMossBowls * mossBowlPrice
subtotal = coffeeTotal + muffinTotal + appleTotal + mossTotal
#Calculates tax
taxTotal = subtotal * tax
#calculates final total
total = subtotal + taxTotal

#Prints out receipt
print("***************************************\nMy Coffee and Muffin Shop \nNumber of coffees bought?\n", numCoffees)
print("Number of muffins bought?\n", numMuffins)
print("Number of apples bought\n", numApples)
print("Bowls of moss bought\n", numMossBowls)
print("***************************************\n\n***************************************\n")
print("My Coffee and Muffin Shop Receipt\n")
print(numCoffees, " Coffee at $5 each: $ ", coffeeTotal)
print(numMuffins, " Muffins at $4 each: $ ", muffinTotal)
print(numApples, " Apples at $1.50 each: $ ", appleTotal)
print(numMossBowls, " Bowls of Moss at $23.25 each: $ ", mossTotal)
print("6% tax: $ ", taxTotal, "\n---------")
print("Total: $ ", total)
print("***************************************")
