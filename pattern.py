# 'Grade' class hierarchy
# Represents all sizes in the design, stores size information & orchestrates grading
import garment as g
import measurement as m

class Pattern:
    def __init__(self, rowGauge, colGauge, sizeNames, dimensionNames, sizeChart, garmentList):
       self.rowGauge = rowGauge
       self.colGauge = colGauge
       self.sizeNames = sizeNames
       self.dimensionNames = dimensionNames
       self.sizeChart = sizeChart
       self.garmentList = garmentList
       self.pattern = []

    def getSizeChart(self):
        """ Returns size chart for the pattern as nested list """
        chart = []
        head_row = ['Size']
        for dim in self.dimensionNames:
            head_row.append(dim)
        chart.append(head_row)
        for index, size in enumerate(self.sizeNames):
            row = []
            row.append(size)
            for dim in self.sizeChart[index]:
                row.append(dim)
            chart.append(row)
        return chart
    
    def appendPattern(self, newText):
        """ Append list of new lines to text pattern """
        self.pattern += newText

    def getPattern(self):
        """ Return list of lines in text pattern """
        return self.pattern

    def getStitchDimension(self, dimName):
        """ Return list of actual stitch values for all sizes """
        dimList = []
        for gar in self.garmentList:
            dimList.append(gar.actualStitchesByName(dimName))
        return dimList
    
    def getTargetCmDimension(self, dimName):
        """ Return list of target cm values for all sizes """
        dimList = []
        for gar in self.garmentList:
            dimList.append(gar.targetSizeByNameCm(dimName))
        return dimList
    
    def formatDimension(self, dim):
        """ Return a string that formats list for use in text pattern """
        dimStr = "{"
        for index, val in enumerate(dim):
            dimStr += f"{val}"
            if index < len(dim) - 1:
                dimStr += ", "
        dimStr += "}"
        return dimStr