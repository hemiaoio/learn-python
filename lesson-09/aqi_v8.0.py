"""
    日期：2018/09/19
    功能：AQI计算
    版本：8.0
    爬取数据到本地文件
"""

import requests
from bs4 import BeautifulSoup
import csv


def get_city_aqi(city_pinyin):

    url = 'http://pm25.in/'+city_pinyin
    result = requests.get(url, timeout=30)
    soup = BeautifulSoup(result.text, 'lxml')
    value_list = soup.find_all('div', {'class': 'span1'})

    aqi_list = []
    for i in range(8):
        div_content = value_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        # aqi_list.append((caption, value))
        aqi_list.append(value)
    return aqi_list


def get_all_cities():
    url = 'http://pm25.in/'
    city_list = []
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))

    return city_list


def main():
    city_list = get_all_cities()
    # for city in city_list:
    #     name = city[0]
    #     pinyin = city[1]
    #     aqi = get_city_aqi(pinyin)
    #     print('{}:{}'.format(name,aqi))

    header = ['城市', '拼音', 'AQI', 'PM2.5/1h', 'PM10/1h',
              'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
    with open('china_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for index, city in enumerate(city_list):
            if index % 10 == 0:
                print('已处理：{}/{}'.format(index, len(city_list)))
            name = city[0]
            pinyin = city[1]
            aqi = get_city_aqi(pinyin)
            row = [name, pinyin]+aqi
            writer.writerow(row)


if __name__ == "__main__":
    main()
