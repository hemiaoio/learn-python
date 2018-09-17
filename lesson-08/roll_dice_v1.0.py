"""
    功能：模拟掷骰子
    版本：1.0
"""

import random


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100000

    result_list = [0] * 6
    for i in range(total_times):
        roll = roll_dice()
        result_list[roll-1] += 1

    for i, x in enumerate(result_list):
        print('点数{}的次数：{}，频率：{}'.format(i+1, x, x/total_times))
    print(result_list)


if __name__ == '__main__':
    main()
