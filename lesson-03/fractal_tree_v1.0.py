"""
    功能：分形树
    版本：1.0
    日期：2018/08/19
"""

import turtle


def draw_branch(branch_length, pen_size):
    if(branch_length > 0):
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length-10, pen_size)

        turtle.left(40)
        draw_branch(branch_length-10, pen_size)

        turtle.right(20)
        turtle.backward(branch_length)


def main():

    # 画笔起始位置
    turtle.right(90)
    turtle.penup()
    turtle.forward(300)
    turtle.pendown()
    turtle.left(90)

    turtle.left(90)
    draw_branch(100, 5)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
