# coding=utf-8
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import time
import random
import copy

# 定义TSP结点坐标
x = [4350, 4500, 4300, 4300, 4300, 4300, 4350, 4500, 4300, 4300, 4300, 4300, 4950, 5150, 5525, 5525, 5525, 5525, 4950,
     5250, 5550, 4950, 5150, 5525, 5525, 5525, 5525, 4950, 5250, 5550, 5875, 5875, 5875, 5875, 5675, 5675, 5875, 5875,
     5875, 5875, 5675, 5675, 8125, 8225, 8325, 8125, 8225, 8325, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675,
     8675, 8425, 8525, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8675, 8425, 8525, 10850, 10850, 10850,
     10850, 10900, 11050, 10850, 10850, 10850, 10850, 10900, 11050, 11500, 11800, 11500, 11700, 11500, 11800, 11500,
     11700, 12075, 12075, 12225, 12225, 12075, 12075, 12100, 12425, 12425, 12425, 12425, 12075, 12075, 12225, 12225,
     12075, 12075, 12100, 12425, 12425, 12425, 12425, 14675, 14675, 14775, 14875, 14975, 15075, 15225, 15225, 15225,
     15225, 15225, 15225, 15225, 15225, 15225, 15225, 14775, 14875, 14975, 15075, 15225, 15225, 15225, 15225, 15225,
     15225, 15225, 15225, 15225, 15225]

y = [4425, 4425, 4725, 4825, 4950, 5050, 8875, 8875, 9175, 9275, 9400, 9500, 10600, 10600, 9525, 9425, 9225, 9125, 8875,
     8875, 8875, 6150, 6150, 5075, 4975, 4775, 4675, 4425, 4425, 4425, 2325, 2475, 2625, 2775, 4825, 4925, 6775, 6925,
     7075, 7225, 9275, 9375, 10150, 10150, 10150, 5700, 5700, 5700, 3150, 3250, 3350, 3450, 3550, 3650, 3750, 3850,
     3950, 4050, 5700, 5700, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 10150, 10150, 9500, 9400, 9275,
     9175, 8875, 8875, 5050, 4950, 4825, 4725, 4425, 4425, 4425, 4425, 6150, 6150, 8875, 8875, 10600, 10600, 9525, 9425,
     9375, 9275, 9225, 9125, 8875, 7225, 7075, 6925, 6775, 5075, 4975, 4925, 4825, 4775, 4675, 4425, 2775, 2625, 2475,
     2325, 5700, 10150, 10150, 10150, 10150, 10150, 8500, 8400, 8300, 8200, 8100, 8000, 7900, 7800, 7700, 7600, 5700,
     5700, 5700, 5700, 4050, 3950, 3850, 3750, 3650, 3550, 3450, 3350, 3250, 3150]

n = len(x)
bestway = list(range(n))
dis_array = [[0] * n for _ in range(n)]

# 计算距离矩阵
for i in range(n):
    for j in range(n):
        if i != j:
            dis_array[i][j] = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)


def calculate_path_length(path):
    """高效计算路径长度"""
    length = 0
    for i in range(n - 1):
        length += dis_array[path[i]][path[i + 1]]
    length += dis_array[path[-1]][path[0]]  # 回到起点
    return length


def draw_bestway():
    best_x = [x[i] for i in bestway]
    best_y = [y[i] for i in bestway]
    best_x.append(best_x[0])
    best_y.append(best_y[0])

    plt.figure(figsize=(12, 8))
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.title('TSP求解 改进蚁群算法')
    plt.plot(best_x, best_y, color='blue', linestyle='-', linewidth=1, marker='o',
             markersize=4, markerfacecolor='red', alpha=0.7)
    plt.xlabel('X坐标')
    plt.ylabel('Y坐标')
    plt.grid(True, alpha=0.3)
    plt.show()


def two_opt_swap(path, i, k):
    """2-opt局部优化"""
    new_path = path[:i] + path[i:k + 1][::-1] + path[k + 1:]
    return new_path


def local_search_2opt(path):
    """2-opt局部搜索"""
    improved = True
    best_path = path[:]
    best_length = calculate_path_length(path)

    while improved:
        improved = False
        for i in range(n - 1):
            for k in range(i + 1, n):
                new_path = two_opt_swap(best_path, i, k)
                new_length = calculate_path_length(new_path)

                if new_length < best_length:
                    best_path = new_path
                    best_length = new_length
                    improved = True
                    break
            if improved:
                break
    return best_path


