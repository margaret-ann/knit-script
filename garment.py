#!/usr/bin/env python
# coding: utf-8

# 'Garment' class hierarchy
class Garment:
    def __init__(self, rowGauge, colGauge, targetMeas=[], actualMeas=[]):
        self.rowGauge = rowGauge #1in gauge for now
        self.colGauge = colGauge #1in gauge for now
        self.targetMeas = targetMeas #data structure to hold target Measurement objects
        self.actualMeas = actualMeas #data structure to hold actual Measurement objects

    def getGauge(self):
        """ Return stitch size of Measurement object """
        return (self.rowGauge, self.colGauge)

    def setGauge(self, row, col):
        """ Return inch size of Measurement object """
        self.rowGauge = row
        self.colGauge = col

    def getTargetMeas(self):
        """ Return targetMeas array """
        return self.targetMeas

    def getActualMeas(self):
        """ Return actualMeas array """
        return self.actualMeas

    def addTarget(self, myName, myBool, mySize):
        """ Initialize new Target object & add it to targetMeas array """
        newTarget = Measurement(myName, myBool, mySize)
        self.targetMeas.append(newTarget)

    #todo
    def printTargets():
        """ Print out all target measurement information for Garment """
        return None
       
# 'Measurement' class hierarchy
class Measurement:
    def __init__(self, name, isWidth, inchSize):
        self.name = name
        self.isWidth = isWidth #true for width measurement
        self.inchSize = inchSize

    def setName(self, newName):
        """ Set the name variable """
        self.name = newName

    def setIsWidth(self, newBool):
        """ Set the isWidth variable """
        self.isWidth = newBool

    def setInchSize(self, newSize):
        """ Set the inchSize variable """
        self.inchSize = newSize

    def getName(self):
        """ Return the name variable """
        return self.name

    def getIsWidth(self):
        """ Return the isWidth variable """
        return self.isWidth

    def getInchSize(self):
        """ Return the inchSize variable """
        return self.inchSize

    def toStitches(self, rowGauge, colGauge):
        """ Return stitch size of Measurement object based on gauge """
        if self.isWidth:
            return self.inchSize/colGauge
        elif not self.isWidth:
            return self.inchSize/rowGauge
        else:
            return None