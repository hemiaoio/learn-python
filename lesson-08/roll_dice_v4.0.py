"""
    功能：模拟掷骰子
    版本：3.0
    2.0新增功能：模拟连个骰子
    3.0新增功能：可视化抛掷两个骰子的结果
    4.0新增功能：使用直方图统计结果
"""

import random
import matplotlib
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000

    result_list = []
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        result_list.append(roll1+roll2)

    # normed=1 以 比率显示 Y轴，1 为分母
    # edgecolor 边线颜色
    # linewidth 边线宽度
    plt.hist(result_list, bins=range(2, 13), normed=10,
             edgecolor='#FFFFFF', linewidth=1)
    # 图表名称
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
