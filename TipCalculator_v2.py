# Creating a command line Tip Calculator v2
# This time using Flow Control as well

# I know there is more efficient ways to do this with more variety. This is just practice for a beginner.

def tipCalculatorStart():
	""" Announces welcome message and starts the program """
	print ("Welcome to Bathmatician's Tip Calculator (v2.0)")
	print ()
	tipCalculatorPercentRequest()

	
def tipCalculatorPercentRequest():
	""" Asks the user which Percentage they would like to calculate by """
	print ("Would you like to calculate by 10%, 15%, or 20%?")
	print ("(Please include numbers only, such as: 10)")
	print ()
	TipPercentage = input()
	if TipPercentage == "10":
		tipCalculator10()
	elif TipPercentage == "15":
		tipCalculator15()
	elif TipPercentage == "20":
		tipCalculator20()
	else:
		print ("Invalid Percentage. Remember to only enter 10, 15, or 20.")
		tipCalculatorPercentRequest()
	print ()
	print ('If you would like to calculate another Tip, type: anotherTip()')

def tipCalculator10():
	""" Asks the user the Total Bill, and calculates a 10% Tip """
	print()
	print ("How much is the total bill?")
	# This function cannot remove extra symbols such as $$
	print ("(Please include numbers only, such as: 33.14)")
	print ()
	TotalCost = float(input())	
	
	def tenTip():
		"""Calculates a 10% Tip rounded to full dollars """
		return str(round(float((TotalCost * 0.10))))
		
	def tenTipTotal():
		""" Calculates total Bill now inluding 10% Tip """
		return str(round(float((TotalCost * 0.10) + TotalCost), 2))
	print ()
	print ("You should give about $" + tenTip(), "extra or $" + tenTipTotal() + " total, for a 10% tip.")

def tipCalculator15():
	""" Asks the user the Total Bill, and calculates a 15% Tip """
	print()
	print ("How much is the total bill?")
	# This function cannot remove extra symbols such as $$
	print ("(Please include numbers only, such as: 33.14)")
	print ()
	
	TotalCost = float(input())	
	def fifteenTip():
		""" Calculates a 15% Tip rounded to full dollars """
		return str(round(float((TotalCost * 0.15))))
		
	def fifteenTipTotal():
		""" Calculates total Bill now inluding 15% Tip"""
		return str(round(float((TotalCost * 0.15) + TotalCost), 2))
	print ()
	print ("You should give about $" + fifteenTip(), "extra or $" + fifteenTipTotal() + " total, for a 15% tip.")
		
def tipCalculator20():
	""" Asks the user the Total Bill, and calculates a 20% Tip """
	print()
	print ("How much is the total bill?")
	# This function cannot remove extra symbols such as $$
	print ("(Please include numbers only, such as: 33.14)")
	print ()
	
	TotalCost = float(input())
	def twentyTip():
		""" Calculates a 20% Tip rounded to full dollars """
		return str(round(float((TotalCost * 0.20))))
		
	def twentyTipTotal():
		""" Calculates total Bill now inluding 20% Tip """
		return str(round(float((TotalCost * 0.20) + TotalCost), 2))
	print ()
	print ("You should give about $" + twentyTip(), "extra or $" + twentyTipTotal() + " total, for a 20% tip.")

def anotherTip():
	tipCalculatorPercentRequest()

tipCalculatorStart()

