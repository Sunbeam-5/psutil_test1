import math
import random

# 障碍圆的半径
R = 500

# 无人机A的初始位置和目标位置
A0 = (1000, 0)
A_target = (1000 + 500 + 30, 0)

# 无人机B的初始位置和目标位置
B0 = (3500, 0)
B_target = (3500 - 500 - 30, 0)

# 无人机速度
velocity = 10

# 模拟退火算法参数
initial_temperature = 1000
final_temperature = 0.1
cooling_rate = 0.99
max_iterations = 10000

def distance(p1, p2):
    # 计算两点之间的距离
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def intersect_circle(p1, p2):
    # 判断线段是否与障碍圆相交
    d1 = distance(p1, (0, 0))
    d2 = distance(p2, (0, 0))
    return (d1 < R and d2 > R) or (d1 > R and d2 < R)

def calculate_time(p1, p2):
    # 计算从点p1到点p2的时间
    return distance(p1, p2) / velocity

def calculate_path_length(path):
    # 计算路径的总长度
    total_length = 0
    for i in range(len(path) - 1):
        total_length += distance(path[i], path[i+1])
    return total_length

def generate_neighbor(solution):
    # 生成邻域解
    neighbor = solution.copy()
    idx = random.randint(0, len(solution) - 1)
    neighbor[idx] = (random.uniform(-1, 1) * 30 + neighbor[idx][0], random.uniform(-1, 1) * 30 + neighbor[idx][1])
    return neighbor

def acceptance_probability(current_cost, new_cost, temperature):
    # 计算接受新解的概率
    if new_cost < current_cost:
        return 1.0
    return math.exp((current_cost - new_cost) / temperature)

def simulated_annealing():
    # 模拟退火算法
    current_solution = [A0, B0]
    best_solution = current_solution.copy()
    current_time = calculate_time(A0, A_target)  # 无人机A到达目标位置的时间
    best_time = current_time

    temperature = initial_temperature
    iteration = 0

    while temperature > final_temperature and iteration < max_iterations:
        new_solution = generate_neighbor(current_solution)
        new_time = calculate_time(new_solution[0], A_target) + calculate_time(new_solution[1], B_target)

        if acceptance_probability(current_time, new_time, temperature) > random.random():
            current_solution = new_solution
            current_time = new_time

        if new_time < best_time:
            best_solution = new_solution
            best_time = new_time

        temperature *= cooling_rate
        iteration += 1

    return best_solution

# 运行模拟退火算法
best_solution = simulated_annealing()

# 计算最短路径的长度
shortest_path_length = calculate_path_length(best_solution)

# 打印最短路径的长度
print("最短路径的长度为:", shortest_path_length, "米")