def antcolony_improved():
    """改进的蚁群算法"""
    global bestway

    best_length = float('inf')
    best_path = list(range(n))

    # 参数设置（可调整）
    num_ants = min(100, n)  # 蚂蚁数量
    alpha = 1.0  # 信息素重要程度
    beta = 3.0  # 启发式信息重要程度（原代码是2，提高可增强距离的引导）
    evaporation = 0.5  # 信息素挥发率
    q0 = 0.9  # 直接选择概率（用于精英策略）
    Q = 100  # 信息素常数

    # 初始化信息素矩阵
    initial_pheromone = 1.0 / (n * calculate_path_length(list(range(n))))
    pheromone = [[initial_pheromone] * n for _ in range(n)]

    for iteration in range(300):  # 增加迭代次数
        all_paths = []
        all_lengths = []

        # 每只蚂蚁构建路径
        for ant in range(num_ants):
            visited = [False] * n
            path = []

            # 随机选择起点
            start = random.randint(0, n - 1)
            path.append(start)
            visited[start] = True

            current = start

            # 构建完整路径
            for _ in range(n - 1):
                # 计算转移概率
                probabilities = []
                total = 0

                for next_city in range(n):
                    if not visited[next_city]:
                        tau = pheromone[current][next_city] ** alpha
                        eta = (1.0 / (dis_array[current][next_city] + 1e-10)) ** beta
                        prob = tau * eta
                        probabilities.append((next_city, prob))
                        total += prob

                if total == 0:
                    # 如果没有可用的概率，随机选择未访问城市
                    unvisited = [i for i in range(n) if not visited[i]]
                    next_city = random.choice(unvisited)
                else:
                    # 精英策略：以概率q0选择最优
                    if random.random() < q0:
                        next_city = max(probabilities, key=lambda x: x[1])[0]
                    else:
                        # 轮盘赌选择
                        r = random.random() * total
                        cumulative = 0
                        for city, prob in probabilities:
                            cumulative += prob
                            if cumulative >= r:
                                next_city = city
                                break

                path.append(next_city)
                visited[next_city] = True
                current = next_city

            # 计算路径长度
            length = calculate_path_length(path)

            # 局部优化（可选，每10代做一次）
            if iteration % 10 == 0:
                path = local_search_2opt(path)
                length = calculate_path_length(path)

            all_paths.append(path)
            all_lengths.append(length)

            # 更新全局最优
            if length < best_length:
                best_length = length
                best_path = path[:]
                print(f"迭代 {iteration}, 新最优长度: {best_length:.2f}")

        # 信息素挥发
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1 - evaporation)

        # 信息素更新（精英蚂蚁策略）
        # 1. 只更新最优路径
        delta_pheromone = Q / best_length
        for i in range(n - 1):
            pheromone[best_path[i]][best_path[i + 1]] += delta_pheromone
            pheromone[best_path[i + 1]][best_path[i]] += delta_pheromone
        # 回路
        pheromone[best_path[-1]][best_path[0]] += delta_pheromone
        pheromone[best_path[0]][best_path[-1]] += delta_pheromone

        # 2. 更新所有蚂蚁（可选）
        # for ant_idx in range(num_ants):
        #     delta = Q / all_lengths[ant_idx]
        #     path = all_paths[ant_idx]
        #     for i in range(n-1):
        #         pheromone[path[i]][path[i+1]] += delta
        #         pheromone[path[i+1]][path[i]] += delta
        #     pheromone[path[-1]][path[0]] += delta
        #     pheromone[path[0]][path[-1]] += delta

    # 最终局部优化
    best_path = local_search_2opt(best_path)
    best_length = calculate_path_length(best_path)

    bestway = best_path
    return best_length


def run():
    print("改进蚁群算法开始运行...")
    print(f"城市数量: {n}")

    time_start = time.time()
    best_score = antcolony_improved()
    time_end = time.time()

    print(f"最优路径: {bestway}")
    print(f"最优分数: {best_score:.2f}")
    print(f"运行时间: {time_end - time_start:.2f}秒")

    # 显示路径图
    draw_bestway()


if __name__ == '__main__':
    run()