import random
import numpy as np
from numpy.random import seed
from numpy.random import randint
from datetime import date, timedelta
import sqlite3


# ############Notes###########
# Future Enhancements - build a random date function with weights, range, etc.
# Rule - Each member record has a memberID, DOB, Gender, LOB, incepDate, termDate
# Rule - Assume all policy periods are continuous from inception until termination
# Rule - Each loss record has a memberID, DOS, DOP, ProcCd, Billed, Allowed, Paid, Units, ClaimID, ClaimLine
# Procedure - Want to simulate the member table first, and then simulate losses assigning each record to a memberID

# function that randomly selects a given number of dates from within a given range with replacement and equal weight
def randDate(minDate, maxDate, dateCount):
    # Step 1 - Create the set of dates from which a date element will be randomly selected (i.e. the sample space)
    dateSet = ()
    dateElement = minDate
    while dateElement <= maxDate:
        dateSet = dateSet + (dateElement,)
        dateElement = dateElement + timedelta(1)

    # Step 2 - Create the set of weights to be applied to the set of dates above - for now, use uniform distribution
    dateWeightSet = ([1]*len(dateSet))

    # Step 3 - Randomly select from the dateSet
    return random.choices(dateSet, dateWeightSet, cum_weights=None, k=dateCount)





# #########Step 1 - Set parameters####################
# set the memberCount
memberCount = 10000
# set the DOB allowed range
dobFirst = date(1921, 1, 1)
dobLast = date(2021, 12, 31)
# set the UW period allowed range - this is the allowed inception date range
incpetionMinDate = date(2018, 1, 1)
incpetionMaxDate = date(2021, 12, 31)
# set the LOB values
lob = ('bronze', 'silver', 'gold')
# #########Step 2 - Simulate data#####################

# 2.1 - simulate memberID as a 6 digit integer
memberID = randint(100000, 999999, memberCount)

# 2.2 - simulate DOB as on or after a given date (can enhance to build in the age distribution here)
# create a tuple (immutable) of DOB date values that will be randomly selected from
dobDates = ()
dobDate = dobFirst
while dobDate <= dobLast:
    dobDates = dobDates + (dobDate,)
    dobDate = dobDate + timedelta(1)
# Check - print(dobDates)
# Randomly select the DOB values from the dobDates tuple
dob = np.random.choice(dobDates, memberCount, replace=True)
print(dob)

# 2.3 - Gender
gender = np.random.choice(['M', 'F'], memberCount, replace=True)
print(gender)

# 2.4 - LOB
lob = np.random.choice(['M', 'F'], memberCount, replace=True)

# 2.5 - Inception Date
randDate(incpetionMinDate,incpetionMaxDate,memberCount)
# 2.5 - Termination Date - Assume 1 year policies only

# ############End Step ###########################################


#############################################################################################
#Random Thoughts

# print(random.choice((3, 6, 9)))
# print (random.randint(1,10))

# print(random.choice(('Bob', 'Sam', 'Fred')))

# randomlist = random.sample(range(10,30),3)
# print(randomlist)

