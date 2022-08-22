import math
from pickletools import uint8
from pprint import pprint
import numpy as np
import distribution as dst
import random
region_driver = [[0 for col in range(7)] for row in range(6)]

#print(region_driver)
region_weight = [[0 for col in range(7)] for row in range(6)]
region_x = 7
region_y = 6
weight=list()
zero=list()

#수정



def setdriver_region(driver,midRegion):
    min_x=7
    min_y=6
    region_driver = [[0 for col in range(7)] for row in range(6)]
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
    return region_driver



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

def detect_outside(region_driver,row,col):
    region_row_num = len(region_driver)
    region_col_num = len(region_driver[0])
    #up -> down -> right -> left
    output = list()
    result = list()

    if row > 0:
        if region_driver[row][col] !=  region_driver[row-1][col]:
            return 1

    if row < (region_row_num-1): 
        if region_driver[row][col] !=  region_driver[row+1][col]:
            return 1
          
    if col > 0:
        if region_driver[row][col] !=  region_driver[row][col-1]:
            return 1
      
    if col < (region_col_num-1):
        if region_driver[row][col] !=  region_driver[row][col+1]:
            return 1
       
    return 0

def detect_outside_driver(region_driver,row,col):
    region_row_num = len(region_driver)
    region_col_num = len(region_driver[0])
    #up -> down -> right -> left
    output = list()
    result = list()

    if row > 0:
        if region_driver[row][col] !=  region_driver[row-1][col]:
            output.append(region_driver[row-1][col])

    if row < (region_row_num-1): 
        if region_driver[row][col] !=  region_driver[row+1][col]:
            output.append(region_driver[row+1][col])
          
    if col > 0:
        if region_driver[row][col] !=  region_driver[row][col-1]:
            output.append(region_driver[row][col-1])
      
    if col < (region_col_num-1):
        if region_driver[row][col] !=  region_driver[row][col+1]:
            output.append(region_driver[row][col+1])

    #중복 제거        
    for value in output:
        if value not in result:
            result.append(value)
       
    return result

def detect_isolation_in2(region_driver,row,col):
    #up -> down -> right -> left
    #고립인 경우 1
    output = 0
    attach_num = 0
    region_row_num = len(region_driver)
    region_col_num = len(region_driver[0])


    if row > 0:
        if region_driver[row][col] ==  region_driver[row-1][col]:
                attach_num += 1

    if row < (region_row_num-1): 
        if region_driver[row][col] ==  region_driver[row+1][col]:
                attach_num += 1     

    if col > 0:
        if region_driver[row][col] ==  region_driver[row][col-1]:
                attach_num += 1       

    if col < (region_col_num-1):
        if region_driver[row][col] ==  region_driver[row][col+1]:
                attach_num += 1

    if attach_num < 2:
            output = 1
        
    return output

#고립 블록 탐지 알고리즘 - 1
def detect_isolation_in(region_driver,row,col,driver):
    #up -> down -> right -> left
    #고립인 경우 1
    output = 0
    attach_num = 0
    region_row_num = len(region_driver)
    region_col_num = len(region_driver[0])    
    if driver == region_driver[row][col]:

        if row > 0:
            if region_driver[row][col] ==  region_driver[row-1][col]:
                attach_num += 1

        if row < (region_row_num-1): 
            if region_driver[row][col] ==  region_driver[row+1][col]:
                attach_num += 1     

        if col > 0:
            if region_driver[row][col] ==  region_driver[row][col-1]:
                attach_num += 1       

        if col < (region_col_num-1):
            if region_driver[row][col] ==  region_driver[row][col+1]:
                attach_num += 1

        if attach_num < 2:
            output = 1
        
    return output

#고립 블록 탐지 알고리즘 - 2
def detect_isolation(region_driver,row,col):
    #up -> down -> right -> left
    #고립인 경우 1
    region_row_num = len(region_driver)
    region_col_num = len(region_driver[0])
    output = 0
    driver = region_driver[row][col]
    if row > 0:
        if detect_isolation_in(region_driver,row-1,col,driver) == 1:
            output = 1

    if row < (region_row_num-1): 
        if detect_isolation_in(region_driver,row+1,col,driver) == 1:
            output = 1  

    if col > 0:
        if detect_isolation_in(region_driver,row,col-1,driver) == 1:
            output = 1  

    if col < (region_col_num-1):
        if detect_isolation_in(region_driver,row,col+1,driver) == 1:
            output = 1
        
    return output

#운전자 = 권역) 별 난이도 합

def driver_difficulty_sum(region_driver,region_difficulty,driver_num):
    region_row_num = len(region_driver)
    region_col_num = len(region_driver[0])
    driver_difficulty = list()
    driver_difficulty = [0 for i in range(driver_num)]
    for row_num in range(0,region_row_num):
        for col_num in range(0,region_col_num):
            driver_difficulty[region_driver[row_num][col_num]-1]+= region_difficulty[row_num][col_num] 
    return driver_difficulty


