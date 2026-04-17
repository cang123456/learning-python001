#coding=utf-8
import matplotlib
matplotlib.use('TkAgg')  # 切换到TkAgg后端
import matplotlib.pyplot as plt
import math
import time
import random

# 定义TSP结点坐标
x = [16,16,20,22,25,22,20,17,16,17,16,21,19,20]
y = [96,94,92,93,97,96,97,96,98,98,97,95,97,94]

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
    plt.title('TSP求解 蚁群算法 李国政 2310011049')
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
    global bestway  # 全局变量用于计算路径分值和输出最优路径结果
    obscore = 10000  # 保存全局最优分值（初始值设为较大值）
    obway = [0] * n  # 保存全局最优路径
    # ----参数定义----
    m = 10  # 蚂蚁数量
    q = 10  # 一只蚂蚁巡回一周释放的信息素总量
    t = 0.5  # 信息素挥发率（0<t<1）
    pheromone = [[1] * n for i in range(n)]  # 初始化信息素浓度（所有路径初始为1）

    # 迭代寻找最优路径（迭代次数50）
    for iter in range(50):
        road = [[0] * n for i in range(m)]  # 保存m只蚂蚁的巡回路线
        vc = [[0] * n for i in range(m)]  # 标记蚂蚁已访问的城市（0=未访问，1=已访问）

        # 随机选择每只蚂蚁的出发城市
        for i in range(m):
            v = random.randint(0, n - 1)
            road[i][0] = v  # 记录起始城市
            vc[i][v] = 1  # 标记为已访问

        # 每只蚂蚁依次访问剩余n-1个城市
        for i in range(n - 1):  # 已访问1个城市，还需访问n-1个
            for j in range(m):  # 遍历每只蚂蚁
                v = road[j][i]  # 当前蚂蚁所在城市
                weight = [0] * n  # 权重（信息素/距离）
                p = [0] * n  # 选择概率
                tolweight = 0  # 权重总和

                # 计算未访问城市的权重
                for k in range(n):
                    if vc[j][k] == 0:  # 只计算未访问的城市
                        weight[k] = pheromone[v][k] / dis_array[v][k]
                    else:
                        weight[k] = 0
                    tolweight += weight[k]

                if tolweight == 0:
                    break  # 防止除数为0（理论上不会触发）

                # 计算选择概率
                for k in range(n):
                    p[k] = weight[k] / tolweight

                # 轮盘赌选择下一个城市
                r = random.random()  # 生成[0,1)随机数
                wheel = 0  # 轮盘累计值
                selected = 0
                for k in range(n):
                    wheel += p[k]
                    if wheel >= r:
                        selected = k
                        break

                road[j][i + 1] = selected  # 记录下一个城市
                vc[j][selected] = 1  # 标记为已访问

        # 计算每条路径的分值并更新全局最优
        roadscore = [0] * m  # 保存每条路径的总长度
        for i in range(m):
            bestway = road[i].copy()
            roadscore[i] = comp_bestway_score()  # 计算路径长度
            # 更新全局最优解
            if roadscore[i] < obscore:
                obscore = roadscore[i]
                obway = bestway.copy()

        # 更新信息素：先挥发
        for i in range(n):
            for j in range(n):
                pheromone[i][j] = t * pheromone[i][j]

        # 更新信息素：再添加蚂蚁释放的信息素（蚁周模型：巡回结束后更新）
        for i in range(m):
            # 遍历路径的每一段（包括回到起点）
            for j in range(n - 1):
                v1 = road[i][j]
                v2 = road[i][j + 1]
                pheromone[v1][v2] += q * 30 / roadscore[i]
                pheromone[v2][v1] += q * 30 / roadscore[i]  # 路径双向
            # 最后一个城市回到起点
            v1 = road[i][-1]
            v2 = road[i][0]
            pheromone[v1][v2] += q * 30 / roadscore[i]
            pheromone[v2][v1] += q * 30 / roadscore[i]

    # 最终最优路径更新到bestway
    bestway = obway.copy()

# 主程序
if __name__ == '__main__':
    print("\\nAnt Colony Algorithm:")
    time_start = time.time()
    antcolony2()
    time_end = time.time()
    print("bestway:", bestway)
    print("score:", comp_bestway_score())
    print("totally time:", time_end - time_start)
    draw_bestway()