from random import random as rand
from random import randrange as randrng
from random import choice

def keygen95():
	genKey = str(rand())[2:12]
	total = 0
	uselessThree = str(genKey)[:3]
	theSeven = str(genKey)[3:]
	for i in list(str(theSeven)):
		total = total + int(i)

	if int(uselessThree) == True in (333, 444, 555, 666, 777, 888, 999):
		print(uselessThree)
	else:
		pass

	if total % 7 == 0:
		theKey = uselessThree + '-' + theSeven
		return theKey
	else:
		return keygen95()

def keygen95oem(): #Even though the algorithm checks out, You may still get some losers that slip through!
    threeSixSix = str(randrng(366))
    if int(threeSixSix) <= 99:
        threeSixSix = '0' + str(threeSixSix)
    if int(threeSixSix) <= 9:
        threeSixSix = '00' + str(threeSixSix)
    else:
        pass

    nintyFive = str(choice(['95', '96', '97', '98', '99', '00', '01', '02']))
    total = 0
    uselessFive = str(rand())[2:7]
    theSeven = str(rand())[3:9]
    for i in list(str(theSeven)):
        total = total + int(i)

    if total % 7 == 0:
        theKey = threeSixSix + nintyFive + '-OEM-0' + theSeven + '-' + uselessFive
        return theKey
    else:
        return keygen95oem()
