"""
Solution for Project Euler Problem # 19
https://projecteuler.net/problem=19
"""
import time


def main():
    days_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days_names = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6 : 'Saturday'}

    startYear = 1901
    startday = 2

    endYear = 2000

    thisyear = startYear
    thismonth = 1
    thisday = startday

    numSundays = 0

    print 'Starting from January 1st (a ' + days_names[startday] + ') ' + str(startYear)

    while thisyear < endYear + 1:
        daysUntilNextMonth = days_months[thismonth]

        # Handle good ole February
        if thismonth == 2:
            if '000' in str(thisyear):
                if thisyear % 400 == 0:
                    daysUntilNextMonth += 1
            elif thisyear % 4 == 0:
                daysUntilNextMonth += 1

        daysOffset = daysUntilNextMonth % 7

        # Get the new day value for the first day of the Month (thisday)
        if thisday + daysOffset > 6:
            thisday = 0 + (daysOffset - (6 - thisday) - 1)  # Accounting for our zero index based dictionary
        else:
            thisday += daysOffset

        if thisday == 0:
            numSundays += 1

        if thismonth == 12:
            thismonth = 1
            thisyear += 1
        else:
            thismonth += 1


    print 'Ending on December 31st (a ' + days_names[thisday] + ') ' + str(thisyear)
    print 'There were ' + str(numSundays) + ' Sundays that occurred on the first day of the month!'
    # There were 171 that occurred on the first day of the month!

if __name__ == '__main__':
    start_time = time.time()
    main()
    print 'It took: ' + str(time.time() - start_time) + ' secs'