import math
import random

# 定义问题的参数
radius = 500  # 障碍圆半径
center_distance_A = 1000  # A站点到圆心的距离
center_distance_B = 3500  # B站点到圆心的距离
speed = 10  # 无人机的恒定速度
turning_radius = 30  # 转弯半径

# 定义模拟退火的参数
initial_temperature = 1000
cooling_rate = 0.99
stopping_temperature = 0.1
iterations = 1000

# 生成初始解
def generate_initial_solution():
    # 假设无人机从A站点出发，直线飞向B站点
    angle = math.atan2(center_distance_B, radius)
    x = center_distance_A + radius * math.cos(angle)
    y = radius * math.sin(angle)
    solution = [(x, y)]
    return solution

# 计算航迹路径的总时间
def calculate_total_time(solution):
    total_time = 0
    for i in range(len(solution) - 1):
        distance = math.sqrt((solution[i+1][0] - solution[i][0])**2 + (solution[i+1][1] - solution[i][1])**2)
        total_time += distance / speed
    return total_time

# 生成邻域解
def generate_neighbor_solution(solution):
    # 随机选择一个点进行变动
    index = random.randint(1, len(solution) - 1)
    point = solution[index]
    x = point[0] + random.uniform(-turning_radius, turning_radius)
    y = point[1] + random.uniform(-turning_radius, turning_radius)
    new_solution = solution[:index] + [(x, y)] + solution[index+1:]
    return new_solution

# 接受准则
def acceptance_criteria(delta, temperature):
    if delta < 0:
        return True
    probability = math.exp(-delta / temperature)
    return random.random() < probability

# 模拟退火算法
def simulated_annealing():
    # 初始化
    temperature = initial_temperature
    solution = generate_initial_solution()
    best_solution = solution.copy()

    # 迭代搜索
    while temperature > stopping_temperature:
        for _ in range(iterations):
            neighbor_solution = generate_neighbor_solution(solution)
            delta = calculate_total_time(neighbor_solution) - calculate_total_time(solution)
            if acceptance_criteria(delta, temperature):
                solution = neighbor_solution.copy()
                if calculate_total_time(solution) < calculate_total_time(best_solution):
                    best_solution = solution.copy()
        temperature *= cooling_rate

    return best_solution

# 执行模拟退火算法
best_solution = simulated_annealing()
best_time = calculate_total_time(best_solution)

print("最优航迹路径：", best_solution)
print("最优用时：", best_time)