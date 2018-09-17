"""
    3.0：存储密码到文件
    4.0：打开文件
    5.0：定义一个密码工具类
"""


class PasswordTool:
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    def check_number_exists(self):
        isnumeric = False
        for c in self.password:
            if c.isnumeric():
                isnumeric = True
                break

        return isnumeric

    def check_letter_exists(self):

        isalpha = False

        for c in self.password:
            if c.isalpha():
                isalpha = True
                break
        return isalpha

    def process_str(self):
        # 规则一：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')

        # 规则二：包含数字
        if self.check_number_exists():
            self.strength_level += 1
        else:
            print('密码中必须包含数字！')

        # 规则三：包含字母
        if self.check_letter_exists():
            self.strength_level += 1
        else:
            print('密码中必须包含字母！')


def main():

    try_times = 5

    while try_times > 0:

        password_str = input("请输入密码：")

        # 实例化对象
        password_tool = PasswordTool(password_str)

        password_tool.process_str()

        f = open('password.txt', 'a')
        f.write('密码：{} 强度：{}\n'.format(
            password_str, password_tool.strength_level))
        f.close()

        if(password_tool.strength_level == 3):
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
