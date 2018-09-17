
"""
    3.0：存储密码到文件
    4.0：打开文件
    5.0：定义一个密码工具类
    6.0：定义一个文件工具类
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


class FileTool:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():

    try_times = 5
    file_tool = FileTool('password.txt')
    while try_times > 0:

        password_str = input("请输入密码：")

        # 实例化对象
        password_tool = PasswordTool(password_str)

        password_tool.process_str()

        file_tool.write_to_file('密码：{} 强度：{}\n'.format(
            password_str, password_tool.strength_level))

        if(password_tool.strength_level == 3):
            print('恭喜,您的密码符合规范！')
            break

    if(try_times <= 0):
        print('尝试次数过多！')

    print('读取文件:')
    # 读取全部
    print(file_tool.read_from_file())


if __name__ == '__main__':
    main()
