"""
    日期：2018/09/06
    功能：AQI计算
"""


def cal_linear(iaql_lo, iaql_hi, bp_lo, bp_hi, cp):
    """
        范围缩放
    """
    return (iaql_hi-iaql_lo)*(cp-bp_lo)/(bp_hi-bp_lo) + iaql_lo


def cal_pm_iaqi(pm_val):
    """
        计算PM2.5的空气质量指数
    """
    if 0 <= pm_val < 36:
        return cal_linear(0, 50, 0, 35, pm_val)
    elif 36 <= pm_val < 76:
        return cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        return cal_linear(100, 150, 75, 115, pm_val)
    elif 116 <= pm_val < 151:
        return cal_linear(150, 200, 115, 150, pm_val)
    elif 151 <= pm_val < 251:
        return cal_linear(200, 300, 150, 250, pm_val)
    elif 251 <= pm_val < 351:
        return cal_linear(300, 400, 250, 350, pm_val)
    elif 351 <= pm_val < 501:
        return cal_linear(400, 500, 350, 500, pm_val)


def cal_co_iaqi(co_val):
    if 0 <= co_val <= 2:
        return cal_linear(0, 50, 0, 2, co_val)
    elif 2 < co_val <= 4:
        return cal_linear(50, 100, 2, 4, co_val)
    elif 4 < co_val <= 14:
        return cal_linear(100, 150, 4, 14, co_val)
    elif 14 < co_val <= 24:
        return cal_linear(150, 200, 14, 24, co_val)
    elif 24 < co_val <= 36:
        return cal_linear(200, 300, 24, 36, co_val)
    elif 36 < co_val <= 48:
        return cal_linear(300, 400, 36, 48, co_val)
    elif 48 < co_val <= 60:
        return cal_linear(400, 500, 48, 60, co_val)


def cal_aqi(param_list):
    pm_val = param_list[0]
    co_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)
    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)
    return max(iaqi_list)


def main():

    print('请输入一下信息，用空格分割开')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)
    aqi_val = cal_aqi(param_list)

    print('空气质量指数为：{}'.format(aqi_val))


if __name__ == "__main__":
    main()
