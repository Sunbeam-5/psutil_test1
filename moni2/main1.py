import numpy as np
from scipy.optimize import minimize

# 障碍圆参数
obstacle_center = np.array([0, 0])
obstacle_radius = 2

# 站点A和B的位置
point_a = np.array([6, 4])
point_b = np.array([0, 8])

# A机的最优航迹（与问题1相同）
a_trajectory = np.array([point_a, point_b])

# 定义目标函数和约束函数
def objective(x):
    t_BE = x[0]
    t_EA = np.linalg.norm(point_a - point_e) / v_B
    return t_BE + t_EA

def constraint(x):
    t_BE = x[0]
    x_B = point_b[0] + t_BE * np.cos(angle_BE)
    y_B = point_b[1] + t_BE * np.sin(angle_BE)
    return (x_B - obstacle_center[0])**2 + (y_B - obstacle_center[1])**2 - obstacle_radius**2

# 初始值
t_BE_guess = np.linalg.norm(point_b - point_a) / v_B
x0 = [t_BE_guess]

# 优化求解
result = minimize(objective, x0, constraints={'type': 'eq', 'fun': constraint})

# 提取最优解
t_BE_opt = result.x[0]
t_EA_opt = np.linalg.norm(point_a - point_b) / v_B
t_B_opt = t_BE_opt + t_EA_opt

print(f"Optimal time for Drone B: {t_B_opt}")

# 绘图代码
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# 绘制障碍圆
obstacle = Circle(obstacle_center, obstacle_radius, color='r', alpha=0.5)

# 绘制航迹和点
fig, ax = plt.subplots()
ax.add_patch(obstacle)
ax.plot(a_trajectory[:, 0], a_trajectory[:, 1], 'r--', label='Drone A')
ax.plot([point_b[0], point_b[0] + t_BE_opt * np.cos(angle_BE)], [point_b[1], point_b[1] + t_BE_opt * np.sin(angle_BE)], 'g--', label='Drone B')
ax.plot(point_a[0], point_a[1], 'ro', label='A')
ax.plot(point_b[0], point_b[1], 'bo', label='B')
ax.plot(point_b[0] + t_BE_opt * np.cos(angle_BE), point_b[1] + t_BE_opt * np.sin(angle_BE), 'go', label='E')

# 设置图形参数
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Flight Trajectories')
plt.grid(True)
plt.legend()

# 显示图形
plt.show()