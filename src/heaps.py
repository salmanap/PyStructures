from string import split
import sys
from numpy.lib.scimath import log2
import math

'''
This method creates a heap from an integer array passed to it and accepts
a closure that will determine if the heap should be structured
in  a Max or Min fashion 
''' 
def __createHeap(someArray, shouldSwapHeapKeys):
    heapArray = []  
    for heapKey in someArray:
        insert(heapArray, int(heapKey), shouldSwapHeapKeys) 
    return heapArray;

def insert(heapArray, heapKey, shouldSwapHeapKeys):
    heapArray.append(heapKey)
    index_of_heap_key = heapArray.index(heapKey)
    parent_index_of_heap_key = (index_of_heap_key-1)/2
    while index_of_heap_key>0:
        if(shouldSwapHeapKeys(heapKey, heapArray[parent_index_of_heap_key])):
            __swap(index_of_heap_key, parent_index_of_heap_key, heapArray)
            index_of_heap_key = parent_index_of_heap_key;
            parent_index_of_heap_key = (index_of_heap_key-1)/2
        else:
            break # we have reached the right spot

def createMaxHeap(someArray):
    return __createHeap(someArray, lambda x,y: x > y)

def createMinHeap(someArray):
    return __createHeap(someArray, lambda x,y: x < y)

def __swap(swapFromIndex, swapToIndex, heapArray):
    middle_man = heapArray[swapToIndex]
    heapArray[swapToIndex] = heapArray[swapFromIndex]
    heapArray[swapFromIndex] = middle_man
    
def printHeapToConsole(someHeap):
    levels = int(log2(len(someHeap))) + 1
    spaceForlevel = math.pow(levels, 2) * 3
    heapKeyPos = 0
    level = 1
    levelBuffer = ''
    for heapKey in someHeap:
        heapKeyPos +=1
        if(int(log2(heapKeyPos)) + 1 > level):
            print levelBuffer + '\n'; level +=1 ; levelBuffer ='' ; 
            spaceForlevel = int(spaceForlevel/2);
        heapKeyStr = str(heapKey)
        leftSpacer = ' ' * int(spaceForlevel/2)
        rightSpacer = ' ' * (int(spaceForlevel/2) - len(heapKeyStr))
        levelBuffer += leftSpacer + heapKeyStr + rightSpacer
    
    if len(levelBuffer) > 0:
        print levelBuffer + '\n'

if __name__ == '__main__':
    someArray = split(sys.argv[1], ",")
    print "Let's heapify this array, how about Max and Min ?"
    print someArray 
    print '\n'
        
    print 'Min Heap Representation: ' 
    printHeapToConsole(createMinHeap(someArray))
    
    print 'Max Heap Representation: ' 
    printHeapToConsole(createMaxHeap(someArray))
    
    