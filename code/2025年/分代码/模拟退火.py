# coding=utf-8
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
import math
import time
import random

# 定义TSP结点坐标
x = [4350,4500,4300,4300,4300,4300,4350,4500,4300,4300,4300,4300,4950,5150,5525,5525,5525,5525,4950,5250,5550,4950,5150,5525,5525,5525,5525,4950,5250,5550,5875,5875,5875,5875,5675,5675,5875,5875,5875,5875,5675,5675,8125,8225,8325,8125,8225,8325,8675,8675,8675,8675,8675,8675,8675,8675,8675,8675,8425,8525,8675,8675,8675,8675,8675,8675,8675,8675,8675,8675,8425,8525,10850,10850,10850,10850,10900,11050,10850,10850,10850,10850,10900,11050,11500,11800,11500,11700,11500,11800,11500,11700,12075,12075,12225,12225,12075,12075,12100,12425,12425,12425,12425,12075,12075,12225,12225,12075,12075,12100,12425,12425,12425,12425,14675,14675,14775,14875,14975,15075,15225,15225,15225,15225,15225,15225,15225,15225,15225,15225,14775,14875,14975,15075,15225,15225,15225,15225,15225,15225,15225,15225,15225,15225]

y = [4425,4425,4725,4825,4950,5050,8875,8875,9175,9275,9400,9500,10600,10600,9525,9425,9225,9125,8875,8875,8875,6150,6150,5075,4975,4775,4675,4425,4425,4425,2325,2475,2625,2775,4825,4925,6775,6925,7075,7225,9275,9375,10150,10150,10150,5700,5700,5700,3150,3250,3350,3450,3550,3650,3750,3850,3950,4050,5700,5700,7600,7700,7800,7900,8000,8100,8200,8300,8400,8500,10150,10150,9500,9400,9275,9175,8875,8875,5050,4950,4825,4725,4425,4425,4425,4425,6150,6150,8875,8875,10600,10600,9525,9425,9375,9275,9225,9125,8875,7225,7075,6925,6775,5075,4975,4925,4825,4775,4675,4425,2775,2625,2475,2325,5700,10150,10150,10150,10150,10150,8500,8400,8300,8200,8100,8000,7900,7800,7700,7600,5700,5700,5700,5700,4050,3950,3850,3750,3650,3550,3450,3350,3250,3150]

n = len(x)  # 定义城市数n
bestway = [i for i in range(n)]  # 保存最优路径，初始最优路径为默认顺序
dis_array = [[0 for i in range(n)] for i in range(n)]  # 距离矩阵，保存每两个城市之间的距离


# 绘图显示最优路径
def draw_bestway():
    best_x = []
    best_y = []
    # 从bestway中建立坐标序列
    for i in range(n):
        p = bestway[i]
        best_x.append(x[p])
        best_y.append(y[p])
    # 加入开始点坐标，形成环路
    best_x.append(best_x[0])
    best_y.append(best_y[0])
    # 利用plt函数绘图
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.title("TSP求解 2310011043 仓正良")
    plt.plot(best_x, best_y, color='green', linestyle='-', marker='o', markerfacecolor='red')
    plt.show()


# 计算最优路径分值
def comp_bestway_score():
    best_x = []
    best_y = []
    # 从bestway中建立坐标序列
    for i in range(n):
        p = bestway[i]
        best_x.append(x[p])
        best_y.append(y[p])
    value = 0.0
    for i in range(1, n):
        x2 = (best_x[i] - best_x[i - 1]) * (best_x[i] - best_x[i - 1])
        y2 = (best_y[i] - best_y[i - 1]) * (best_y[i] - best_y[i - 1])
        value = value + math.sqrt(x2 + y2)
    x2 = (best_x[0] - best_x[n - 1]) * (best_x[0] - best_x[n - 1])
    y2 = (best_y[0] - best_y[n - 1]) * (best_y[0] - best_y[n - 1])
    value = value + math.sqrt(x2 + y2)
    return (value)


#模拟退火，利用温度控制逐步减少接受差解的概率，最终达到局部最优
def sa():
    t = 100    #设置初始温度
    tf = 0.01  #设置终止温度
    kb = 0.8   #设置降温系数
    f1 = comp_bestway_score()    #f1保存当前解分值
    obway = [0] * n   #保存当前全局最优解
    for i in range(n):
        obway[i] = bestway[i]
    obscore = f1    #obscore保存全局最优分值
    while t > tf:
        for iter in range(200):  #等温过程
            v1 = random.randint(0,n-1)
            v2 = random.randint(0,n-1)
            if(v1 != v2):
                bestway[v1],bestway[v2]=bestway[v2],bestway[v1]
                f2 = comp_bestway_score() #f2保存候选解分值
                if(f2 < obscore):
                    obscore = f2
                    for i in range(n):
                        obway[i] = bestway[i]
                delta = f2 - f1 #计算候选解与当前解之间的差值
                if(delta < 0):
                    f1 = f2
                else:
                    alpha = random.random()
                    if(math.exp( - delta / t ) > alpha):
                        f1 = f2
                    else:
                        bestway[v2], bestway[v1] = bestway[v1], bestway[v2]
        t = kb * t  #降温
    #将最终获取到的最优路径更新至bestway
    for i in range(n):
        bestway[i] = obway[i]



def run():
    print("模拟退火算法:")
    time_start = time.time()
    bestway = [i for i in range(n)]  # 设置默认初始解
    sa()
    time_end = time.time()
    print("bestway:", bestway)
    print("score: ", comp_bestway_score())
    print("totally time:", time_end - time_start)
    # draw_bestway()

#主程序
# print("nSa:")
# time_start=time.time()
# bestway = [i for i in range(n)]  # 设置默认初始解
# sa()
# time_end=time.time()
# print("bestway:",bestway)
# print("score: ",comp_bestway_score())
# print("totally time:",time_end - time_start)
# draw_bestway()