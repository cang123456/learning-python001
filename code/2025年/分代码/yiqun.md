# 改进蚁群算法求解TSP问题

## 项目概述

该Python程序使用改进的蚁群算法来解决旅行商问题（TSP），即寻找访问所有城市一次并返回起点的最短路径。程序不仅实现了基本的蚁群算法，还结合了2-opt局部优化策略，以提高解的质量。

## 功能特性

- 使用改进的蚁群算法求解TSP问题
- 集成2-opt局部优化策略提升解的质量
- 可视化最优路径
- 实时显示算法优化过程

## 算法原理

### 蚁群算法

蚁群算法是一种模拟蚂蚁觅食行为的启发式算法。蚂蚁在寻找食物时会在路径上留下信息素，信息素浓度越高的路径越容易被选择。在TSP问题中，算法通过模拟这一过程来寻找最短路径。

### 2-opt局部优化

2-opt是一种经典的路径优化策略，通过选择路径中的两个点，将这两点之间的路径段反转，以寻找更短的路径。

## 代码结构

### 主要变量

- [x](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L13-L21), [y](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L23-L31): 城市坐标的数组
- [n](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L33-L33): 城市数量
- [bestway](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L34-L34): 最优路径
- [dis_array](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L35-L35): 距离矩阵

### 核心函数

#### [calculate_path_length(path)](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L39-L45)
计算给定路径的总长度，包括从最后一个城市回到起始城市的距离。

#### [draw_bestway()](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L47-L58)
使用matplotlib绘制最优路径图，包含坐标轴、标题和路径可视化。

#### [two_opt_swap(path, i, k)](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L60-L62)
实现2-opt交换操作，将路径中索引i到k的路径段反转。

#### [local_search_2opt(path)](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L64-L80)
使用2-opt策略对给定路径进行局部优化，持续改进直到无法再优化。

#### [antcolony_improved()](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L82-L166)
实现改进的蚁群算法，包括：
- 初始化信息素矩阵
- 每只蚂蚁构建路径（基于概率选择）
- 精英策略（q0概率选择最优）
- 信息素挥发和更新
- 定期局部优化（每10代执行2-opt）

#### [run()](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L168-L184)
主运行函数，负责算法执行、时间统计和结果可视化。

## 算法参数

- [num_ants](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L95-L95): 蚂蚁数量，设置为min(100, n)
- [alpha](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L96-L96): 信息素重要程度，值为1.0
- [beta](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L97-L97): 启发式信息重要程度，值为3.0（提高此值可增强距离引导）
- [evaporation](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L98-L98): 信息素挥发率，值为0.5
- [q0](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L99-L99): 精英策略选择概率，值为0.9
- [Q](file:///D:/project/pyprj/pythonProject1/code/2025年/分代码/yiqun.py#L100-L100): 信息素常数，值为100
- 迭代次数：300次

## 使用方法

直接运行程序，程序将：
1. 自动执行改进蚁群算法
2. 在控制台输出优化过程
3. 显示最终的最优路径、分数和运行时间
4. 绘制最优路径图

## 依赖库

- matplotlib: 用于可视化路径
- math: 用于数学计算
- time: 用于时间测量
- random: 用于随机操作
- copy: 用于数据复制

## 优化策略

1. **精英策略**: 以q0概率直接选择最优路径，加快收敛速度
2. **2-opt局部优化**: 定期对解进行局部优化，提高解的质量
3. **自适应参数**: 根据问题规模调整蚂蚁数量
4. **信息素初始化**: 基于初始路径长度进行合理初始化

## 适用场景

- 旅行商问题（TSP）求解
- 路径优化问题
- 组合优化问题研究
- 启发式算法学习

## 注意事项

- 城市坐标数据已预定义在代码中
- 可根据需要调整算法参数以获得更好的结果
- 程序运行时间与城市数量和迭代次数成正比