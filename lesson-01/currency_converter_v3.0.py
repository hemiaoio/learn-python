USD_VS_RMB = 6.77

currency_str_value = input("请输入带单位的货币:")

i = 0

while currency_str_value != 'Q':
    i = i+1
    print('循环次数：',i)
    # 获取货币单位
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        rmb_str_value = currency_str_value[:-3]
        rmb_value = eval(rmb_str_value)
        usd_value = rmb_value / USD_VS_RMB
        print('CNY to USD :', usd_value)
    elif unit == 'USD':
        usd_str_value = currency_str_value[:-3]
        usd_value = eval(usd_str_value)
        rmb_value = usd_value * USD_VS_RMB
        print('USD to CNY:', rmb_value)
    else:
        print('暂不支持此单位')

    currency_str_value = input("请输入带单位的货币(输入Q则退出程序):")

