import math
import dst_search as sch
import numpy as np

def getRegion(): #weight format : (x_cord,y_cord,weight)
    conn = sch.db_connect()
    sql = "select * from region_difficulty_sum"
    cursor = conn.cursor(buffered=True)
    cursor.execute(sql)
    res_list = cursor.fetchall()
    #print(int(res_list[-1][0]),int(res_list[-1][1]))
    regionList = np.ndarray((int(res_list[-1][0]),int(res_list[-1][1])))
    for res in res_list:
        regionList[res[0]-1][res[1]-1] = res[2]
    #print(regionList)
    return regionList

def getRegion_test(max_weight):
    tst_regionList = np.random.rand(11,12) * max_weight

    return tst_regionList

def setMidRegion(driverNum,shape):
    if driverNum> min(shape):
        print("wrong driver number")
        midRegion = list()
    else:
        maxDispose = (math.ceil(driverNum**(1/2)))
        if driverNum%maxDispose==0:
            minDispose = int(driverNum/maxDispose)
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

        maxDisposeNum = driverNum%minDispose
        if(minDispose==1):
            maxDisposeNum=driverNum%maxDispose
        midRegion = list()
        count = 0
        if maxIndex==0:
            for i in range(maxDisposeNum):
                for j in range(maxDispose):
                    midRegion.append((maxCord[i],maxDisposeMinCord[j]))
            if minDispose == 1:
                midRegion.append((maxCord[-1], minDisposeMinCord[-1]))
            else:
                for i in range(math.trunc(driverNum//minDispose)-maxDisposeNum):
                    for j in range(minDispose):
                        midRegion.append((maxCord[maxDispose-i-1],minDisposeMinCord[j]))

        else:
            #print("max index is y")
            for i in range(maxDisposeNum):
                for j in range(maxDispose):
                    midRegion.append((maxDisposeMinCord[j],maxCord[i]))
            if minDispose == 1:
                midRegion.append((minDisposeMinCord[-1],maxCord[-1]))
            else:
                for i in range(math.trunc(driverNum//minDispose)-maxDisposeNum):
                    for j in range(minDispose):
                        midRegion.append((minDisposeMinCord[j],maxCord[maxDispose-i-1]))

    return midRegion

if __name__ == '__main__':
    print("distribution code")
    tst_regionList = getRegion_test(100)
    regionList = getRegion()
    midRegion = setMidRegion(11,tst_regionList.shape)
    print(midRegion)
    print(len(midRegion))