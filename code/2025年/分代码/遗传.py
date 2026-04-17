# 遗传算法，初始化10条路径，迭代的交叉、突变，选择最优解
import matplotlib
matplotlib.use('TkAgg')  # 切换到TkAgg后端
import matplotlib.pyplot as plt
import math
import time
import random

# 定义TSP结点坐标（从1.py复制）
x = [4350,4500,4300,4300,4300,4300,4350,4500,4300,4300,4300,4300,4950,5150,5525,5525,5525,5525,4950,5250,5550,4950,5150,5525,5525,5525,5525,4950,5250,5550,5875,5875,5875,5875,5675,5675,5875,5875,5875,5875,5675,5675,8125,8225,8325,8125,8225,8325,8675,8675,8675,8675,8675,8675,8675,8675,8675,8675,8425,8525,8675,8675,8675,8675,8675,8675,8675,8675,8675,8675,8425,8525,10850,10850,10850,10850,10900,11050,10850,10850,10850,10850,10900,11050,11500,11800,11500,11700,11500,11800,11500,11700,12075,12075,12225,12225,12075,12075,12100,12425,12425,12425,12425,12075,12075,12225,12225,12075,12075,12100,12425,12425,12425,12425,14675,14675,14775,14875,14975,15075,15225,15225,15225,15225,15225,15225,15225,15225,15225,15225,14775,14875,14975,15075,15225,15225,15225,15225,15225,15225,15225,15225,15225,15225]

y = [4425,4425,4725,4825,4950,5050,8875,8875,9175,9275,9400,9500,10600,10600,9525,9425,9225,9125,8875,8875,8875,6150,6150,5075,4975,4775,4675,4425,4425,4425,2325,2475,2625,2775,4825,4925,6775,6925,7075,7225,9275,9375,10150,10150,10150,5700,5700,5700,3150,3250,3350,3450,3550,3650,3750,3850,3950,4050,5700,5700,7600,7700,7800,7900,8000,8100,8200,8300,8400,8500,10150,10150,9500,9400,9275,9175,8875,8875,5050,4950,4825,4725,4425,4425,4425,4425,6150,6150,8875,8875,10600,10600,9525,9425,9375,9275,9225,9125,8875,7225,7075,6925,6775,5075,4975,4925,4825,4775,4675,4425,2775,2625,2475,2325,5700,10150,10150,10150,10150,10150,8500,8400,8300,8200,8100,8000,7900,7800,7700,7600,5700,5700,5700,5700,4050,3950,3850,3750,3650,3550,3450,3350,3250,3150]

n = len(x)  # 定义城市数
bestway = [i for i in range(n)]  # 保存最优路径，初始最优路径设为默认顺序
dis_array = [[0]*n for i in range(n)]  # 距离矩阵，保存每两个城市之间的距离

# 绘图显示最优路径（从1.py复制）
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
    plt.title('TSP求解 遗传算法 仓正良 2310011043')
    plt.plot(best_x, best_y, color='green', linestyle='-', marker='o', markerfacecolor='red')
    plt.show()

# 计算最优路径分值（从1.py复制）
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

# 随机生成路径的函数
def randomway():
    global bestway
    # 创建一个随机路径
    bestway = list(range(n))
    random.shuffle(bestway)

