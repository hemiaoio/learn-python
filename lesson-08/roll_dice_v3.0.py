"""
    功能：模拟掷骰子
    版本：3.0
    2.0新增功能：模拟连个骰子
    3.0新增功能：可视化抛掷两个骰子的结果
"""

import random
import matplotlib
import matplotlib.pyplot as plt


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 1000

    result1_list = []
    result2_list = []
    result3_list = [0] * 11
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        result1_list.append(roll1)
        result2_list.append(roll2)
        result3_list[roll1+roll2-2] += 1

    result_dic = dict(zip(range(2, 13), result3_list))

    for i, x in result_dic.items():
        print('点数{}的次数：{}，频率：{}'.format(i, x, x/total_times))

    x = range(1, total_times+1)
    plt.scatter(x, result1_list, c='red', alpha=0.5)
    plt.scatter(x, result2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
