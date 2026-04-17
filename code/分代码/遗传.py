# 遗传算法，初始化10条路径，迭代的交叉、突变，选择最优解
import matplotlib

matplotlib.use('TkAgg')  # 切换到TkAgg后端
import matplotlib.pyplot as plt
import math
import time
import random
import numpy as np

# 定义TSP结点坐标（从1.py复制）
x = [4350, 4500, 4300, 4300, 4300, 4300, 4350, 4500, 4300, 4300, 4300, 4300, 4950, 5150, 5525, 5525, 5525, 5525, 4950,
     5250, 5550, 4950, 5150, 5525, 5525, 5525, 5525, 4950, 5250, 5550, 5875, 5875, 5875, 5875, 5675, 5675, 5875, 5875,
     5875, 5875, 5675, 5675, 8125, 8225, 8325, 8125, 8225, 8325, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675,
     8675, 8425, 8525, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8425, 8525, 10850, 10850, 10850, 10850,
     10900, 11050, 10850, 10850, 10850, 10850, 10900, 11050, 11500, 11800, 11500, 11700, 11500, 11800, 11500, 11700,
     12075, 12075, 12225, 12225, 12075, 12075, 12100, 12425, 12425, 12425, 12425, 12075, 12075, 12225, 12225, 12075,
     12075, 12100, 12425, 12425, 12425, 12425, 14675, 14675, 14775, 14875, 14975, 15075, 15225, 15225, 15225, 15225,
     15225, 15225, 15225, 15225, 15225, 15225, 14775, 14875, 14975, 15075, 15225, 15225, 15225, 15225, 15225, 15225,
     15225, 15225, 15225, 15225]

y = [4425, 4425, 4725, 4825, 4950, 5050, 8875, 8875, 9175, 9275, 9400, 9500, 10600, 10600, 9525, 9425, 9225, 9125, 8875,
     8875, 8875, 6150, 6150, 5075, 4975, 4775, 4675, 4425, 4425, 4425, 2325, 2475, 2625, 2775, 4825, 4925, 6775, 6925,
     7075, 7225, 9275, 9375, 10150, 10150, 10150, 5700, 5700, 5700, 3150, 3250, 3350, 3450, 3550, 3650, 3750, 3850,
     3950, 4050, 5700, 5700, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 10150, 10150, 9500, 9400, 9275,
     9175, 8875, 8875, 5050, 4950, 4825, 4725, 4425, 4425, 4425, 4425, 6150, 6150, 8875, 8875, 10600, 10600, 9525, 9425,
     9375, 9275, 9225, 9125, 8875, 7225, 7075, 6925, 6775, 5075, 4975, 4925, 4825, 4775, 4675, 4425, 2775, 2625, 2475,
     2325, 5700, 10150, 10150, 10150, 10150, 10150, 8500, 8400, 8300, 8200, 8100, 8000, 7900, 7800, 7700, 7600, 5700,
     5700, 5700, 5700, 4050, 3950, 3850, 3750, 3650, 3550, 3450, 3350, 3250, 3150]

n = len(x)  # 定义城市数
bestway = [i for i in range(n)]  # 保存最优路径，初始最优路径设为默认顺序


# 绘图显示最优路径
def draw_bestway():
    best_x = []
    best_y = []
    for i in range(n):
        p = bestway[i]
        best_x.append(x[p])
        best_y.append(y[p])
    best_x.append(best_x[0])
    best_y.append(best_y[0])
    plt.rcParams['font.sans-serif'] = 'SimHei'

    plt.plot(best_x, best_y, color='green', linestyle='-', marker='o', markerfacecolor='red', markersize=3)
    plt.show()


# 计算路径分值
def compute_distance(route):
    """计算给定路径的总距离"""
    total_distance = 0.0
    for i in range(n):
        current_city = route[i]
        next_city = route[(i + 1) % n]
        dx = x[current_city] - x[next_city]
        dy = y[current_city] - y[next_city]
        total_distance += math.sqrt(dx * dx + dy * dy)
    return total_distance


def comp_bestway_score():
    return compute_distance(bestway)


