"""
    功能：五角星的绘制
    版本：2.0
    日期：2018/8/17
"""

import turtle


def draw_pentagram(size):
    i = 0
    while(i < 5):
        turtle.forward(size)
        turtle.right(144)
        i = i+1


def main():
    # 设置初始位置为中心向左300
    turtle.penup()
    turtle.bk(300)
    turtle.pendown()

    # 设置笔的宽度和颜色
    turtle.pensize(3)
    turtle.pencolor('#EDCEAD')

    count = 0
    size = 50
    while(count < 10):
        draw_pentagram(size)
        size += 20
        count += 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()
