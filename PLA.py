import numpy as np
import random

def GetData(x0 , scaledown ):  #從資料集抽取出data,並加入x0或將其scale down
    with open('hw1_train.dat','r') as file :
        data = []
        lines = file.readlines()
        N = len(lines)
        for i in lines:
            i = i.strip().split()
            temp = np.zeros(12)
            for j in range(12):
                if j == 0 :
                    temp[j] = x0
                elif j == 11:
                    temp[j] = np.float(i[j-1])
                else:
                    temp[j] = np.float(i[j-1])/scaledown
            data.append(temp)
        return N , data           #返回資料筆數及 data 向量

def sign(w , x):  #判斷向量內積大於0或小於0
    if np.dot(w,data[x][:-1].T) >= 0:
        return 1
    else:
        return -1 

def PLA( data , N , w  ):  #運行PLA,隨機抽取資料,若抽取資料滿足連續 5N 次與 w 向量內積謀合, 則跳出迴圈,得所求model
    count0 = 0             #若內積與結果不符,則做修正
    count1 = 0
    while 1:
        x = random.randint(0,N-1)
        if sign(w,x) != data[x][-1]:
            w = w + data[x][0:-1]*data[x][-1]
            count0 = 0
            count1 += 1
        else:
            count0 += 1
            if count0 == 5*N:
                break
    return count1, w[0]

if __name__ == '__main__':
    N , data = GetData(x0 = 1, scaledown = 1)
    count_list = []
    w0 = []
    for i in range(1000):   #做1000次PLA將所得解取中位數
        random.seed(i)
        w = np.zeros(11)
        count , w_0= PLA(data, N, w)
        count_list.append(count)
        w0.append(w_0)
    count_list.sort()
    print("number of updates:",(count_list[500]+count_list[501])//2, ",w0 =",(w0[500]+w0[501])//2)

        
        





