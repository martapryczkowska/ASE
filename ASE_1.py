import random
import numpy as np
from timeit import default_timer as timer

randomNumber=[]
liczbaElementow=5000
for i in range(liczbaElementow):
    randomNumber.append(random.randint(0,100000))

randomNumber2=randomNumber.copy()
randomNumber3=randomNumber.copy()


sorted=True
def babelkowy(sorted, liczbaElementow):
    while(sorted):
        sorted=False
        for i in range(1,liczbaElementow):
         if(randomNumber[liczbaElementow-i]<randomNumber[liczbaElementow-i-1]):
            buffer=randomNumber[liczbaElementow-i]
            randomNumber[liczbaElementow-i]=randomNumber[liczbaElementow-i-1]
            randomNumber[liczbaElementow-i-1]=buffer
            sorted=True

start1 = timer()
babelkowy(True, liczbaElementow)
end1 = timer()
print ("Sortowanie bąbelkowe"  +str (randomNumber))
print("czas = " + str(end1-start1) )


def selection(index,x,randomNumer2):
    for j in range(0,liczbaElementow):
        smallest=randomNumber2[-1]
        index_small = len(randomNumber2)-1
        for i in range(index,liczbaElementow):
            if (randomNumber2[i]<smallest):
                smallest=randomNumber2[i]
                index_small=i
        index=index+1
        buffer=randomNumber2[j]
        randomNumber2[j]=randomNumber2[index_small]
        randomNumber2[index_small]=buffer

start2=timer()
selection(0,0,randomNumber2)
end2=timer()

print ("Selection sort"  +str (randomNumber2))
print("czas = " + str(end2-start2) )

def quicksort(start_pos, end_pos):
    if end_pos>start_pos:
        pIndex=partition(start_pos, end_pos)
        quicksort(start_pos, pIndex-1)
        quicksort(pIndex+1, end_pos)


def partition(start_pos, end_pos):
    elem=randomNumber3[end_pos]
    pIndex=start_pos
    for i in range(start_pos, end_pos):
        if randomNumber3[i]<=elem:
            buffer = randomNumber3[i]
            randomNumber3[i] = randomNumber3[pIndex]
            randomNumber3[pIndex] = buffer
            pIndex=pIndex+1
    buffer = randomNumber3[pIndex]
    randomNumber3[pIndex] = randomNumber3[end_pos]
    randomNumber3[end_pos] = buffer
    return pIndex

start3=timer()
quicksort(0, len(randomNumber3)-1)
end3=timer()

print ("Quick sort"  +str (randomNumber2))
print("czas = " + str(end3-start3) )