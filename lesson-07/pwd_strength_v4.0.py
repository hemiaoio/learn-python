"""
    3.0：存储密码到文件
    4.0：打开文件
"""


def check_number_exists(str):
    isnumeric = False
    for c in str:
        if c.isnumeric():
            isnumeric = True
            break

    return isnumeric


def check_letter_exists(str):

    isalpha = False

    for c in str:
        if c.isalpha():
            isalpha = True
            break
    return isalpha


def main():

    try_times = 5

    while try_times > 0:

        password_str = input("请输入密码：")

        strength_level = 0

        # 规则一：密码长度大于8
        if len(password_str) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位！')
            try_times -= 1

        # 规则二：包含数字
        if check_number_exists(password_str):
            strength_level += 1
        else:
            print('密码中必须包含数字！')
            try_times -= 1

        # 规则三：包含字母
        if check_letter_exists(password_str):
            strength_level += 1
        else:
            print('密码中必须包含字母！')
            try_times -= 1

        f = open('password.txt', 'a')
        f.write('密码：{} 强度：{}\n'.format(password_str, strength_level))
        f.close()

        if(strength_level == 3):
            print('恭喜,您的密码符合规范！')
            break

    if(try_times <= 0):
        print('尝试次数过多！')
        
    print('读取文件:')
    f = open('password.txt', 'r')

    # 读取全部
    print(f.read())

    # 读取一行
    print(f.readline())

    # 读取行到列表
    lines = f.readlines()
    print(lines)

    f.close()


if __name__ == '__main__':
    main()
