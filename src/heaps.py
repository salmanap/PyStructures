from string import split
import sys, trees
 
def __createHeap(someArray, shouldSwapHeapKeys):
    heapArray = []  
    for heapKey in someArray:
        insert(heapArray, int(heapKey), shouldSwapHeapKeys) 
    return heapArray;

def insert(heapArray, heapKey, shouldSwapHeapKeys):
    heapArray.append(heapKey)
    index_of_heap_key = len(heapArray)-1
    parent_index_of_heap_key = (index_of_heap_key-1)/2
    while index_of_heap_key>0:
        if(shouldSwapHeapKeys(heapKey, heapArray[parent_index_of_heap_key])):
            __swap(index_of_heap_key, parent_index_of_heap_key, heapArray)
            index_of_heap_key = parent_index_of_heap_key;
            parent_index_of_heap_key = (index_of_heap_key-1)/2
        else:
            break # we have reached the right spot

def removeTopElementAndRearrangeHeap(heapArray, shouldSwapHeapKeys):
    top_element = heapArray[0]
    if(len(heapArray) > 0):
        element_to_insert = heapArray.pop()
        heapArray[0] = element_to_insert
        index_of_element_to_insert = 0
        while True:
            right_child_index = index_of_element_to_insert*2+2
            child_index_with_priority = left_child_index = index_of_element_to_insert*2+1
            if right_child_index < len(heapArray):
                if (shouldSwapHeapKeys(heapArray[right_child_index], 
                                                heapArray[left_child_index])):
                    child_index_with_priority = right_child_index
            elif left_child_index >= len(heapArray):
                break
            
            if(shouldSwapHeapKeys(heapArray[child_index_with_priority], 
                            heapArray[index_of_element_to_insert])):
                __swap(index_of_element_to_insert, child_index_with_priority, heapArray)
                index_of_element_to_insert = child_index_with_priority
            else:
                break
                    
    return top_element

def __minHeapKeyComparisonLambda():
    return lambda x,y: x < y

def __maxHeapKeyComparisonLambda():
    return lambda x,y: x > y

def __swap(swapFromIndex, swapToIndex, heapArray):
    middle_man = heapArray[swapToIndex]
    heapArray[swapToIndex] = heapArray[swapFromIndex]
    heapArray[swapFromIndex] = middle_man

"""
Returns a MinHeap representation of the array, where the array elements
should be comparable, i.e. should implement the means to have a logical 
comparison done 
"""
def createMinHeap(someArray):
    return __createHeap(someArray, __minHeapKeyComparisonLambda())

"""
Returns a MaxHeap representation of the array, where the array elements
should be comparable, i.e. should implement the means to have a logical 
comparison done 
"""
def createMaxHeap(someArray):
    return __createHeap(someArray, __maxHeapKeyComparisonLambda())

if __name__ == '__main__':
    someArray = split(sys.argv[1], ",")
    print "Creating a max and min heap representation of the following array"
    print someArray 
    print '\n'
        
    print 'Min Heap Representation: '
    min_heap = createMinHeap(someArray) 
    trees.printTreeToConsole(min_heap)
    
    print 'Max Heap Representation: ' 
    max_heap = createMaxHeap(someArray)
    trees.printTreeToConsole(max_heap)
    

    
    