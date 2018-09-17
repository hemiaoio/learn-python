"""
    日期：2018/09/06
    功能：AQI计算
    版本：6.0
    使用 网页解析 解析 html 内容
"""

import requests
from bs4 import BeautifulSoup


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
        aqi_list.append((caption, value))
    return aqi_list


def main():
    city_pinyin = input('请输入城市拼音：')
    city_aqi = get_city_aqi(city_pinyin)
    print(city_aqi)


if __name__ == "__main__":
    main()
