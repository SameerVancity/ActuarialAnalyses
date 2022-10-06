import random
import numpy as np
import pandas as pd
from numpy.random import seed
from numpy.random import randint
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import sqlite3


# ############ Notes ###########################################
# Rule - Each member record has a memberID, DOB, Gender, LOB, incepDate, termDate
# Rule - DOB values are restricted to a chosen range
# Rule - Inception date values are restricted to a chosen range and greater than the DOB
# Rule - Assume all policies terminate according to a daily geometric distribution
# Rule - Assume all policy periods are continuous from inception until termination
# Rule - Each loss record has a memberID, DOS, DOP, ProcCd, Billed, Allowed, Paid, Units, ClaimID, ClaimLine
# Procedure - Want to simulate the member table first, and then simulate losses assigning each record to a memberID


# ######### Step 1 - Define Functions ####################

# function that randomly selects a given number of dates from within a given range with replacement and equal weight
def randDate(minDate, maxDate, dateCount):
    # Step 1.1 - Create the (immutable) tuple  of dates from which a date element
    # will be randomly selected (i.e. the sample space)
    dateSet = ()
    dateElement = minDate
    while dateElement <= maxDate:
        dateSet = dateSet + (dateElement,)
        dateElement = dateElement + timedelta(1)

    # Step 1.2 - Create the set of weights to be applied to the set of dates above - for now, use uniform distribution
    dateWeightSet = ([1]*len(dateSet))

    # Step 1.3 - Randomly select from the dateSet
    return random.choices(dateSet, dateWeightSet, cum_weights=None, k=dateCount)


# ######### Step 2 - Set Member Data Parameters ####################
# set the memberCount
memberCount = 10000
# set the DOB allowed range
dobFirst = date(1921, 1, 1)
dobLast = date(2021, 12, 31)
# set the LOB values
lobValues = ('bronze', 'silver', 'gold')
# set the inception date range and the daily probability of non-renewal
inceptDateMin = date(2018, 1, 1)
inceptDateMax = date(2021, 12, 31)
termProb = 0.004  # daily probability of policy termination

# #########Step 3 - Simulate Member data #####################

# 3.1 - simulate memberID as a 6 digit integer
memberID = randint(100000, 999999, memberCount)

# 3.2 - simulate DOB as on or after a given date (can enhance to build in the age distribution here)
# create a tuple (immutable) of DOB date values that will be randomly selected from
dob = randDate(dobFirst, dobLast, memberCount)

# 3.3 - Gender
gender = np.random.choice(['M', 'F'], memberCount, replace=True)

# 3.4 - LOB
lob = np.random.choice(lobValues, memberCount, replace=True)

# 3.5 - Inception Date
randInceptDate = randDate(inceptDateMin, inceptDateMax, memberCount)
inceptDate = np.maximum(dob, randInceptDate)

# 3.6 - Termination Date - Simulate the number of months until termination as geometric
policyDuration = np.random.geometric((termProb), memberCount)
# create termDate - would be better to avoid looping here
termDate = ()
for x in range(0, memberCount):
    z = np.datetime64(InceptDate[x]) + np.timedelta64(policyDuration[0], 'D')
    termDate = termDate + (np.datetime64(z),)

# ############End Step ###########################################

# #########Step 4 - Simulate loss data ####################
# Rule - Assume a poisson frequency and log-normal severity distribution for loss by member
# Simulate losses as a whole, and then randomly allocate those losses to the membership assuming a uniform distribution

# 4.1 - Set the loss parameters

lossLambda = 2.0
lossMu = 3.0
lossSigma = 3.0

# 4.2 - Simulate the losses
# each loss has a memberID, DOS, and Incurred Amount
# for each member, simulate the number of losses and amount for each
losses_memberID = np.arrray()
losses_DOS = np.array()
losses_Amount = np.array()

for x in range(0, memberCount):
    lossCount = random.poisson(lam=lossLambda*(termDate-inceptDate).days)
    lossesIncurred = random.lognormal(lossMu, lossSigma, lossCount)
    losses = losses + lossesIncurred

#############################################################################################

