"""
    日期：2018/09/20
    功能：AQI计算
    版本：9.0
    利用pandas分析数据

    # 一维数据
    Series
    ser_obj = pd.Series(list) 使用列表数据初始化一个series对象
    ser_obj.index 获取索引
    ser_obj.values 获取数据列表
    ser_obj[index] 获取指定位置数据
    
    ser_obj.head(5) 取前5数据
    ser_obj.tail(5) 取后5数据

    # 二维数据
    DataFrame
    df.head(5) 取前5数据
    df[columnName] 取指定列数据
    df[[columnName,columnName]] 取指定多列数据
"""

import pandas as pd


def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data[['城市','AQI']])
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head(5))

    print('基本统计：')
    print('AQI最大值：{}'.format(aqi_data['AQI'].max()))
    print('AQI最小值：{}'.format(aqi_data['AQI'].min()))
    print('AQI均值：{}'.format(aqi_data['AQI'].mean()))

    print('TOP 10:')
    # 默认升序
    aqi_top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print(aqi_top10_cities)

    print('Bottom 10:')
    aqi_bottom10_cities = aqi_data.sort_values(by=['AQI'],ascending=False).head(10)
    print(aqi_bottom10_cities)

    # 保存csv
    aqi_top10_cities.to_csv('top10_aqi.csv',index=False)
    aqi_bottom10_cities.to_csv('bottom10_aqi.csv',index=False)


if __name__ == "__main__":
    main()
