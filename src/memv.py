
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

#for n in (100000, 200000): #, 300000, 400000):
#for i in range(n):
rand = array.array('B', [random.randint(1,100) for _ in range (10)])
start = time.time()
b = memoryview(rand)
#b = rand
while b:
    b = b[1:]
print(f'random memoryview {1000000} {time.time()-start}')

    #InputBuf = array.array('B', [126 for x in range(BUFSIZE)]) 