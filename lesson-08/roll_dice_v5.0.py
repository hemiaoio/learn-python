"""
    功能：模拟掷骰子
    版本：3.0
    2.0新增功能：模拟连个骰子
    3.0新增功能：可视化抛掷两个骰子的结果
    4.0新增功能：使用直方图统计结果
    5.0新增功能：使用科学计算库简化程序
"""

import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():

    roll1_arr = np.random.randint(1, 7, size=1000)
    roll2_arr = np.random.randint(1, 7, size=1000)
    roll3_arr = np.random.randint(1, 7, size=1000)

    result_list = roll1_arr + roll2_arr+roll3_arr

    hist, bins = np.histogram(result_list, bins=range(3, 6*3+2))

    print(hist)
    print(bins)
    # normed=1 以 比率显示 Y轴，1 为分母
    # edgecolor 边线颜色
    # linewidth 边线宽度
    plt.hist(result_list, bins=bins, normed=10,
             edgecolor='#FFFFFF', linewidth=1)
    # 图表名称
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
