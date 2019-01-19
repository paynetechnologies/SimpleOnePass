
import time
import random
import array
'''
for n in (100000, 200000, 300000, 400000):
    data = 'x'*n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print(f'bytes {n} {time.time()-start}')

for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print(f'memoryview {n} {time.time()-start}')
'''

#for n in (100000, 200000, 300000, 400000):
    # rand = array.array('B', [random.randint(1,100) for _ in range (10)])
    # start = time.time()
    # b = memoryview(rand)
    # while b:
    #     b = b[1:]
    # print(f'random memoryview {1000000} {time.time()-start}')

    #InputBuf = array.array('B', [126 for x in range(BUFSIZE)]) 

# array
# data1 = array.array('B', [random.randint(1,100) for _ in range (10)])
# b = data1
# while b:
#     b = b[1:]

MAXLOOK = 16                               # max amount of lookahead
MAXLEX  = 1024                             # max lexeme size
BUFSIZE = (MAXLEX * 3) + (2 * MAXLOOK)     # Change the 3 only
END = BUFSIZE                              # just past last char in buf

# Input Buffer
#InputBuf = array.array('B', [random.randint(1,100) for _ in range (BUFSIZE)]) 
InputBuf = array.array('h', [i for i in range (BUFSIZE)]) 
#InputBuf = array.array('h', [i for i in range (20)]) 
arr2 = array.array('h', [i for i in range (100, 120)]) 


def sliceit():
    # memoryview
    data2 = array.array('B', [random.randint(1,100) for _ in range (10)])
    b = memoryview(data2)
    b2 = array.array('B', b)
    #while b2:
    b2 = b2[2:]
    b3 = memoryview(b2)
    print('b3')


def rotate(arr, d, n):
    start = time.time()
    return arr[d:] + arr[:d] 
    #print(f'leftRotate {time.time()-start}')

def right_rotation(a, k):
    # if the size of k > len(a), rotate only necessary with
    # module of the division
    rotations = k % len(a)
    return a[-rotations:] + a[:-rotations]

def left_rotation(a, k):
    # if the size of k > len(a), rotate only necessary with
    # module of the division
    rotations = k % len(a)
    return a[rotations:] + a[:rotations]

def main():
    a = right_rotation(InputBuf, 2)
    b = left_rotation(InputBuf, 4)
    c = left_rotation(InputBuf, 3081)
    d = rotate(InputBuf, 3081, BUFSIZE)
    print ('done')

    #leftRotate(InputBuf, 3103, BUFSIZE)
    #mv = memoryview(InputBuf)
    #leftRotate(mv, 3103, BUFSIZE)

def leftRotate(arr, d, n): 
    start = time.time()
    for _ in range(d): 
        leftRotatebyOne(arr, n) 
    print(f'leftRotate {time.time()-start}')

# Function to left Rotate arr[] of size n by 1*/  
def leftRotatebyOne(arr, n): 
    temp = 32
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 

if __name__ == '__main__':
    main()
    print('done')
