"""
    功能：BMR计算器
    版本：v2.0
    日期：2018/8/20
"""


def main():
    
    y_or_n = 'n'
    while y_or_n != 'y':
        # 性别
        gender = input('性别：')

        # 体重（kg）
        weight_str = input('体重（kg）：')

        # 身高(cm)
        height_str = input('身高（cm）：')

        # 年龄
        age_str = input('年龄：')

        if (gender == '男'):
            # 男性
            bmr = 13.7 * float(weight_str) + 5.0 * \
                float(height_str) - 6.8 * int(age_str) + 66
        elif (gender == '女'):
            # 女性
            bmr = 9.6 * float(weight_str) + 1.8 * \
                float(height_str) - 4.7 * int(age_str) + 655
        else:
            bmr = -1

        if(bmr != -1):
            print('基础代谢率（大卡）：', bmr)
        else:
            print('不支持')
        
        y_or_n = input('是否退出程序(y/n)?')


if __name__ == '__main__':
    main()
