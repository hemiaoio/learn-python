
from datetime import datetime
import math


def main():
    input_date_str = input('请输入日期(yyyy/MM/dd):')

    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算之前月份天数总和及当前月份天数
    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    days = sum(days_in_month_tup[:month-1]) + day

    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month > 2:
        days += 1

    print(days)


if __name__ == '__main__':
    main()
