import math
from pprint import pprint
import numpy as np
import distribution as dst
region_driver = [[0 for col in range(7)] for row in range(6)]
#print(region_driver)
region_weight = [[0 for col in range(7)] for row in range(6)]
region_x = 7
region_y = 6
weight=list()
zero=list()
def setdriver_region(driver,midRegion):
    min_x=7
    min_y=6
    for i in range(driver):
        region_driver[int(midRegion[i][0])][int(midRegion[i][1])]=i+1
        if min_x>midRegion[i][0]:
            min_x=midRegion[i][0]
        if min_y>midRegion[i][0]:
            min_y=midRegion[i][0]
    #pprint(region_driver)
    for i in range(driver):
         #print(midRegion[i])
         for y in range(3):
             for x in range(3):
                 if check(midRegion[i][1]+x-1,midRegion[i][0]+y-1):
                    if(region_driver[midRegion[i][0]+y-1][midRegion[i][1]+x-1]==0):
                        region_driver[midRegion[i][0] + y - 1][midRegion[i][1] + x - 1]=i+1
    #pprint(region_driver)
    for i in range(region_y):
        for j in range(region_x):
            #print(i,j)
            if(region_driver[i][j]==0):
                #print(i,j)
                region_driver[i][j]=findclose_region(i,j,region_x,region_y)
    #pprint(region_driver)    #나눠진 권역


def check(x,y):
    if(x>=0 and x<region_x):
        if(y>=0 and y<region_y):
            return True
        else:
            return False
    else:
        return False
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
    else:
        if(region_driver[i][j-1]!=0):
            return region_driver[i][j-1]
        elif(region_driver[i-1][j]!=0):
            return region_driver[i-1][j]

def finddriver_weight(driver, tst_regionList):   #초기에 운전자별 가중치 총 합 weight 리스트에 넣음
    for i in range(driver):
        wd = 0
        for y in range(region_y):
            for x in range(region_x):
                if(region_driver[y][x]==i+1):
                    wd+=tst_regionList[y][x]
        weight.append(wd)


def change_region(new_driver,before_driver,target_x,target_y):
    region_driver[target_y][target_x]=new_driver
    we=tst_regionList[target_y][target_x]
    weight[before_driver-1]= weight[before_driver-1]-we
    weight[new_driver-1]=weight[new_driver-1]+we


if __name__ == '__main__':
    print("distribution code")
    tst_regionList = dst.getRegion_test(100)
    driver=5
    midRegion = dst.setMidRegion(5,tst_regionList.shape)
    pprint(tst_regionList)
    d1 = [int(midRegion[0][0]), int(midRegion[0][1])]
    d2 = [int(midRegion[1][0]), int(midRegion[1][1])]
    d3 = [int(midRegion[2][0]), int(midRegion[2][1])]
    d4 = [int(midRegion[3][0]), int(midRegion[3][1])]
    #print(midRegion)
    #pprint(tst_regionList)
    #pprint(midRegion)
    setdriver_region(driver,midRegion)
    pprint(region_driver)
    finddriver_weight(driver,tst_regionList)
    print(weight)
    #change_region(1,2,4,3)
    #print(tst_regionList[3][4])
    #pprint(region_driver)
    #print(weight)
    #print(len(midRegion))