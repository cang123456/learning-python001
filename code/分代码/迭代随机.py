import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import time
import random

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

n = len(x)  # 定义城市数n
bestway = [i for i in range(n)]  # 保存最优路径，初始最优路径设为默认顺序


# 预先计算距离矩阵，提高计算效率
def calculate_distance_matrix():
    distance_matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                distance_matrix[i][j] = math.sqrt(dx * dx + dy * dy)
    return distance_matrix


# 创建距离矩阵（全局变量）
dist_matrix = calculate_distance_matrix()


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

    plt.plot(best_x, best_y, color='green', linestyle='-', marker='o', markerfacecolor="red")
    plt.show()


# 计算最优路径分值（使用距离矩阵优化）
def comp_bestway_score():
    value = 0.0
    for i in range(n - 1):
        value += dist_matrix[bestway[i]][bestway[i + 1]]
    value += dist_matrix[bestway[-1]][bestway[0]]  # 回到起点
    return value


# 计算指定路径的分值
def compute_route_score(route):
    value = 0.0
    for i in range(n - 1):
        value += dist_matrix[route[i]][route[i + 1]]
    value += dist_matrix[route[-1]][route[0]]
    return value


# 随机生成巡回路线
def randway():
    global bestway
    # 使用更高效的方法生成随机排列
    route = list(range(n))
    random.shuffle(route)
    for i in range(n):
        bestway[i] = route[i]
    return route


# 改进的2-opt优化函数
def two_opt_optimize(route, max_iterations=100):
    """对路径进行2-opt优化"""
    best_route = route.copy()
    best_score = compute_route_score(best_route)
    improved = True
    iteration = 0

    while improved and iteration < max_iterations:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                if j - i == 1:  # 相邻边，交换无意义
                    continue

                # 计算交换后的改进量（增量计算，提高效率）
                # 移除边 (i-1,i) 和 (j,j+1)
                # 添加边 (i-1,j) 和 (i,j+1)
                old_cost = (dist_matrix[best_route[i - 1]][best_route[i]] +
                            dist_matrix[best_route[j]][best_route[j + 1]])
                new_cost = (dist_matrix[best_route[i - 1]][best_route[j]] +
                            dist_matrix[best_route[i]][best_route[j + 1]])

                if new_cost < old_cost:
                    # 执行交换
                    best_route[i:j + 1] = reversed(best_route[i:j + 1])
                    best_score = best_score - old_cost + new_cost
                    improved = True

        iteration += 1

    return best_route, best_score


# 3-opt优化函数
def three_opt_optimize(route, max_iterations=50):
    """对路径进行3-opt优化"""
    best_route = route.copy()
    best_score = compute_route_score(best_route)
    improved = True
    iteration = 0

    while improved and iteration < max_iterations:
        improved = False

        for i in range(1, n - 4):
            for j in range(i + 1, n - 3):
                for k in range(j + 1, n - 2):
                    # 尝试不同的3-opt交换
                    current_segments = [
                        best_route[:i],
                        best_route[i:j],
                        best_route[j:k],
                        best_route[k:]
                    ]

                    # 尝试不同的重新连接方式
                    possible_reorders = [
                        (0, 1, 2, 3),  # 原始顺序
                        (0, 2, 1, 3),  # 交换中间两段
                        (0, 1, 3, 2),  # 交换后两段
                        (0, 3, 1, 2),  # 其他组合
                        (0, 2, 3, 1),
                        (0, 3, 2, 1)
                    ]

                    current_order = [0, 1, 2, 3]

                    for order in possible_reorders:
                        if order == tuple(current_order):
                            continue

                        new_route = []
                        for idx in order:
                            new_route.extend(current_segments[idx])

                        new_score = compute_route_score(new_route)

                        if new_score < best_score:
                            best_route = new_route
                            best_score = new_score
                            improved = True

        iteration += 1

    return best_route, best_score


# 插入优化：尝试将每个城市插入到更好的位置
def insertion_optimize(route):
    best_route = route.copy()
    best_score = compute_route_score(best_route)

    for i in range(n):
        current_city = best_route[i]
        # 从路径中移除当前城市
        temp_route = best_route[:i] + best_route[i + 1:]

        # 尝试插入到每个可能的位置
        for pos in range(len(temp_route) + 1):
            if pos == i:  # 原来的位置
                continue

            new_route = temp_route[:pos] + [current_city] + temp_route[pos:]
            new_score = compute_route_score(new_route)

            if new_score < best_score:
                best_route = new_route
                best_score = new_score
                break

    return best_route, best_score


def iterandway():
    global bestway
    # print("开始迭代优化...")

    bestscore = float('inf')
    obway = [0] * n

    # 多阶段优化策略
    phases = [
        {"iter": 2000, "optimizer": "two_opt"},  # 第一阶段：快速探索
        {"iter": 3000, "optimizer": "insertion"},  # 第二阶段：精细化调整
        {"iter": 2000, "optimizer": "three_opt"}  # 第三阶段：深度优化
    ]

    start_time = time.time()

    for phase_idx, phase in enumerate(phases):
        # print(f"\n阶段 {phase_idx + 1}/{len(phases)}: {phase['optimizer']} 优化")
        iterations = phase["iter"]
        optimizer = phase["optimizer"]

        for i in range(iterations):
            if i % 500 == 0 and i > 0:
                elapsed = time.time() - start_time
                # print(f"  已处理 {i}/{iterations} 次迭代, 当前最优分数: {bestscore:.2f}, 用时: {elapsed:.2f}秒")

            # 生成随机路径
            randway()
            current_route = bestway.copy()
            current_score = comp_bestway_score()

            # 应用相应的优化器
            if optimizer == "two_opt":
                optimized_route, optimized_score = two_opt_optimize(current_route)
            elif optimizer == "insertion":
                optimized_route, optimized_score = insertion_optimize(current_route)
            elif optimizer == "three_opt":
                optimized_route, optimized_score = three_opt_optimize(current_route)
            else:
                optimized_route, optimized_score = two_opt_optimize(current_route)

            # 更新最优路径
            if optimized_score < bestscore:
                bestscore = optimized_score
                obway = optimized_route.copy()
                # print(f"  发现更优解: {bestscore:.2f}")

        # 阶段结束时，确保bestway是最优的
        for j in range(n):
            bestway[j] = obway[j]

    # 最终全局优化
    # print("\n执行最终全局优化...")
    final_route, final_score = three_opt_optimize(obway, max_iterations=100)
    if final_score < bestscore:
        bestscore = final_score
        obway = final_route.copy()

    # 将最终获取到的最优路径更新至bestway
    for i in range(n):
        bestway[i] = obway[i]

    total_time = time.time() - start_time
    # print(f"\n优化完成，总用时: {total_time:.2f}秒")
    return total_time


def run():
    # 主程序
    # print("城市数量:", n)
    # print("初始路径:", bestway[:10], "...")  # 只显示前10个
    # print("初始路径分数:", comp_bestway_score())
    #
    print("迭代随机优化")
    total_time = iterandway()
    #
    # print("\n最终结果:")
    print("最优路径分数:", comp_bestway_score())
    print("总用时:", total_time, "秒")

    # 绘制结果
    # draw_bestway()


if __name__ == '__main__':
    run()