############################################################
# Calculate price, cost, or margin given any two numbers.
# prepared 2012-01-10
# version 1.0
############################################################

def margin(p, c): #returns the margin given price and cost
	return p-c
	
def margin_rate(p, c): #returns the margin rate give price and cost
	return float((p-c)/p)
	
def price(c, mr): #returns price given a cost and desired margin
	return c / (1 - (mr / 100.00))
	
def cost(p, mr): #returns cost given the price and the desired margin
	return p - (mr * p / 100.00)

calc = raw_input(
"""What would you like to calculate; 
margin, 
margin rate, 
price 
cost? 
""")

if calc == "margin":
	price = int(input("What is the price? "))
	cost = int(input("What is the cost? "))
	m = margin(price, cost)
	print "Then margin is %d " % (m)

elif calc == "margin rate":
	price = float(raw_input("What is the price? ")) # needs to allow for floating point numbers.
	cost = float(raw_input("What is the cost? "))
	mr = margin_rate(price, cost)
	print "Then the margin rate is %.2f " % (mr) #.2f is the format string to print floats out to two decimel places.
	
elif calc == "price":
	cost = float(input("What is the cost? "))
	margin_rate = float(input("What is the margin rate? "))
	p = price(cost, margin_rate)
	print "Then price is %.2f " % (p)
	
elif calc == "cost":
	price = float(input("What is the price? "))
	margin_rate = float(input("What is the margin rate? "))
	c = cost(price, margin_rate)
	print "Then cost is %.2f " % (c)
	
else:
	print "You suck."
	print "Try again dumbass."

print ""
	# how do I loop this back to line 13?