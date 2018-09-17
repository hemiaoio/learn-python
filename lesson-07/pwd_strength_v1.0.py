
def check_number_exists(str):
    for c in str:
        if c.isnumeric():
            return True

    return False


def check_letter_exists(str):
    for c in str:
        if c.isalpha():
            return True

    return False


def main():
    password_str = input("请输入密码：")

    strength_level = 0

    # 规则一：密码长度大于8
    if len(password_str) >= 8:
        strength_level += 1
    else:
        print('密码长度要求至少8位！')

    # 规则二：包含数字
    if check_number_exists(password_str):
        strength_level += 1
    else:
        print('密码中必须包含数字！')

    # 规则三：包含字母
    if check_letter_exists(password_str):
        strength_level += 1
    else:
        print('密码中必须包含字母！')

    if(strength_level == 3):
        print('恭喜,您的密码符合规范！')
    
if __name__ == '__main__':
    main()