def main_algorithm(region_difficulty,region_driver,driver_num,bounds):
    region_row_num = len(region_driver)
    region_col_num = len(region_driver[0])
    check = 0
    difficulty_sum = 0

    #오차 범위
    #bounds = 0.05
    for i in region_difficulty:
            for j in i:
                difficulty_sum += j

    average_difficulty = difficulty_sum / driver_num

    #print(average_difficulty)

    count = 0

    while check == 0:

        count +=1
        driver_check = 0

        for driver in range(1,driver_num+1):
            driver_difficulty = driver_difficulty_sum(region_driver,region_difficulty,driver_num)[driver -1]
            #print("driver : ",driver,"driver difficulty: ",driver_difficulty)

            driver_difficulty_check = driver_difficulty / average_difficulty
            driver_difficulty_difference = driver_difficulty - average_difficulty
            
            if driver_difficulty_check < (1 + bounds) and driver_difficulty_check > (1 - bounds):
                driver_check += 1

            elif driver_difficulty_check > 1:
                #외각 블록 확인
                driver_outside_block = list()
                outside_block_difficulty = list()
                for row_num in range(0,region_row_num):
                    for col_num in range(0,region_col_num):
                        if driver == region_driver[row_num][col_num] and detect_outside(region_driver,row_num,col_num) == 1: 

                            driver_outside_block.append([row_num,col_num])
                            outside_block_difficulty.append(abs(region_difficulty[row_num][col_num]-abs(average_difficulty-driver_difficulty_sum(region_driver,region_difficulty,driver_num)[driver -1])))
                            #min(|외곽 블록 - |난이도취합 - 평균|)

                check_block = 0

                while check_block == 0:
                    #1순위 퇴출 블록
                    #print(driver_outside_block)
                    #print(outside_block_difficulty)
                    for row_col in driver_outside_block:
                        abs_value = abs(region_difficulty[row_col[0]][row_col[1]]-abs(average_difficulty-driver_difficulty_sum(region_driver,region_difficulty,driver_num)[driver -1]))
                        #print(abs_value)
                        if min(outside_block_difficulty) == abs_value:

                            first_min_block_row = row_col[0]
                            first_min_block_col = row_col[1]
                            #print(driver,row_col[0],row_col[1])
    #                 print(driver_outside_block)
    #                 print(outside_block_difficulty)

                    #고립 블록이 있는 경우
                    isolation = detect_isolation(region_driver,first_min_block_row, first_min_block_col)

                    if isolation == 1:
                        #print("고립되는 블록 존재")
                        driver_outside_block.remove([first_min_block_row, first_min_block_col])
                        outside_block_difficulty.remove(min(outside_block_difficulty))

                        #print(driver_outside_block)
                        #print(outside_block_difficulty)
                        #1순위 가중치


                    #고립 블록이 없는 경우
                    elif isolation == 0:
                        candidate_min = 100000
                        for new_driver in detect_outside_driver(region_driver,first_min_block_row,first_min_block_col):
                            if driver_difficulty_sum(region_driver,region_difficulty,driver_num)[new_driver -1] < candidate_min:
                                candidate_min = driver_difficulty_sum(region_driver,region_difficulty,driver_num)[new_driver -1]
                                block_new_driver = new_driver
                        #print(first_min_block_row,first_min_block_col,"block",driver,">>>>>",block_new_driver)
                        region_driver[first_min_block_row][first_min_block_col] = block_new_driver
                    check_block = 1
                    
            #1        
            elif driver_difficulty_check < 1:
                outside_another_driver_block = list()
                isolation_check = 1
                isol_num = 0
                isol_check_num = 0
                for row_num in range(0,region_row_num):
                    for col_num in range(0,region_col_num):   
                            #print(region_driver[row_num][col_num])
                        if detect_outside_driver(region_driver,row_num, col_num) == [driver]:                        
                            outside_another_driver_block.append([row_num,col_num])
                length =  len(outside_another_driver_block)           

                input_block = outside_another_driver_block[random.randint(0,length-1)]
                origin_driver = region_driver[input_block[0]][input_block[1]]
                region_driver[input_block[0]][input_block[1]] = driver
                    #고립이면 리턴

                if detect_isolation_in2(region_driver,input_block[0],input_block[1]) == 1:   
                    region_driver[input_block[0]][input_block[1]] = origin_driver

            if driver_check == 4:
                check = 1     
        if count > 10:
            return region_driver
    return region_driver

def set_driver_region(shape,midregion):
    driver_region = [[0 for i in range(shape[1])] for j in range(shape[0])]
    driver_num = 1
    for cord in midregion:
        driver_region[cord[0]][cord[1]] = driver_num
        driver_num+=1 

    for y in range(0,shape[1]):
        for x in range(0,shape[0]):
            dist_array = list()
            for cord in midregion:
                dist_array.append(pow((x-cord[0]),2) + pow((y-cord[1]),2))
            driver_region[x][y] = dist_array.index(min(dist_array))+1

    print(driver_region)

    return driver_region

if __name__ == '__main__':
    print("distribution code")
    tst_regionList = dst.getRegion()
    #tst_regionList = dst.getRegion_test(20)
    driver=3


    midRegion = dst.setMidRegion(driver,tst_regionList.shape)
    #print(midRegion)
    #pprint(tst_regionList)

    #print(midRegion)
    pprint(tst_regionList)
    #pprint(midRegion)
    region_driver = set_driver_region(tst_regionList.shape,midRegion)
    #pprint(region_driver)

    final_result = main_algorithm(tst_regionList, region_driver, driver, 0.05)


    for i in final_result :
        for j in i:
            print(j,end=" | ")
        print()
        print("------------------------------")

    for i in range(0,driver): 
        diff = driver_difficulty_sum(region_driver,tst_regionList,driver)[i]
        print(i+1,"driver = ", diff)
    
    #print(setdriver_region(driver,midRegion))
    #finddriver_weight(driver,tst_regionList)
    #print(weight)
    #change_region(1,2,4,3)
    #print(tst_regionList[3][4])
    #pprint(region_driver)
    #print(weight)
    #print(len(midRegion))