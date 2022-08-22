import math
from pprint import pprint
import numpy as np
region_driver = [[0 for col in range(7)] for row in range(6)]
#print(region_driver)
region_weight = [[0 for col in range(7)] for row in range(6)]
region_x = 7
region_y = 6
weight=list()
def getRegion(shape,weight): #weight format : (x_cord,y_cord,weight)
    regionList = np.array()
    return regionList

def getRegion_test(max_weight):
    tst_regionList = np.random.rand(7,6) * max_weight
    #print(tst_regionList)
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
                    midRegion.append((maxCord[i],int(maxDisposeMinCord[j])))
            for i in range(maxDispose-maxDisposeNum):
                for j in range(int(minDispose)):
                    midRegion.append((maxCord[maxDispose-i-1],int(minDisposeMinCord[j])))
        else:
            print("max index is y")

    return midRegion

def setdriver_region(driver,midRegion):
    min_x=7
    min_y=6
    for i in range(driver):
        region_driver[int(midRegion[i][0])][int(midRegion[i][1])]=i+1
        if min_x>midRegion[i][0]:
            min_x=midRegion[i][0]
        if min_y>midRegion[i][0]:
            min_y=midRegion[i][0]
    pprint(region_driver)
    r=min(min_x,min_y)*2
    for i in range(driver):
        #print(midRegion[i])
        for x in range(r+1):
            for y in range(r+1):
                if(region_driver[midRegion[i][0]+x-int(r/2)][midRegion[i][1]+y-int(r/2)]==0):
                    region_driver[midRegion[i][0] + x - int(r/2)][midRegion[i][1] + y - int(r/2)]=i+1
    pprint(region_driver)
    for i in range(region_y):
        for j in range(region_x):
            #print(i,j)
            if(region_driver[i][j]==0):
                #print(i,j)
                region_driver[i][j]=findclose_region(i,j,region_x,region_y)
    pprint(region_driver)    #나눠진 권역

def findclose_region(i,j,region_x,region_y):
    if((i+1)>=region_y and region_driver[i-1][j]!=0):
        #print(i,j)
        return region_driver[i-1][j]
    elif ((j-1)<0 and region_driver[i][j+1]!=0):
        #print(i, j)
        return region_driver[i][j+1]
    elif ((j+1)>=region_x and region_driver[i][j-1]!=0):
        #print(i, j)
        return region_driver[i][j-1]
    elif ((i-1)<0 and region_driver[i+1][j]!=0):
        #print(i, j)
        return region_driver[i+1][j]

def finddriver_weight(driver, tst_regionList):   #초기에 운전자별 가중치 총 합 weight 리스트에 넣음
    a_weight = 0
    b_weight = 0
    c_weight = 0
    d_weight = 0
    for y in range(region_y):
        for x in range(region_x):
            #print(y,x)
            if(region_driver[y][x]==1):
                a_weight += tst_regionList[y][x]
            if (region_driver[y][x] == 2):
                b_weight+=tst_regionList[y][x]
            if (region_driver[y][x] == 3):
                c_weight+=tst_regionList[y][x]
            if(region_driver[y][x]==4):
                d_weight+=tst_regionList[y][x]
    weight.extend([a_weight,b_weight,c_weight,d_weight])

def change_region(new_driver,before_driver,target_x,target_y):
    region_driver[target_y][target_x]=new_driver
    we=tst_regionList[target_y][target_x]
    weight[before_driver-1]= weight[before_driver-1]-we
    weight[new_driver-1]=weight[new_driver-1]+we


if __name__ == '__main__':
    print("distribution code")
    tst_regionList = getRegion_test(100)
    driver=5
    midRegion = setMidRegion(5,tst_regionList.shape)
    d1 = [int(midRegion[0][0]), int(midRegion[0][1])]
    d2 = [int(midRegion[1][0]), int(midRegion[1][1])]
    d3 = [int(midRegion[2][0]), int(midRegion[2][1])]
    d4 = [int(midRegion[3][0]), int(midRegion[3][1])]
    #print(midRegion)
    #pprint(tst_regionList)
    #pprint(midRegion)
    setdriver_region(driver,midRegion)
    finddriver_weight(driver,tst_regionList)
    print(weight)
    change_region(1,2,4,7)
    print(tst_regionList[7][4])
    pprint(region_driver)
    print(weight)
    print(len(midRegion))