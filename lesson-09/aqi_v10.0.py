"""
    日期：2018/09/20
    功能：AQI计算
    版本：10.0
    利用pandas 数据清洗 和 可视化数据

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
import matplotlib.pyplot as plt


# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def main():
    # 获取数据
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data[['城市','AQI']])
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head(5))

    # 数据清洗
    # 只保留AQI大于0的数据

    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    print('基本统计：')
    print('AQI最大值：{}'.format(clean_aqi_data['AQI'].max()))
    print('AQI最小值：{}'.format(clean_aqi_data['AQI'].min()))
    print('AQI均值：{}'.format(clean_aqi_data['AQI'].mean()))

    print('TOP 50:')
    # 默认升序
    aqi_top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    aqi_top50_cities.plot(kind='bar', x='城市', y='AQI',
                          title='空气质量最好的50个城市', figsize=(20, 10))
    plt.savefig('top50_aqi_bar.png')
    # aqi_top50_cities.plot(kind='line', x='城市', y='AQI',
    #                        title='空气质量最好的50个城市', figsize=(20, 10))
    # plt.savefig('top50_aqi_line.png')
    plt.show()


if __name__ == "__main__":
    main()
