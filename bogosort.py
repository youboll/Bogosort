from random import shuffle,randint
import time
t1 = time.time()
def bogosort(seq):
    while not all(x <= y for x, y in zip(seq, seq[1:])):
        
        x = randint(0,(len(seq) - 2))
        if (seq[x] > seq[x + 1]):
            temp = seq[x]
            seq[x] = seq[x + 1]
            seq[x + 1] = temp 
    return seq
def randomize(size,m):
    if (type(size) != type(int())): return(False)
    rand = []
    while (size > 0):
        rand.append(randint(0,m))
        size -=1
    return(rand)
x = bogosort(randomize(550,100000))
t2 = time.time()
print(x)
print("time",t1-t2)
