"""
    功能：52周存钱挑战
    版本：V5.0
    日期：2018/8/22
    新增：记录每周存款数
"""

import math
import datetime


def save_moeny_in_n_weeks(money_per_week, increase_money, total_weeks):
    # 账户累计
    sum_money = 0

    # 存款列表
    money_list = []
    # 每周账户累计
    saved_moeny_list = []
    # while(week_index <= total_weeks):
    for week_index in range(total_weeks):
        money_list.append(money_per_week)
        sum_money = math.fsum(money_list)
        saved_moeny_list.append(sum_money)
        print('第{}周：存入{}元，账户累计{}元'.format(
            week_index+1, money_per_week, sum_money))
        money_per_week += increase_money
        # week_index += 1
    return saved_moeny_list


def main():

    money_per_week_str = input('请输入第一周存入的金额：')
    # 每周存入的金额，初始第一周为10
    money_per_week = float(money_per_week_str)

    increase_money_str = input('请输入每周递增金额：')
    # 递增的金额
    increase_money = float(increase_money_str)

    total_weeks_str = input('请输入总共的周数：')
    # 总共周数
    total_weeks = int(total_weeks_str)

    sum_moeny_list = save_moeny_in_n_weeks(
        money_per_week, increase_money, total_weeks)

    print('总存款金额：{}'.format(sum_moeny_list[-1]))

    input_date_str = input('请输入日期(yyyy/mm/dd)：')

    input_date = datetime.datetime.strptime(input_date_str,format('%Y/%m/%d'))

    # week_num_str = input('请输入第几周：')

    # week_num = int(week_num_str)

    week_num = input_date.isocalendar()[1]

    print('第{}周的存款金额为{}'.format(week_num-1, sum_moeny_list[week_num]))


if __name__ == '__main__':
    main()
