import math

import numpy as np

def getRegion(shape,weight): #weight format : (x_cord,y_cord,weight)
    regionList = np.array()
    return regionList

def getRegion_test(max_weight):
    tst_regionList = np.random.rand(14,10) * max_weight

    return tst_regionList

def setMidRegion(driverNum,shape):
    if driverNum> min(shape):
        print("wrong driver number")
        midRegion = list()
    else:
        maxDispose = (math.ceil(driverNum**(1/2)))
        if driverNum%maxDispose==0:
            minDispose = driverNum/maxDispose
        else:
            minDispose = math.trunc(driverNum**(1/2))
        maxInterval = max(shape)//maxDispose
        minInterval = min(shape)//minDispose

        maxIndex = shape.index(max(shape))
        maxCord = list()
        minDisposeMinCord = list()
        maxDisposeMinCord = list()

        for i in range(maxDispose):
            maxCord.append(maxInterval//2 + maxInterval*(i))
        for i in range(maxDispose):
            maxDisposeMinCord.append((min(shape)//maxDispose)//2 + (min(shape)//maxDispose)*(i))
        for i in range(int(minDispose)):
            minDisposeMinCord.append(minInterval//2 + minInterval*(i))

        maxDisposeNum = driverNum%maxDispose

        midRegion = list()
        count = 0
        if maxIndex==0:
            for i in range(maxDisposeNum):
                for j in range(maxDispose):
                    midRegion.append((maxCord[i],maxDisposeMinCord[j]))
            for i in range(maxDispose-maxDisposeNum):
                for j in range(minDispose):
                    midRegion.append((maxCord[maxDispose-i-1],minDisposeMinCord[j]))
        else:
            print("max index is y")

    return midRegion

if __name__ == '__main__':
    print("distribution code")
    tst_regionList = getRegion_test(100)
    midRegion = setMidRegion(8,tst_regionList.shape)
    print(midRegion)
    print(len(midRegion))