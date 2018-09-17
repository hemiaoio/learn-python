"""
    功能：52周存钱挑战
    版本：V1.0
    日期：2018/8/22
"""


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
    sum_moeny = 0

    while(week_index <= total_weeks):
        sum_moeny += money_per_week
        print('第{}周：存入{}元，账户累计{}元'.format(
            week_index, money_per_week, sum_moeny))
        money_per_week += increase_money
        week_index += 1

if __name__ == '__main__':
    main()