def genetic():
    global bestway  # 全局变量用于传递初始路径和计算路径分值
    dna = [[0] * n for i in range(10)]  # 保存10条dna所代表的可行路径
    score = [[0] * 2 for i in range(10)]  # 保存10条路径的分值,0行存dna编号，1行存分值
    for i in range(10):
        randomway()
        dna[i] = bestway.copy()
        score[i][0], score[i][1] = i, comp_bestway_score()
    scorebysort = sorted(score, key=lambda x: x[1])  # 保存按分值排序后的结果

    # 迭代进化求解最优解,dnat保存交叉变异过程中的dna
    dnat = [[0] * n for i in range(8)]  # 0-1保存原始dna，2-3保存交叉后dna，4-7保存变异后dna
    for iter in range(100):
        # 选择操作
        r = random.randint(0, 54)  # 按照概率选择第1条dna
        if (r < 10):
            n1 = scorebysort[0][0]
        elif (r < 19):
            n1 = scorebysort[1][0]
        elif (r < 27):
            n1 = scorebysort[2][0]
        elif (r < 34):
            n1 = scorebysort[3][0]
        elif (r < 40):
            n1 = scorebysort[4][0]
        elif (r < 45):
            n1 = scorebysort[5][0]
        elif (r < 49):
            n1 = scorebysort[6][0]
        elif (r < 52):
            n1 = scorebysort[7][0]
        elif (r < 54):
            n1 = scorebysort[8][0]
        else:
            n1 = scorebysort[9][0]
        n2 = n1
        while (n2 == n1):  # 按照概率选择第2条dna（与第1条不同）
            r = random.randint(0, 54)
            if (r < 10):
                n2 = scorebysort[0][0]
            elif (r < 19):
                n2 = scorebysort[1][0]
            elif (r < 27):
                n2 = scorebysort[2][0]
            elif (r < 34):
                n2 = scorebysort[3][0]
            elif (r < 40):
                n2 = scorebysort[4][0]
            elif (r < 45):
                n2 = scorebysort[5][0]
            elif (r < 49):
                n2 = scorebysort[6][0]
            elif (r < 52):
                n2 = scorebysort[7][0]
            elif (r < 54):
                n2 = scorebysort[8][0]
            else:
                n2 = scorebysort[9][0]
        dnat[0] = dna[n1].copy()
        dnat[1] = dna[n2].copy()

        # 交叉操作
        # 交叉操作步骤1：选择交叉片段端点
        tag = 0  # 标记端点选择未完成
        while (tag == 0):  # 随机选择交叉片段的两个端点
            c1 = random.randint(0, n-1)
            c2 = random.randint(0, n-1)
            if (c1 == c2):  # 保证两端点不相同
                continue
            if (c2 < c1):  # 保证c1在前、c2在后
                c1, c2 = c2, c1
            if (c1 == 0 and c2 == 13):  # 保证片段不为整个dna序列
                continue
            tag = 1  # 成功选择两个断点c1,c2
        # 交叉操作步骤2：对dnat[0]用顺序交叉法，交叉结果存入dnat[2]
        for i in range(c1, c2+1):  # 将dnat[0]中c1~c2基因复制到dnat[2]中c1~c2位置
            dnat[2][i] = dnat[0][i]
        v = 0  # 从dnat[1]中顺序选择与dnat[2]中已有基因不重复的基因填入dnat[2]中c1前位置
        for i in range(0, c1):
            insert = 0
            while (insert == 0):
                find = 0  # 标记当前基因v是否与c1~c2中的基因冲突，find=0代表未发现冲突
                for j in range(c1, c2+1):
                    if (dnat[1][v] == dnat[2][j]):
                        find = 1
                        break
                if (find == 0):
                    dnat[2][i] = dnat[1][v]
                    insert = 1  # 插入成功
                v = v + 1
        for i in range(c2+1, n):  # 继续从dnat[1]中顺序选择与dnat[2]中已有基因不重复的基因填入dnat[2]中c2后位置
            insert = 0  # 记录当前位置基因是否插入成功，insert=0代表未插入成功
            while (insert == 0):
                find = 0  # 标记当前基因v是否与c1~c2中的基因冲突，find=0代表未发现冲突
                for j in range(c1, c2+1):
                    if (dnat[1][v] == dnat[2][j]):
                        find = 1
                        break
                if (find == 0):
                    dnat[2][i] = dnat[1][v]
                    insert = 1  # 插入成功
                v = v + 1
        # 交叉操作步骤3：对dnat[1]用顺序交叉法，交叉结果存入dnat[3]
        for i in range(c1, c2+1):  # 将dnat[1]中c1~c2基因复制到dnat[3]中c1~c2位置
            dnat[3][i] = dnat[1][i]
        v = 0  # 从dnat[0]中顺序选择与dnat[3]中已有基因不重复的基因填入dnat[3]中c1前位置
        for i in range(0, c1):
            insert = 0
            while (insert == 0):
                find = 0
                for j in range(c1, c2+1):
                    if (dnat[0][v] == dnat[3][j]):
                        find = 1
                        break
                if (find == 0):
                    dnat[3][i] = dnat[0][v]
                    insert = 1  # 插入成功
                v = v + 1
        for i in range(c2+1, n):  # 继续从dnat[0]中顺序选择与dnat[3]中已有基因不重复的基因填入dnat[3]中c2后位置
            insert = 0
            while (insert == 0):
                find = 0
                for j in range(c1, c2+1):
                    if (dnat[0][v] == dnat[3][j]):
                        find = 1
                        break
                if (find == 0):
                    dnat[3][i] = dnat[0][v]
                    insert = 1  # 插入成功
                v = v + 1

        # 突变操作
        for i in range(4):  # 复制dnat[0]-[3]到dnat[4]-[7]进行突变
            dnat[i + 4] = dnat[i].copy()
        for i in range(4, 8):  # 对dnat[4]-[7]随机选择两个不同基因交换
            tag = 0  # 突变成功标志，tag=0表示未能突变
            while (tag == 0):
                v1 = random.randint(0, n-1)
                v2 = random.randint(0, n-1)
                if (v1 != v2):
                    dnat[i][v1], dnat[i][v2] = dnat[i][v2], dnat[i][v1]
                    tag = 1

        # 更新操作
        tscore = [[0] * 2 for i in range(8)]  # 保存8条路径的分值,0行存dna编号，1行存分值
        for i in range(8):  # 计算8条dna的个体分值
            bestway = dnat[i].copy()
            tscore[i][0], tscore[i][1] = i, comp_bestway_score()
        tscorebysort = sorted(tscore, key=lambda x: x[1])  # 保存按分值排序后的结果
        dna[n1] = dnat[tscorebysort[0][0]].copy()
        dna[n2] = dnat[tscorebysort[1][0]].copy()
        for i in range(10):  # 对更新后的种群重新排序
            bestway = dna[i].copy()
            score[i][0], score[i][1] = i, comp_bestway_score()
        scorebysort = sorted(score, key=lambda x: x[1])  # 保存按分值排序后的结果

    # 将最终获取到的最优路径更新至bestway
    bestway = dna[scorebysort[0][0]].copy()

# 主程序
def run():
    print("遗传:")
    time_start = time.time()
    bestway = [i for i in range(n)]  # 设置默认初始解
    genetic()
    time_end = time.time()
    print("bestway:", bestway)
    print("score:", comp_bestway_score())
    print("totally time:", time_end - time_start)
    # draw_bestway()