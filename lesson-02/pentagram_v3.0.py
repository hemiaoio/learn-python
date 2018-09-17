"""
    功能：五角星的绘制
    版本：3.0
    日期：2018/8/19
"""

import turtle


def draw_pentagram(size):
    i = 0
    while(i < 5):
        turtle.forward(size)
        turtle.right(144)
        i = i+1


def draw_recursive_pentagram(size):
    """
        迭代绘制五角星
    """
    i = 0
    while(i < 5):
        turtle.forward(size)
        turtle.right(144)
        i += 1
    # 五角星绘制完成

    size += 10
    if(size <= 300):
        draw_recursive_pentagram(size)


def main():
    # 设置初始位置为中心向左300
    turtle.penup()
    turtle.bk(300)
    turtle.pendown()

    # 设置笔的宽度和颜色
    # turtle.pensize(3)
    # turtle.pencolor('#EDCEAD')

    size = 50
    draw_recursive_pentagram(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
