#!/usr/bin/env python
# coding: utf-8

# 'Garment' class hierarchy
class Garment:
    def __init__(self, rowGauge, colGauge, measList=[]):
        self.rowGauge = rowGauge #1in gauge for now
        self.colGauge = colGauge #1in gauge for now
        self.measList = measList #data structure to hold Measurement objects

    def getGauge(self):
        """ Return stitch size of Measurement object """
        return (self.rowGauge, self.colGauge)
    
    def getRowGauge(self):
        """ Return row gauge """
        return self.rowGauge
    
    def getColGauge(self):
        """ Return column gauge """
        return self.colGauge

    def setGauge(self, row, col):
        """ Set row & column gauge of garment """
        self.rowGauge = row
        self.colGauge = col

    def setRowGauge(self, row):
        """ Set row gauge of garment """
        self.rowGauge = row

    def setColGauge(self, col):
        """ Set column gauge of garment """
        self.colGauge = col

    def getMeasList(self):
        """ Return measList array """
        return self.measList

    def addTarget(self, myName, myIsWidth, mySize, myDiv=[], myIsOdd=None):
        """ Initialize new Target object & add it to targetMeas array """
        newTarget = Measurement(myName, myIsWidth, mySize, myDiv, myIsOdd)
        self.measList.append(newTarget)

    def printTargetMeas(self):
        """ Print out all target measurement information for Garment """
        for each in self.measList:
            print(f"{each.getName()}, {each.getTargetSizeIn()} inches, {each.getTargetStitches(self.getRowGauge(), self.getColGauge())} stitches")
        return self.measList
    
    def printActualMeas(self):
        """ Print out all actual measurement information for Garment """
        for each in self.measList:
            print(f"{each.getName()}, {each.getActualSizeIn()} inches, {each.getActualStitches(self.getRowGauge(), self.getColGauge())} stitches")
        return self.measList
    
    def printSummary(self):
        """ Print summary of all design measurements """
        for each in self.measList:
            print(f"{each.getName()}; Stitches {each.getTargetStitches(self.getRowGauge(), self.getColGauge())} -> {each.getActualStitches()};")
        return self.measList
    
    def targetStitchesByName(self, searchName):
        """ Return the number of stitches in target Measurement by name """
        for each in self.measList:
            if searchName == each.getName():
                return each.getTargetStitches(self.rowGauge, self.colGauge)
        return None
    
    def actualStitchesByName(self, searchName):
        """ Return the number of stitches in target Measurement by name """
        for each in self.measList:
            if searchName == each.getName():
                return each.getActualStitches()
        return None
    
    def targetSizeByName(self, searchName):
        """ Return the size in inches of target Measurement by name """
        for each in self.measList:
            if searchName == each.getName():
                return each.getTargetSizeIn()
        return None
    
    def actualSizeByName(self, searchName):
        """ Return the size in inches of actual Measurement by name """
        for each in self.measList:
            if searchName == each.getName():
                return each.getActualSizeIn()
        return None
    
    def calculateMeasurements(self, rowGauge, colGauge):
        """ Calculate actualSize_in values for all Measurement objects stored in Garment.targetMeas """
        for each in self.measList:
            each.calculateMeasurement(rowGauge, colGauge)
       
# 'Measurement' class hierarchy
class Measurement:

    def __init__(self, name, isWidth, target_cm, colGauge_4cm, rowGauge_4cm, divBy=[1], isOdd=None):
        self.name = name
        self.isWidth = isWidth #true if width measurement, false if height
        self.target_cm = target_cm
        self.colGauge = colGauge_4cm/4
        self.rowGauge = rowGauge_4cm/4
        self.divBy = divBy #list of numbers that measurement must be divisible by
        self.isOdd = isOdd #true if measurement must by odd
        self.target_in = target_cm / 2.54

        #Calculate target stitches
        if self.isWidth:
            self.targetStitches = self.target_cm*self.colGauge
        elif not self.isWidth:
            self.targetStitches = self.target_cm*self.rowGauge
        else:
            print("Error")

        #Calculate new stitch measurement that meets requirements
        self.actualStitches = self.calculateMeasurement()

        #Calculate actual in & cm measurements based on actual stitch count
        if self.isWidth:
            self.actual_cm = self.actualStitches/self.colGauge
            self.actual_in = self.actual_cm / 2.54
        elif not self.isWidth:
            self.actual_cm = self.actualStitches/self.rowGauge
            self.actual_in = self.actual_cm / 2.54
        else:
            print("Error")

        #Calculate % error
        self.error = abs((self.actual_cm-self.target_cm)/self.target_cm)*100

    def getTargetStitches(self):
        """ Return targetStitches variable """
        return self.targetStitches
    
    def getActualStitches(self):
        """ Return actualStitches variable """
        return self.actualStitches
    
    def getActualCm(self):
        """ Reutrn actual_cm variable """
        return self.actual_cm
    
    def setActualStitches(self, newStitchCount):
        """ Set the actualStitches variable """
        self.actualStitches = int(newStitchCount)

    def printSummary(self):
        """ Print user readable summary of this measurement """
        print(f"{self.name}; {self.target_cm}cm target; {self.target_in}in target; ")

    def getSummary(self):
        """ Return CSV summary of this measurement """
        return(f"{self.name}; {self.target_cm}; {self.target_in}; {self.targetStitches}; {self.actualStitches}; {self.actual_cm}; {self.actual_in}; {self.error}")
        
    def calculateMeasurement(self, roundUp=True):
        """ Calculate measurement that will meet requirements """

        #If required, add 1 stitch to an even target
        #if self.isOdd and stitch_num % 2 == 1:
            #stitch_num = stitch_num + 1

        #Simplify divisibiliy list
        del_list = []
        for value1 in self.divBy:
            for value2 in self.divBy:
                if value1 != value2 and value1 % value2 == 0:
                    del_list.append(value2)

        for each in del_list:
            if each in self.divBy:
                self.divBy.remove(each)

        #Multiply the numbers to get interval
        mult_num = 1
        for each in self.divBy:
            mult_num = each * mult_num

        #Rounding
        # Case 1: all requirements met
        if self.targetStitches % mult_num == 0:
            return int(self.targetStitches)
        # Case 2: div num is larger than stitch target, need to round up
        elif mult_num > self.targetStitches:
            return int(mult_num)
        # Case 3: div num is smaller than stitch target, want to round up
        elif roundUp: #round up
            return int(self.targetStitches + (mult_num - (self.targetStitches % mult_num)))
        # Case 4: div num is smaler than stitch target, want to round down
        else:
            return int(self.targetStitches - (self.targetStitches % mult_num))