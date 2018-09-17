"""
    日期：2018/09/06
    功能：AQI计算
    版本：2.0
    JSON 库操作

    # 将对象写入 文件流
    json.dump(obj,filestream)

    # 从文件中读取 json
    obj = json.load(filestream)

    # 将对象写入 string
    json.dumps(obj,str)

    # 从string中读取json
    json.load(str)
"""

import json


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, 'r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    filepath = input('请输入JSON文件名称：')
    city_list = process_json_file(filepath)

    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]
    f = open('top5api.json', 'w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
