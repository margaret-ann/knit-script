# 'Garment' class hierarchy
# Represents one size of one design, holds 'Measurement' objects
import measurement as m

class Garment:
    def __init__(self, rowGauge, colGauge, measList=[]):
        self.rowGauge = rowGauge #10cm gauge
        self.colGauge = colGauge #10cm gauge
        self.measList = measList #data structure to hold Measurement objects
        self.pattern = [] #pattern text by line

    def getGauge(self):
        """ Return stitch size of Measurement object """
        return (self.rowGauge, self.colGauge)
    
    def getRowGauge(self):
        """ Return row gauge """
        return self.rowGauge
    
    def getColGauge(self):
        """ Return column gauge """
        return self.colGauge

    def appendPattern(self, newText):
        """ Append list of new lines to text pattern """
        self.pattern += newText

    def getPattern(self):
        """ Return list of lines in text pattern """
        return self.pattern
    
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
        newTarget = m.Measurement(myName, myIsWidth, mySize, myDiv, myIsOdd)
        self.measList.append(newTarget)

    def printTargetMeas(self):
        """ Print out all target measurement information for Garment """
        for each in self.measList:
            print(f"{each.getName()}, {each.getTargetSizeIn()} inches, {each.getTargetStitches()} stitches")
        return self.measList
    
    def printActualMeas(self):
        """ Print out all actual measurement information for Garment """
        for each in self.measList:
            print(f"{each.getName()}, {each.getActualSizeIn()} inches, {each.getActualStitches()} stitches")
        return self.measList
    
    def printSummary(self):
        """ Print summary of all design measurements """
        for each in self.measList:
            print(f"{each.getName()}; Stitches {each.getTargetStitches()} -> {each.getActualStitches()};")
        return self.measList
    
    def targetStitchesByName(self, searchName):
        """ Return the number of stitches in target Measurement by name """
        for each in self.measList:
            if searchName == each.getName():
                return each.getTargetStitches()
        return None
    
    def actualStitchesByName(self, searchName):
        """ Return the number of stitches in target Measurement by name """
        for each in self.measList:
            if searchName == each.getName():
                return each.getActualStitches()
        return None
    
    def targetSizeByNameCm(self, searchName):
        """ Return the size in inches of target Measurement by name """
        for each in self.measList:
            if searchName == each.getName():
                return each.target_cm
        return None
    
    def actualSizeByNameCm(self, searchName):
        """ Return the size in inches of actual Measurement by name """
        for each in self.measList:
            if searchName == each.getName():
                return each.getActualCm()
        return None
    
    def calculateMeasurements(self, rowGauge, colGauge):
        """ Calculate actualSize_in values for all Measurement objects stored in Garment.targetMeas """
        for each in self.measList:
            each.calculateMeasurement(rowGauge, colGauge)
