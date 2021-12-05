from random import random as rand
from random import randrange as randrng
from random import choice

def keygen95(): 
	genKey = str(rand())[2:12] # Generate a random set of 10 numbers to work with
	total = 0 # This will be our total sum for our modulus 7 algorithm
	uselessThree = str(genKey)[:3] # Strip the last 3 numbers from our 10
	theSeven = str(genKey)[3:] # Strip the first 7 numbers
	for i in list(str(theSeven)): # Convert them to integers
		total = total + int(i) # And then add them together

	if int(uselessThree) == True in (333, 444, 555, 666, 777, 888, 999): # Checks if our last the numbers are one of these
		print(uselessThree) # Print them for debug so we know how often this happens
	else:
		pass	# Otherwise if we're legit, move on

	if total % 7 == 0: # This is the modulus 7 algorithm Microsoft used. Any number divisible by 7 that has no remainders passes the check
		theKey = uselessThree + '-' + theSeven # Build our key string
		return theKey #Hand it off to the user
	else: # Otherwise, if our mod7 check fails
		return keygen95() # Try again until we get one

def keygen95oem(): #Even though the algorithm checks out, You may still get some losers that slip through!
    threeSixSix = str(randrng(366)) # Generate a random number between 0 and 366, this sets our date code
    if int(threeSixSix) <= 99: # If the integer generated is less than or equal to 99, pad one zero to the left
        threeSixSix = '0' + str(threeSixSix)
    if int(threeSixSix) <= 9: # If the integer generated is less than or equal to 9, pad two zeros to the left
        threeSixSix = '00' + str(threeSixSix)
    else:
        pass # We generated a number above 100, move on

    nintyFive = str(choice(['95', '96', '97', '98', '99', '00', '01', '02'])) # This is the year for the Microsoft date code
    total = 0 # and the total for our mod7 algorithm is still used
    uselessFive = str(rand())[2:7] # The last 5 numbers of the OEM key are absolutely useless, so we just make them up
    theSeven = str(rand())[3:9] # Here's the 7 for the mod7 check, BUT we're only stripping 6 numbers actually
    for i in list(str(theSeven)): # Sum our 6 numbers for the mod7 check
        total = total + int(i)

    if total % 7 == 0: # Perform mod7 check, we sum 6 numbers instead of 7 this time because OEM keys MUST have a 0 as the first digit
        theKey = threeSixSix + nintyFive + '-OEM-0' + theSeven + '-' + uselessFive # Build our key, we pad a 0 after OEM for the mod7 change
        return theKey # Pass to the user
    else:
        return keygen95oem() # Try again until we get a good key
