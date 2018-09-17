"""
    功能：模拟掷骰子
    版本：2.0
    2.0新增功能：模拟连个骰子
"""

import random


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100000

    result_list = [0] * 11
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        result_list[roll1+roll2-2] += 1

    for i, x in enumerate(result_list):
        print('点数{}的次数：{}，频率：{}'.format(i+2, x, x/total_times))
    print(result_list)


if __name__ == '__main__':
    main()
