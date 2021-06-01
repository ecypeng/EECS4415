#!/usr/bin/python

import sys 

previousBusiness = None
previousDay = None
sumCheckins = 0
outputFile = open('checkinbyday.txt', 'w')

for line in sys.stdin:
        businessId, weekDay, sumCheckins = line.split(', ')
        if businessId != previousBusiness:
                # for the case where it's none (for the first business)
                if previousBusiness is not None:
                        if weekDay != previousDay:
                                if previousDay is not None:
                                        outputFile.write(previousBusiness + ', ' + previousDay + ', '+ str(sumCheckins))
        # initializing for first entry of a business
        previousBusiness = businessId
        previousDay = weekDay
        sumCheckins = 0
               
        sumCheckins = sumCheckins + int(numCheckIns)    
outputFile.write(str(previousBusiness) + ', ' + str(previousDay) + ', ' + str(sumCheckins))
