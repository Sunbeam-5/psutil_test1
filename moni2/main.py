import matplotlib.pyplot as plt
import numpy as np

# 障碍圆参数
obstacle_center = (0, 0)
obstacle_radius = 2

# 站点A和B的位置
point_a = (6, 4)
point_b = (0, 8)

# 绘制障碍圆
circle = plt.Circle(obstacle_center, obstacle_radius, color='r', alpha=0.5)
fig, ax = plt.subplots()
ax.add_patch(circle)

# 绘制站点A和B
ax.plot(point_a[0], point_a[1], 'ro', label='A')
ax.plot(point_b[0], point_b[1], 'bo', label='B')

# 绘制连线
ax.plot([point_b[0], point_a[0]], [point_b[1], point_a[1]], 'b--', label='B to A')

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