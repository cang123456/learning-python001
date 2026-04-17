#coding=utf-8
import matplotlib
matplotlib.use('TkAgg')  # 切换到TkAgg后端
import matplotlib.pyplot as plt
import math
import time
import random

# 定义TSP结点坐标
x = [4350,4500,4300,4300,4300,4300,4350,4500,4300,4300,4300,4300,4950,5150,5525,5525,5525,5525,4950,5250,5550,4950,5150,5525,5525,5525,5525,4950,5250,5550,5875,5875,5875,5875,5675,5675,5875,5875,5875,5875,5675,5675,8125,8225,8325,8125,8225,8325,8675,8675,8675,8675,8675,8675,8675,8675,8675,8675,8425,8525,8675,8675,8675,8675,8675,8675,8675,8675,8675,8675,8425,8525,10850,10850,10850,10850,10900,11050,10850,10850,10850,10850,10900,11050,11500,11800,11500,11700,11500,11800,11500,11700,12075,12075,12225,12225,12075,12075,12100,12425,12425,12425,12425,12075,12075,12225,12225,12075,12075,12100,12425,12425,12425,12425,14675,14675,14775,14875,14975,15075,15225,15225,15225,15225,15225,15225,15225,15225,15225,15225,14775,14875,14975,15075,15225,15225,15225,15225,15225,15225,15225,15225,15225,15225]

y = [4425,4425,4725,4825,4950,5050,8875,8875,9175,9275,9400,9500,10600,10600,9525,9425,9225,9125,8875,8875,8875,6150,6150,5075,4975,4775,4675,4425,4425,4425,2325,2475,2625,2775,4825,4925,6775,6925,7075,7225,9275,9375,10150,10150,10150,5700,5700,5700,3150,3250,3350,3450,3550,3650,3750,3850,3950,4050,5700,5700,7600,7700,7800,7900,8000,8100,8200,8300,8400,8500,10150,10150,9500,9400,9275,9175,8875,8875,5050,4950,4825,4725,4425,4425,4425,4425,6150,6150,8875,8875,10600,10600,9525,9425,9375,9275,9225,9125,8875,7225,7075,6925,6775,5075,4975,4925,4825,4775,4675,4425,2775,2625,2475,2325,5700,10150,10150,10150,10150,10150,8500,8400,8300,8200,8100,8000,7900,7800,7700,7600,5700,5700,5700,5700,4050,3950,3850,3750,3650,3550,3450,3350,3250,3150]

n = len(x)  # 定义城市数
bestway = [i for i in range(n)]  # 保存最优路径，初始最优路径设为默认顺序
dis_array = [[0]*n for i in range(n)]  # 距离矩阵，保存每两个城市之间的距离

# 计算城市间距离矩阵
for i in range(n):
    for j in range(n):
        dis_array[i][j] = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)

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
    # 利用plot函数绘图
    plt.rcParams['font.sans-serif'] = 'SimHei'

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
    for i in range(1,n):
        x2 = (best_x[i] - best_x[i-1]) * (best_x[i] - best_x[i-1])
        y2 = (best_y[i] - best_y[i-1]) * (best_y[i] - best_y[i-1])
        value = value + math.sqrt(x2 + y2)
    x2 = (best_x[0] - best_x[n-1]) * (best_x[0] - best_x[n-1])
    y2 = (best_y[0] - best_y[n-1]) * (best_y[0] - best_y[n-1])
    value = value + math.sqrt(x2 + y2)
    return (value)

# 蚁群算法（蚁周模型）
def antcolony2():
    global bestway
    obscore = float('inf')  # 初始设为无穷大
    obway = [0] * n
    # 改进参数
    m = 100  # 增加蚂蚁数量，提高搜索能力
    q = 100  # 信息素总量
    t = 0.05  # 降低挥发率，保留更多信息素
    alpha = 1.0  # 信息素重要程度
    beta = 3.0  # 启发函数重要程度（增加对距离的重视）
    pheromone = [[1.0] * n for i in range(n)]  # 初始信息素设为1.0

    # 初始化信息素为启发式信息
    for i in range(n):
        for j in range(n):
            if i != j:
                if dis_array[i][j] > 0:
                    pheromone[i][j] = 1.0 / dis_array[i][j]  # 基于距离的初始信息素

    for iter in range(300):  # 增加迭代次数
        road = [[0] * n for i in range(m)]
        vc = [[0] * n for i in range(m)]

        # 随机选起点
        for i in range(m):
            v = random.randint(0, n-1)
            road[i][0] = v
            vc[i][v] = 1

        # 蚂蚁选路
        for i in range(n-1):
            for j in range(m):
                v = road[j][i]
                weight = [0.0] * n
                tolweight = 0.0

                # 计算权重（信息素^α / 距离^β）
                for k in range(n):
                    if vc[j][k] == 0:
                        if dis_array[v][k] > 0:
                            weight[k] = (pheromone[v][k] ** alpha) / (dis_array[v][k] ** beta)
                        else:
                            weight[k] = float('inf')  # 避免除以0
                    tolweight += weight[k]

                if tolweight == 0:
                    # 如果所有城市都被访问过，这种情况不应该发生
                    continue

                # 轮盘赌选择
                r = random.random()
                wheel = 0.0
                selected = 0
                for k in range(n):
                    if weight[k] > 0:
                        wheel += weight[k] / tolweight
                        if wheel >= r:
                            selected = k
                            break

                road[j][i+1] = selected
                vc[j][selected] = 1

        # 更新最优解
        for i in range(m):
            # 计算当前路径的分数
            current_path = road[i]
            current_score = 0.0
            for j in range(n):
                current_score += dis_array[current_path[j]][current_path[(j+1)%n]]
            
            if current_score < obscore:
                obscore = current_score
                obway = current_path.copy()

        # 信息素挥发
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1 - t)

        # 仅对最优路径进行信息素更新
        for i in range(m):
            road_path = road[i]
            road_score = 0.0
            for j in range(n):
                road_score += dis_array[road_path[j]][road_path[(j+1)%n]]
            
            # 仅对较优路径增加信息素
            if road_score < obscore * 1.2:  # 只对相对较好的路径进行信息素更新
                for j in range(n):
                    v1 = road_path[j]
                    v2 = road_path[(j+1)%n]
                    pheromone[v1][v2] += q / road_score
                    pheromone[v2][v1] += q / road_score

    bestway = obway.copy()



def run():
    print("蚁群算法 Ant Colony Algorithm:")
    time_start = time.time()
    antcolony2()
    time_end = time.time()
    print("bestway:", bestway)
    print("score:", comp_bestway_score())
    print("totally time:", time_end - time_start)
    # draw_bestway()

# 主程序
# if __name__ == '__main__':
#     print("\\nAnt Colony Algorithm:")
#     time_start = time.time()
#     antcolony2()
#     time_end = time.time()
#     print("bestway:", bestway)
#     print("score:", comp_bestway_score())
#     print("totally time:", time_end - time_start)
#     draw_bestway()