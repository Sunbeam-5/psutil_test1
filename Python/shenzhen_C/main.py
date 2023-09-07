import math
import random


def objective_function(x):
    # 定义目标函数，这里以一个简单的二维函数为例
    return math.sin(x[0]) + math.cos(x[1])


def acceptance_probability(old_cost, new_cost, temperature):
    # 计算接受新解的概率
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / temperature)


def simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    best_solution = current_solution
    current_temperature = initial_temperature

    for i in range(num_iterations):
        # 生成新的解
        new_solution = [current_solution[0] + random.uniform(-1, 1),
                        current_solution[1] + random.uniform(-1, 1)]

        # 计算当前解和新解的成本
        current_cost = objective_function(current_solution)
        new_cost = objective_function(new_solution)

        # 判断是否接受新解
        if acceptance_probability(current_cost, new_cost, current_temperature) > random.random():
            current_solution = new_solution

        # 更新最优解
        if objective_function(current_solution) > objective_function(best_solution):
            best_solution = current_solution

        # 降低温度
        current_temperature *= cooling_rate

    return best_solution


# 设置算法参数
initial_solution = [0, 0]  # 初始解
initial_temperature = 100.0  # 初始温度
cooling_rate = 0.95  # 温度衰减率
num_iterations = 1000  # 迭代次数

# 运行模拟退火算法
best_solution = simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations)

# 输出结果
print("Best solution:", best_solution)
print("Objective value:", objective_function(best_solution))