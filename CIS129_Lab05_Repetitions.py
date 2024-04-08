# Andrea Gonzales
# CIS129
# 04-07-2024

''' Code meant to collect the daily amount of bottles colected.
Then, uses this information to calculate the total number of 
bottles and the returning payout. Each bottle returns $.10'''

def main():
    totalBottles = 0
    counter = 1
    todayBottles = 0
    totalPayout = 0
    keepGoing = 'y'

    while keepGoing == 'y':
        totalBottles = getBottles(totalBottles, todayBottles, counter)
        totalPayout = calcPayout(totalPayout, totalBottles)
        printInfo(totalBottles, totalPayout)
        keepGoing = input("Do you want to enter another weeks worth of data? (Enter y or n) ")


def getBottles(totalBottles, todayBottles, counter):
    NBR_OF_DAYS = 7 
    todayBottles = 0
    totalBottles = 0
    counter = 1

    while counter <= 7:
        todayBottles = int(input("Enter number of bottles for day #" +str(counter)+ ": "))
        totalBottles = totalBottles + todayBottles
        counter = counter + 1
    return totalBottles


def calcPayout(totalPayout, totalBottles):
    PAYOUT_PER_BOTTLE = .10
    totalPayout = 0  # Resets to 0 for multiple runs
    totalPayout = totalBottles * .10
    return totalPayout


def printInfo(totalBottles, totalPayout):
    print("You collected " +str(totalBottles)+ " bottles this week!")
    print("You will recieve $" +str(totalPayout)+ " for the bottles.")

main()
