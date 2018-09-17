"""
    功能：五角星的绘制
    版本：1.0
    日期：2018/8/17
"""

import turtle


def main():
    i = 0
    while(i < 5):
        turtle.forward(6*50)
        turtle.right(144)
        i = i+1

    turtle.exitonclick()


if __name__ == '__main__':
    main()
