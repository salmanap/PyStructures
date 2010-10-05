'''
Created on Oct 3, 2010

@author: salman
'''
from numpy.lib.scimath import log2
import math

def printTreeToConsole(tree):
    levels = int(log2(len(tree)))
    space_for_elements = math.pow(2, levels) * 3
    heapKeyPos = 1; level = 0; levelBuffer = ''
    for heapKey in tree:
        if(int(log2(heapKeyPos)) > level):
            print levelBuffer + '\n' ; level +=1 ; levelBuffer ='' ;
            
        heapKeyStr = str(heapKey)
        if heapKey is None:
            heapKeyStr = "x"
            
        space_for_element = int((space_for_elements/(math.pow(2, level))))
        right_spacer = left_spacer = ' ' * ((space_for_element-len(heapKeyStr))/2)
        
        if (space_for_element-len(heapKeyStr)) % 2 == 1:   
            right_spacer += ' '
                
        levelBuffer += (left_spacer + heapKeyStr + right_spacer)
        heapKeyPos +=1
    
    if len(levelBuffer) > 0:
        print levelBuffer + '\n'