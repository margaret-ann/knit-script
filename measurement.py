# 'Measurement' class hierarchy
# Represents one measurement within one size of a garment
class Measurement:

    def __init__(self, name, isWidth, target_cm, colGauge_10cm, rowGauge_10cm, divBy=[1], isOdd=None, rounding='error'):
        self.name = name
        self.isWidth = isWidth #true if width measurement, false if height
        self.target_cm = target_cm
        self.colGauge = colGauge_10cm/10
        self.rowGauge = rowGauge_10cm/10
        self.divBy = divBy #list of numbers that measurement must be divisible by
        self.isOdd = isOdd #true if measurement must by odd
        self.rounding = rounding #'error', 'up', 'down'
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
        """ Return actual_cm variable """
        return self.actual_cm
    
    def getName(self):
        """ Return name variable """
        return self.name
    
    def setActualStitches(self, newStitchCount):
        """ Set the actualStitches variable """
        self.actualStitches = int(newStitchCount)

    def printSummary(self):
        """ Print user readable summary of this measurement """
        print(f"{self.name}; {self.target_cm}cm target; {self.target_in}in target; ")

    def getSummary(self):
        """ Return CSV summary of this measurement """
        return(f"{self.name}; {self.target_cm}; {self.target_in}; {self.targetStitches}; {self.actualStitches}; {self.actual_cm}; {self.actual_in}; {self.error}")
        
    def calculateMeasurement(self):
        """ Calculate measurement that will meet requirements """

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
        roundUp = int(self.targetStitches + (mult_num - (self.targetStitches % mult_num)))
        roundDown = int(self.targetStitches - (self.targetStitches % mult_num))  
        
        # Case 1: all requirements perfectly met
        if self.targetStitches % mult_num == 0:
            return int(self.targetStitches)
        # Case 2: div num is larger than stitch target, need to round up to avoid zero stitch count
        elif mult_num > self.targetStitches:
            return int(mult_num)
        # Case 3: div num is smaller than stitch target, choose to round up
        elif self.rounding == 'up':
            return roundUp
        # Case 4: div num is smaler than stitch target, choose to round down
        elif self.rounding == 'down':
            return roundDown
        # Case 5: round based on smallest error
        else:
            if self.isWidth:
                actual_cm_up = roundUp / self.colGauge
                actual_cm_down = roundDown / self.colGauge
            else:
                actual_cm_up = roundUp / self.rowGauge
                actual_cm_down = roundDown / self.rowGauge

            errorUp = abs((actual_cm_up-self.target_cm)/self.target_cm)*100
            errorDown = abs((actual_cm_down-self.target_cm)/self.target_cm)*100

            if errorUp < errorDown:
                return roundUp
            else:
                return roundDown
