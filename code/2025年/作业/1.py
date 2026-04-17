#coding=utf-8
import matplotlib
matplotlib.use('TkAgg')  # 切换到TkAgg后端
import matplotlib.pyplot as plt
#coding=utf-8
import matplotlib.pyplot as plt
import math
import time
import random

#定义TSP结点坐标
x = [16,16,20,22,25,22,20,17,16,17,16,21,19,20]
y = [96,94,92,93,97,96,97,96,98,98,97,95,97,94]

n = len(x)  #定义城市数
bestway = [i for i in range(n)] #保存最优路径，初始最优路径设为默认顺序
dis_array = [[0]*n for i in range(n)] #距离矩阵，保存每两个城市之间的距离

#绘图显示最优路径
def draw_bestway():
    best_x = []
    best_y = []
    #从bestway中建立坐标序列
    for i in range(n):
        p = bestway[i]
        best_x.append(x[p])
        best_y.append(y[p])
    #加入开始点坐标，形成环路
    best_x.append(best_x[0])
    best_y.append(best_y[0])
    #利用plot函数绘图
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.title('TSP求解 赵炜 2310011059')
    plt.plot(best_x, best_y, color='green', linestyle='-', marker='o', markerfacecolor='red')
    plt.show()

#计算最优路径分值
def comp_bestway_score():
    best_x = []
    best_y = []
    #从bestway中建立坐标序列
    for i in range(n):
        p = bestway[i]
        best_x.append(x[p])
        best_y.append(y[p])
    value = 0.0
    for i in range(1,n):
        x2 = (best_x[i] - best_x[i-1]) * (best_x[i] - best_x[i-1])
        y2 = (best_y[i] - best_y[i-1]) * (best_y[i] - best_y[i-1])
        value = value + math.sqrt(x2 + y2)
    x2 = (best_x[0] - best_x[n-1]) * (best_x[0] - best_x[n-1])
    y2 = (best_y[0] - best_y[n-1]) * (best_y[0] - best_y[n-1])
    value = value + math.sqrt(x2 + y2)
    return (value)

def tabu_search(): #全局变量用于传递初始路径和计算路径分值
    global bestway
    obway = bestway.copy() #保存全局最优解
    way = bestway.copy() #保存当前路径
    obscore = comp_bestway_score() #保存全局最优分值
    tabu_long = 5 #设置禁忌长度
    tabulist = [0 for i in range(n)] #定义禁忌表
    print("way:",way,"obscore:",obscore)
    for iter in range(0,20):
        bestscore = 10000 #保存当前邻域中找到的最优解的分值
        for a in range(1, n):
            for b in range(a):
                bestway = way.copy()
                bestway[a], bestway[b] = bestway[b], bestway[a]
                score = comp_bestway_score()
                if(score < obscore):
                    obscore = score
                    obway = bestway.copy()
                    eli = 1
                    v1 = a; v2 = b
                elif(score < bestscore and tabulist[a] == 0 and tabulist[b] == 0):
                    bestscore = score
                    way = bestway.copy()
                    v1 = a; v2 = b
        way[v1],way[v2] = way[v2],way[v1]
        print("way:",way,"iter=",iter,"obscore:",bestscore)
        print("tabulist:",tabulist)
        for i in range(n):
            if(tabulist[i] > 0):
                tabulist[i] = tabulist[i] - 1
        tabulist[v1] = tabu_long
        tabulist[v2] = tabu_long
        bestway = obway.copy()

#主程序
print("\nTabu search:")
time_start=time.time()
bestway = [i for i in range(n)]  # 设置默认初始解
tabu_search()
time_end=time.time()
print("bestway:",bestway)
print("score:",comp_bestway_score())
print("totally time:",time_end - time_start)
draw_bestway()