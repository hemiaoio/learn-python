
from datetime import datetime
import math


def is_leap_year(year):
    """
        判断年份是否为闰年！
    """
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))


def main():
    input_date_str = input('请输入日期(yyyy/MM/dd):')

    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    days = day
    for i in range(1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and month > 2:
        days += 1

    # # 计算之前月份天数总和及当前月份天数
    # days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # if is_leap_year(year):
    #     days_in_month_list[1] = 29
    # days = sum(days_in_month_list[:month-1]) + day

    print(days)


if __name__ == '__main__':
    main()
