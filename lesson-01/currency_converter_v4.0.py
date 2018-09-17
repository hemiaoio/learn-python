
def convert_currency(in_money,exchange_rate):
    out_money =  in_money * exchange_rate
    return out_money

USD_VS_RMB = 6.77

currency_str_value = input("请输入带单位的货币:")

# 获取货币单位
unit = currency_str_value[-3:]

if unit == 'CNY':
    exchange_rate = 1/USD_VS_RMB
elif unit == 'USD':
    exchange_rate = USD_VS_RMB
else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])

    result = convert_currency(in_money,exchange_rate)

    print('计算结果：',result)
else:
    print('不支持的单位')