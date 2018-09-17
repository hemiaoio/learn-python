"""
    日期：2018/09/06
    功能：AQI计算
    版本：3.0
    CSV 库操作

    # 先从 filestream 取得 writer 
    writer = csv.writer(f)
    # 按行写数据 
    writer.writerow(rowdata)

    # 读数据
    data_list = writer.reader()

"""

import csv
import json
import os


def process_json_file(filepath):
    """
        解码json文件
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        city_list = json.load(f)
        return city_list


def process_csv_file(filepath):
    """
        解码csv文件
    """
    city_list = []
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            city_list.append(','.join(row))
        return city_list


def main():
    filepath = input('请输入文件名称：')

    file_name, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        # json文件
        process_json_file(filepath)
        pass
    elif file_ext == '.csv':
        pass

    city_list = process_json_file(filepath)

    # 先将JSON文件转成csv
    lines = []

    # 列名（表头）
    lines.append(city_list[0].keys())

    for city in city_list:
        lines.append(city.values())
    # 将数据写入csv
    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == "__main__":
    main()
