"""
    功能：52周存钱挑战
    版本：V2.0
    日期：2018/8/22
    新增：记录每周存款数
"""

import math


def main():
    # 每周存入的金额，初始第一周为10
    money_per_week = 10

    # 第N周
    week_index = 1

    # 递增的金额
    increase_money = 10

    # 总共周数
    total_weeks = 52

    # 账户累计
    sum_money = 0

    # 存款列表
    money_list = []

    while(week_index <= total_weeks):
        money_list.append(money_per_week)
        sum_money = math.fsum(money_list)
        print('第{}周：存入{}元，账户累计{}元'.format(
            week_index, money_per_week, sum_money))
        money_per_week += increase_money
        week_index += 1

if __name__ == '__main__':
    main()
