import csv
from collections import Counter

# which states have the most number of spicy dishes?
with open("indian_food.csv") as csvfile:
	reader = csv.reader(csvfile)
	first = True
	stateToFlavor = dict()
	for row in reader:
		if(first):
			first = False
			continue

		state = row[7]
		flavor = row[5]
		if state not in stateToFlavor:
			stateToFlavor[state] = Counter()
		stateToFlavor[state][flavor] += 1
 
	spicyStates = list()
	for state in stateToFlavor:
		#print ("state: " + str(stateToFlavor[state]["sweet"]))
		spicyStates.append((float(stateToFlavor[state]["spicy"]), state))

	spicyStates.sort(reverse = True)
	print ("States with the most spicy dishes: " + str(spicyStates))


# do vegetarian dishes take less time to cook?

with open("indian_food.csv") as csvfile:
	reader = csv.reader(csvfile)
	first = True
	vegTimeSum = 0
	vegTimeCount = 0

	nonVegTimeSum = 0
	nonVegTimeCount = 0

	for row in reader:
		if(first):
			first = False
			continue

		prepTime = int(row[3])
		cookTime = int(row[4])
		diet = row[2]

		if diet.lower() == "vegetarian":
			vegTimeSum += (prepTime + cookTime)
			vegTimeCount += 1
		elif diet.lower() == "non vegetarian":
			nonVegTimeSum += (prepTime + cookTime)
			nonVegTimeCount += 1

	print ("Avg veg prep/cook time: " + str(float(vegTimeSum)/vegTimeCount))
	print ("Avg nonveg prep/cook time: " + str(float(nonVegTimeSum)/nonVegTimeCount))


# ingredients in nonveg food

with open("indian_food.csv") as csvfile:
	reader = csv.reader(csvfile)
	first = True

	ingredientSet = set()

	for row in reader:
		if(first):
			first = False
			continue

		diet = row[2]
		ingredients = row[1].split(",")
		if diet.lower() == "non vegetarian":
			for item in ingredients:
				ingredientSet.add(item.lower().strip())

	l = list(ingredientSet)
	l.sort()
	print (l)

# most common meats eaten
with open("indian_food.csv") as csvfile:
	reader = csv.reader(csvfile)
	first = True

	meatSet = {"pork", "duck", "chicken", "fish", "lobster", "mutton", "prawn", "beef"}
	meatFrequency = Counter()


	for row in reader:
		if(first):
			first = False
			continue

		ingredients = row[1].split(",")
		for item in ingredients:
			item = item.lower()

			for meat in meatSet:
				if meat in item:
					meatFrequency[meat] += 1

	l = list()
	for meat in meatFrequency:
		l.append((meatFrequency[meat], meat))

	l.sort(reverse = True)
	print ("Most common meats eaten in reverse order: " + str(l))

# where is fish eaten?
with open("indian_food.csv") as csvfile:
	reader = csv.reader(csvfile)
	first = True
	stateFrequencyForFish = Counter()

	for row in reader:
		if(first):
			first = False
			continue


		ingredients = row[1].split(",")
		for item in ingredients:
			item = item.lower()
			state = row[7]

			if "fish" in item:
				stateFrequencyForFish[state] += 1

	l = list()
	for state in stateFrequencyForFish:
		l.append((stateFrequencyForFish[state], state))

	l.sort(reverse = True)

	print ("States where fish dishes are from: " + str(l))











