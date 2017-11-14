# File: statements.py
# Template file for Informatics 2A Assignment 2:
# 'A Natural Language Query System in Python/NLTK'

# John Longley, November 2012
# Revised November 2013 and November 2014 with help from Nikolay Bogoychev
# Revised November 2015 by Toms Bergmanis
# Revised October 2017 by Chunchuan Lyu


# PART A: Processing statements

def add(lst,item):
    if (item not in lst):
        lst.insert(len(lst),item)

class Lexicon:
    """stores known word stems of various part-of-speech categories"""
    def __init__ (self):
        self.stems = {}
        self.validTags = ["P","N","A","I","T"]

    def add (self, stem, cat):
        if not(cat in self.validTags):
            raise ValueError("Category: " + cat + " is not valid!")
        for key in self.stems:
            if (key == stem):
                if not(cat in self.stems[key]):
                    self.stems[stem].append(cat)
                    return 0

        self.stems[stem] = [cat]
        return 1

    def getAll(self, cat):
        toReturn = []
        for key in self.stems:
            if cat in self.stems[key]:
                toReturn.append(key)

        return toReturn

    def printStems (self):
        print(self.stems)

class FactBase:
    """stores unary and binary relational facts"""
    def __init__ (self):
        self.unary = {}
        self.binary = {}
    def addUnary(self,pred,e1):
        if pred in self.unary:
            self.unary[pred].append(e1)
        else:
            self.unary[pred] = [e1]
    def addBinary(self,pred,e1,e2):
        if pred in self.binary:
            self.binary[pred].append([e1,e2])
        else:
            self.binary[pred] = [[e1,e2]]

    def queryUnary(self,pred,e1):
        for key in self.unary:
            if (key == pred):
                if e1 in self.unary[key]:
                    return True
        return False

    def queryBinary(self,pred,e1,e2):
        for key in self.binary:
            if (key == pred):
                for exp in self.binary[key]:
                    if (e1 in exp) and (e2 in exp):
                        return True
        return False


import re
from nltk.corpus import brown
def verb_stem(s):
    """extracts the stem from the 3sg form of a verb, or returns empty string"""
    #stem is have
    #see notepad for flow chart


def add_proper_name (w,lx):
    """adds a name to a lexicon, checking if first letter is uppercase"""
    if ('A' <= w[0] and w[0] <= 'Z'):
        lx.add(w,'P')
        return ''
    else:
        return (w + " isn't a proper name")

def process_statement (lx,wlist,fb):
    """analyses a statement and updates lexicon and fact base accordingly;
       returns '' if successful, or error message if not."""
    # Grammar for the statement language is:
    #   S  -> P is AR Ns | P is A | P Is | P Ts P
    #   AR -> a | an
    # We parse this in an ad hoc way.
    msg = add_proper_name (wlist[0],lx)
    if (msg == ''):
        if (wlist[1] == 'is'):
            if (wlist[2] in ['a','an']):
                lx.add (wlist[3],'N')
                fb.addUnary ('N_'+wlist[3],wlist[0])
            else:
                lx.add (wlist[2],'A')
                fb.addUnary ('A_'+wlist[2],wlist[0])
        else:
            stem = verb_stem(wlist[1])
            if (len(wlist) == 2):
                lx.add (stem,'I')
                fb.addUnary ('I_'+stem,wlist[0])
            else:
                msg = add_proper_name (wlist[2],lx)
                if (msg == ''):
                    lx.add (stem,'T')
                    fb.addBinary ('T_'+stem,wlist[0],wlist[2])
    return msg

lx = Lexicon()
lx.add("John","N")
lx.add("Shelia","N")
lx.add("John","T")
fb = FactBase()
fb.addUnary("duck","John")
fb.addBinary("love","John","Mary")
fb.addBinary("love","John","Mildrid")
print(fb.queryUnary("duck","John"))
print(fb.queryBinary("love","Mildrid","John"))

# End of PART A.
