#-------------------------------------------------------------------------------
# Author:       Callen Wang Quansen
# Created:      Oct 8, 2017
# Last updated: Oct 9, 2017
#
# Execution:    python coinchange.py
#
# This program determines the minimum number of coins for a particular value.
#
#-------------------------------------------------------------------------------

def minimumcoins(cents):
    # YOUR CODE HERE
    numCoin = 0
    while (cents >= 25):
        numCoin += cents//25
        cents = cents % 25
    while (cents >= 10 and cents < 25):
        numCoin += cents // 10
        cents = cents % 10
    while (cents >= 5 and cents <10):
        numCoin += cents // 5
        cents = cents % 5
    while (cents >=1 and cents <5):
        numCoin += cents
        cents = 0
    return numCoin
result = minimumcoins(7932)
print(result)


#-------------------------------------------------------------------------------
# Author:       Callen Wang Quansen
# Created:      Oct 8, 2017
# Last updated: Oct 9, 2017
#
# Execution:    python coinchange.py
#
# This program determines the minimum number of coins for a particular value.
#
#-------------------------------------------------------------------------------

def minimumcoins(cents):
    # YOUR CODE HERE
    numCoin = 0
    left = 0
    if cents >= 25:
        numCoin += (cents//25)
        left = cents % 25
        numCoin += minimumcoins(left)
    elif cents >= 10 and cents < 25:
        numCoin += (cents//10)
        left = cents % 10
        numCoin += minimumcoins(left)
    elif cents >= 5 and cents < 10:
        numCoin += (cents//5)
        left = cents % 5
        numCoin += minimumcoins(left)
    elif cents >= 1 and cents < 5:
        numCoin += cents
    return numCoin
result = minimumcoins(41)
print(result)

#-------------------------------------------------------------------------------
#  Author:          Callen Wang Quansen
#  Created:         Oct 15, 2017
#  Last updated:    Oct 16, 2017
#
#  Execution:       python bookidentifier.py
#
#  This program checks the validity of ISBN codes.
#  Valid ISBN:      YES
#  Invalid ISBN:    NO
#
#  Valid test values:
#  "0789751984"
#  "0321776410"
#  "0321842685"
#
#  Invalid test values:
#  "0789751985"
#  "5558675309"
#  "6178675309"
#
#-------------------------------------------------------------------------------

def validatebook(isbncode):
    # YOUR CODE HERE
    nameList = [int(x) for x in str(isbncode)]
    sum = 0
    for i in range(0, 9):
        sum += (i+1)*nameList[i]
    if (sum % 11 == nameList[9]:
        return "YES"
    return "NO"
result = validatebook("0789751984")
print(result)

#-------------------------------------------------------------------------------
#  Author:          Callen Wang Quansen
#  Created:         Oct 15, 2017
#  Last updated:    Oct 16, 2017
#
#  Execution:       python bookidentifier.py
#
#  This program checks the validity of ISBN codes.
#  Valid ISBN:      YES
#  Invalid ISBN:    NO
#
#  Valid test values:
#  "0789751984"
#  "0321776410"
#  "0321842685"
#
#  Invalid test values:
#  "0789751985"
#  "5558675309"
#  "6178675309"
#
#-------------------------------------------------------------------------------

def validatebook(isbncode):
    # YOUR CODE HERE
    total=0
    for i in range(0,9):
        total+=int(isbncode[i])*(i+1)
    if(total % 11 == int(isbncode[-1])):
        return "YES"
    return "NO"
result = validatebook("0789751984")
print(result)