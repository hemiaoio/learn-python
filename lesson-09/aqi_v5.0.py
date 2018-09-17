"""
    日期：2018/09/06
    功能：AQI计算
    版本：5.0
    使用request 库从网络抓取aqi数据

"""

import requests


def get_html_text(url):
    result = requests.get(url, timeout=30)
    return result.text


def main():
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/'+city_pinyin
    html_text = get_html_text(url)
    aqi_div = '''    <div class="span12 data">
        <div class="span1">
          <div class="value">
            '''

    index = html_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_value = html_text[begin_index:end_index]
    print('空气质量为：{}'.format(aqi_value))


if __name__ == "__main__":
    main()