# 遗传算法主函数
def genetic():
    global bestway

    # 参数设置
    POPULATION_SIZE = 50  # 种群大小
    ELITE_SIZE = 5  # 精英保留数量
    MUTATION_RATE = 0.3  # 突变率
    GENERATIONS = 500  # 迭代次数

    # 初始化种群
    population = []
    for _ in range(POPULATION_SIZE):
        individual = list(range(n))
        random.shuffle(individual)
        population.append(individual)

    # 计算初始适应度
    def calculate_fitness(individual):
        distance = compute_distance(individual)
        return 1.0 / (distance + 1.0)  # 距离越小，适应度越大

    # 选择操作 - 轮盘赌选择
    def selection(population, fitness_values):
        total_fitness = sum(fitness_values)
        probabilities = [f / total_fitness for f in fitness_values]
        selected_idx = np.random.choice(range(len(population)), size=2, p=probabilities)
        return population[selected_idx[0]], population[selected_idx[1]]

    # 交叉操作 - 部分映射交叉(PMX)
    def pmx_crossover(parent1, parent2):
        size = len(parent1)
        child = [-1] * size

        # 随机选择两个交叉点
        point1 = random.randint(0, size - 1)
        point2 = random.randint(0, size - 1)
        if point1 > point2:
            point1, point2 = point2, point1

        # 复制交叉片段
        for i in range(point1, point2 + 1):
            child[i] = parent1[i]

        # 映射关系
        mapping = {}
        for i in range(point1, point2 + 1):
            if parent2[i] not in child:
                mapping[parent1[i]] = parent2[i]

        # 填充剩余位置
        for i in range(size):
            if child[i] == -1:
                gene = parent2[i]
                while gene in mapping:
                    gene = mapping[gene]
                child[i] = gene

        return child

    # 突变操作 - 多种突变策略
    def mutate(individual):
        if random.random() < MUTATION_RATE:
            mutation_type = random.choice(['swap', 'reverse', 'scramble'])

            if mutation_type == 'swap':  # 交换突变
                i, j = random.sample(range(n), 2)
                individual[i], individual[j] = individual[j], individual[i]

            elif mutation_type == 'reverse':  # 逆转变异
                i, j = random.sample(range(n), 2)
                if i > j:
                    i, j = j, i
                individual[i:j + 1] = reversed(individual[i:j + 1])

            elif mutation_type == 'scramble':  # 扰乱突变
                i, j = random.sample(range(n), 2)
                if i > j:
                    i, j = j, i
                segment = individual[i:j + 1]
                random.shuffle(segment)
                individual[i:j + 1] = segment

        return individual

    # 2-opt局部优化
    def two_opt_optimize(route):
        best_route = route[:]
        improved = True

        while improved:
            improved = False
            best_distance = compute_distance(best_route)

            for i in range(1, n - 2):
                for j in range(i + 1, n):
                    if j - i == 1:
                        continue

                    new_route = best_route[:]
                    new_route[i:j + 1] = reversed(new_route[i:j + 1])
                    new_distance = compute_distance(new_route)

                    if new_distance < best_distance:
                        best_route = new_route
                        improved = True
                        break

                if improved:
                    break

        return best_route

    # 主进化循环
    best_individual = None
    best_fitness = float('inf')
    convergence_history = []

    for generation in range(GENERATIONS):
        # 计算适应度
        fitness_values = [calculate_fitness(ind) for ind in population]

        # 记录最佳个体
        distances = [compute_distance(ind) for ind in population]
        min_distance = min(distances)
        if min_distance < best_fitness:
            best_fitness = min_distance
            best_individual = population[distances.index(min_distance)].copy()

        convergence_history.append(min_distance)

        # 打印进度
        # if generation % 50 == 0:
            # print(f"Generation {generation}: Best Distance = {min_distance:.2f}")

        # 创建新一代种群
        new_population = []

        # 精英保留
        sorted_indices = np.argsort(distances)
        for i in range(ELITE_SIZE):
            new_population.append(population[sorted_indices[i]].copy())

        # 生成剩余个体
        while len(new_population) < POPULATION_SIZE:
            # 选择父母
            parent1, parent2 = selection(population, fitness_values)

            # 交叉
            child = pmx_crossover(parent1, parent2)

            # 突变
            child = mutate(child)

            # 有概率进行2-opt优化
            if random.random() < 0.1:  # 10%的概率进行局部优化
                child = two_opt_optimize(child)

            new_population.append(child)

        population = new_population

    # 最终优化
    best_individual = two_opt_optimize(best_individual)
    bestway = best_individual

    # 绘制收敛曲线
    plt.figure(figsize=(10, 5))
    plt.plot(convergence_history)
    plt.title('遗传算法收敛曲线')
    plt.xlabel('迭代次数')
    plt.ylabel('最优路径长度')
    plt.grid(True)
    plt.show()

    return best_fitness


# 主程序
def run():
    print("遗传算法优化TSP:")
    print(f"城市数量: {n}")

    time_start = time.time()

    # 运行遗传算法
    best_distance = genetic()

    time_end = time.time()

    print(f"最优路径: {bestway}")
    print(f"路径长度: {best_distance:.2f}")
    print(f"运行时间: {time_end - time_start:.2f}秒")

    # 绘制最优路径
    draw_bestway()


# 运行主程序
if __name__ == "__main__":
    run()