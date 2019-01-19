import unittest
import src.CInput

class Test_Entry(unittest.TestCase):
    ''' Python3 program to rotate an array by d elements '''
    # Function to left rotate arr[] of size n by d*/ 
    # Driver program to test above functions */ 
    # arr = array.array('B', [x for x in range(10)])
    arr = [1, 2, 3, 4, 5, 6, 7] 
    CInput.leftRotate(arr, 2, 7) 
    CInput.printArray(arr, 7) 