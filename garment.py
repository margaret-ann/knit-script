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

    actualSize_in = None
    actualStitches = None

    def __init__(self, name, isWidth, targetSize_in, divBy, isOdd):
        self.name = name
        self.isWidth = isWidth #true if width measurement, false if height
        self.targetSize_in = targetSize_in
        self.divBy = divBy #list of numbers that measurement must be divisible by
        self.isOdd = isOdd #true if measurement must by odd

    def setName(self, newName):
        """ Set the name variable """
        self.name = newName

    def setIsWidth(self, newBool):
        """ Set the isWidth variable """
        self.isWidth = newBool

    def setTargetSizeIn(self, newSize):
        """ Set the targetSize_in variable """
        self.targetSize_in = newSize

    def setActualSizeIn(self, newSize):
        """ Set the actualSize_in variable """
        self.actualSize_in = newSize

    def getName(self):
        """ Return the name variable """
        return self.name

    def getIsWidth(self):
        """ Return the isWidth variable """
        return self.isWidth

    def getTargetSizeIn(self):
        """ Return the inchSize variable """
        return self.targetSize_in
    
    def getDivBy(self):
        """ Return the divBy variable """
        return self.divBy
    
    def getIsOdd(self):
        """ Return the isOdd variable """
        return self.isOdd
    
    def getActualSizeIn(self):
        """ Return the actualSize_in variable """
        return self.actualSize_in
    
    def getActualStitches(self):
        """ Return the actualStitches variable """
        return self.actualStitches

    def getTargetStitches(self, rowGauge, colGauge):
        """ Return stitch size of target design measurement based on gauge """
        if self.isWidth:
            return self.targetSize_in*colGauge
        elif not self.isWidth:
            return self.targetSize_in*rowGauge
        else:
            return None
        
    def calculateMeasurement(self, rowGauge , colGauge, roundUp=True):
        """ Update actual measurement based on current divisibility requirements """
        stitch_num = self.getTargetStitches(rowGauge, colGauge)

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
        if stitch_num % mult_num == 0:
            self.actualStitches = stitch_num
        # Case 2: div num is larger than stitch target, need to round up
        elif mult_num > stitch_num:
            self.actualStitches = mult_num
        # Case 3: div num is smaller than stitch target, want to round up
        elif roundUp: #round up
            self.actualStitches = stitch_num + (mult_num - (stitch_num % mult_num))
        # Case 4: div num is smaler than stitch target, want to round down
        else:
            self.actualStitches = stitch_num - (stitch_num % mult_num)